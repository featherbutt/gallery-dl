# -*- coding: utf-8 -*-
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

# """Extractors for https://framedsc.com/"""

from .common import Extractor, Message
from .. import text

RELATIONS = ["<", "=", ">"]

IMAGE_DB = (
    "https://raw.githubusercontent.com/"
    "originalnicodrgitbot/"
    "hall-of-framed-db/"
    "main/"
    "shotsdb.json"
)

AUTHOR_DB = (
    "https://raw.githubusercontent.com/"
    "originalnicodrgitbot/"
    "hall-of-framed-db/"
    "main/"
    "authorsdb.json"
)


class BaseFramedscExtractor(Extractor):
    """Base Class for framedsc extractors"""
    category = "framedsc"
    archive_fmt = "{filename}"

    def _init(self):
        self.image_db = {}
        self.author_db = {}

    def setup_db(self):
        self.image_db = self.request(IMAGE_DB).json()['_default']
        self.author_db = self.request(AUTHOR_DB).json()['_default']

    def find_author(self, author_nick):
        for author in self.author_db.values():
            if author['authorNick'] == author_nick:
                return author['authorid']

    def process_image(self, url):
        url = text.ensure_http_scheme(url)
        image = text.nameext_from_url(url, {"url": url})
        yield Message.Directory, "", image
        yield Message.Url, url, image


class FramedscImageExtractor(BaseFramedscExtractor):
    """Extractor for single framedsc image"""
    subcategory = "image"
    archive_fmt = "{filename}"

    pattern = (
        r"(?:https?://)?(?:www\.)?"
        r"framedsc\.com/HallOfFramed/\?"
        r"[^?]*imageId=(\d+)"
    )

    example = "https://framedsc.com/HallOfFramed/?imageId=12345"

    def __init__(self, match):
        Extractor.__init__(self, match)
        self.image_id = int(match[1])

    def items(self):
        self.setup_db()
        for image in self.image_db.values():
            if image['epochTime'] == self.image_id:
                yield from self.process_image(image['shotUrl'])
                return


class FramedscRawExtractor(BaseFramedscExtractor):
    """Extractor for single framedsc image (raw image link)"""
    subcategory = "raw"
    pattern = r"(?:https?://)?cdn\.framedsc\.com/images/([^/?#]+)"
    example = "https://cdn.framedsc.com/images/NAME.EXT"

    def items(self):
        yield from self.process_image(self.url)


class FramedscSearchExtractor(BaseFramedscExtractor):
    """Extractor for framedsc image searches"""
    subcategory = "search"
    archive_fmt = "{filename}"

    pattern = (
        r"(?:https?://)?(?:www\.)?"
        r"framedsc\.com/HallOfFramed/\?"
        r"(?!.*imageId=)(.*)"
    )
    example = "https://framedsc.com/HallOfFramed/?author=AUTHOR&title=TITLE"

    def __init__(self, match):
        Extractor.__init__(self, match)
        self.filters_str = match[1]

    def clean_filters(self, unclean_filters):
        def valid_date(date):
            return bool(self.parse_datetime_iso(date))

        def valid_int(integer):
            try:
                int(integer)
                return True
            except (ValueError):
                return False

        filters = {
            'author': [],
            'title': [],
            'on': [],
            'before': [],
            'after': [],
            'color': [],
            'width': {
                '>': [],
                '<': [],
                '=': []
            },
            'height': {
                '>': [],
                '<': [],
                '=': []
            },
            'score': {
                '>': [],
                '<': [],
                '=': []
            },
        }

        for (field, value) in unclean_filters.items():
            value = text.unquote(value)

            if field == 'author':
                filters[field].append(self.find_author(value))
            elif field == 'title':
                filters[field].append(value.replace("+", " "))
            elif field == 'width' or field == 'height' or field == 'score':
                if len(value) == 0 or not (value[0] == '>' or value[0] == '<'):
                    filters[field]['='].append(value[1:])
                else:
                    filters[field][value[0]].append(value[1:])
            else:
                if field in filters.keys():
                    filters[field].append(value)

        for field in ['on', 'before', 'after']:
            if len(filters[field]) > 0:
                filters[field] = [
                    self.parse_datetime_iso(date)
                    for date in filters[field] if valid_date(date)
                ]
                if len(filters[field]) == 0:
                    return

        for field in ['width', 'height', 'score']:
            field_exists = False
            for relation in RELATIONS:
                field_exists = len(filters[field][relation]) > 0
                filters[field][relation] = [
                    int(integer)
                    for integer in filters[field][relation]
                    if valid_int(integer)
                ]

            if field_exists and all(
                    [
                        len(filters[field][relation]) == 0
                        for relation in RELATIONS
                    ]):
                return

        return filters

    def find_images(self, filters):
        def any_match_strict(image_field, target_fields):
            return any(
                [image_field == target_field for target_field in target_fields]
            )

        def any_greater_strict(image_field, target_fields):
            return any(
                [image_field >= target_field for target_field in target_fields]
            )

        def any_less_strict(image_field, target_fields):
            return any(
                [image_field <= target_field for target_field in target_fields]
            )

        def any_match(image_field, target_fields):
            return len(target_fields) == 0 or any_match_strict(
                image_field, target_fields)

        def any_greater(image_field, target_fields):
            return len(target_fields) == 0 or any_greater_strict(
                image_field, target_fields)

        def any_less(image_field, target_fields):
            return len(target_fields) == 0 or any_less_strict(
                image_field, target_fields)

        def integer_field_check(image, field):
            filter_dne = all([len(filters[field][relation]) ==
                             0 for relation in RELATIONS])

            equal = any_match_strict(image[field], filters[field]["="])
            greater = any_greater_strict(image[field], filters[field][">"])
            less = any_less_strict(image[field], filters[field]["<"])

            return filter_dne or equal or greater or less

        def title_check(title, target_titles):
            return len(target_titles) == 0 or any(
                [title.find(target_title) != -1
                 for target_title in target_titles]
            )

        images = []

        if not filters:
            return images

        for image in self.image_db.values():
            author = any_match(image['author'], filters['author'])
            title = title_check(image['gameName'], filters['title'])
            color = any_match(image['colorName'], filters['color'])

            before = any_less(
                self.parse_datetime_iso(
                    image['date'][:10]
                ), filters['before']
            )
            on = any_match(
                self.parse_datetime_iso(
                    image['date'][:10]
                ), filters['on']
            )
            after = any_greater(
                self.parse_datetime_iso(
                    image['date'][:10]
                ), filters['after']
            )

            width = integer_field_check(image, "width")
            height = integer_field_check(image, "height")
            score = integer_field_check(image, "score")

            if all([author, title, color, before,
                   on, after, width, height, score]):
                images.append(image['shotUrl'])

        return images

    def download_images(self, images):
        for image in images:
            yield from self.process_image(image)

    def items(self):
        self.setup_db()
        unclean_filters = text.parse_query(self.filters_str)
        filters = self.clean_filters(unclean_filters)
        images = self.find_images(filters)
        yield from self.download_images(images)
