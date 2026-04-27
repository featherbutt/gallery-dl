# # -*- coding: utf-8 -*-

# # Copyright 2026 Mike Fährmann
# #
# # This program is free software; you can redistribute it and/or modify
# # it under the terms of the GNU General Public License version 2 as
# # published by the Free Software Foundation.

# """Extractors for https://framedsc.com/"""

from .common import Extractor, Message
from .. import text

IMAGE_DB = "https://raw.githubusercontent.com/originalnicodrgitbot/hall-of-framed-db/main/shotsdb.json"
AUTHOR_DB = "https://raw.githubusercontent.com/originalnicodrgitbot/hall-of-framed-db/main/authorsdb.json"

class BaseFramedscExtractor(Extractor):
    """Base Class for framedsc extractors"""
    category = "framedsc"
    archive_fmt = "{filename}"

    def _init(self):
        self.image_db = self.request(IMAGE_DB).json()['_default']
        self.author_db = self.request(AUTHOR_DB).json()['_default']

    def process_image(self, url):
        url = text.ensure_http_scheme(url)
        image = text.nameext_from_url(url, {"url": url})
        yield Message.Directory, "", image
        yield Message.Url, url, image

class FramedscImageExtractor(BaseFramedscExtractor):
    """Extractor for single framedsc image"""
    subcategory = "image"
    archive_fmt = "{filename}"
    
    pattern = r"(?:https?://)?(?:www\.)?framedsc\.com/HallOfFramed/\?imageId=(\d+)"
    example = "https://framedsc.com/HallOfFramed/?imageId=12345"

    def __init__(self, match):
        Extractor.__init__(self, match)
        self.image_id = int(match[1])
    
    def items(self):
        for image in self.image_db.values():
            if image['epochTime'] == self.image_id:
                yield from self.process_image(image['shotUrl'])
                return
        
class FramedscAltImageExtractor(BaseFramedscExtractor):
    """Extractor for single framedsc image (alternative link)"""
    subcategory = "image"
    pattern = r"(?:https?://)?cdn\.framedsc\.com/images/([^/?#]+)"
    example = "https://cdn.framedsc.com/images/NAME.EXT"

    def items(self):
        yield from self.process_image(self.url)