# -*- coding: utf-8 -*-

# Copyright 2026 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://www.comicartfans.com/"""

from .common import Extractor, Message
from .. import text

BASE_PATTERN = r"(?i)(?:https?://)?(?:www\.)?comicartfans\.com"


class ComicartfansExtractor(Extractor):
    """Base class for comicartfans extractors"""
    category = "comicartfans"
    root = "https://www.comicartfans.com"


class ComicartfansArtworkExtractor(ComicartfansExtractor):
    subcategory = "artwork"
    directory_fmt = ("{category}", "{owner}")
    filename_fmt = "{id}{num:?_//} {title}.{extension}"
    archive_fmt = "{id}_{num}"
    pattern = BASE_PATTERN + r"/gallerypiece\.asp\?piece=(\d+)"
    example = "https://www.comicartfans.com/gallerypiece.asp?piece=12345"

    def items(self):
        iid = self.groups[0]
        url = f"{self.root}/gallerypiece.asp?piece={iid}"
        extr = text.extract_from(self.request(url, encoding="utf-8").text)

        work = {
            "id"      : text.parse_int(iid),
            "views"   : text.parse_int(extr('id="likecount-load">', "&")),
            "comments": text.parse_int(extr("-&nbsp;", "&")),
            "likes"   : text.parse_int(extr("-&nbsp;", "&")),
            "file_url": extr('<img src="', '"'),
            "additional" : extr(
                ">Additional Images</h5>", '<div style="clear: both;"></div>'),
            "location": text.unescape(extr(
                "<b>Location:</b>", "</a>").rpartition(">")[2]),
            "title"   : text.unescape(extr("<b>Title:</b>", "<").strip()),
            "artist"  : text.split_html(extr("<b>Artist:</b>", "<br>"))[1::2],
            "media_type" : extr("<b>Media Type:</b>", "<").lstrip(),
            "art_type": extr("<b>Art Type:</b>", "<").lstrip(),
            "sale_status": extr("<b>For Sale Status:</b>", "<").lstrip(),
            "date"    : self.parse_datetime(extr(
                "<b>Added to Site:</b>", "<").lstrip(), "%m/%d/%Y"),
            "description": text.unescape(extr(
                'content description-box">', "</div>").strip()),
            "owner_id": text.parse_int(extr(
                '>\n<a href="gallerydetail.asp?gcat=', '"')),
            "owner"   : text.unescape(extr(">", "<")).strip(),
            "owner_date" : self.parse_datetime(extr(
                "<b>Member Since:</b>", "<").lstrip(), "%B&nbsp;%Y"),
            "owner_website": extr("<b>Website:</b>	<a href='", "'"),
            "owner_country": text.extr(extr(
                '<b>Country:</b>', '"'), ">", "<").capitalize(),
        }

        if additional := work.pop("additional", None):
            additional = additional.split('<a href="')
            work["count"] = len(additional)
            del additional[0]
        else:
            work["count"] = 1

        yield Message.Directory, "", work

        url = work["file_url"]
        work["num"] = 1 if additional else 0
        text.nameext_from_url(url, work)
        yield Message.Url, url, work

        if additional:
            for work["num"], file in enumerate(additional, 2):
                work["title"] = text.unescape(text.extr(
                    file, 'data-caption="', '"'))
                url = file[:file.find('"')]
                text.nameext_from_url(url, work)
                yield Message.Url, url, work
