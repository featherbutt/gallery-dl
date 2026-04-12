# -*- coding: utf-8 -*-

# Copyright 2026 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://www.cosmos.so/"""

from .common import Extractor, Message
from .. import text, util

BASE_PATTERN = r"(?:https?://)?(?:www\.)?cosmos\.so"


class CosmosExtractor(Extractor):
    """Base class for cosmos extractors"""
    category = "cosmos"
    root = "https://www.cosmos.so"
    root_graphql = "https://api.cosmos.so/graphql"
    filename_fmt = "{id}{num:?_//}_{filename}.{extension}"

    def _init(self):
        self.fmt = self.config("format", "jpg")

    def request_graphql(self, opname, variables):
        headers = {
            "Accept"       : "application/graphql-response+json,"
                             "application/json;q=0.9",
            "content-type" : "application/json",
            "x-client-name": "cosmos-web",
        }
        data = {
            "operationName": opname,
            "variables"    : variables,
            "extensions"   : {
                "clientLibrary": {
                    "name"   : "@apollo/client",
                    "version": "4.1.4",
                },
            },
            "query"        : self.utils("graphql", opname),
        }
        return self.request_json(
            f"{self.root_graphql}?q={opname}", method="POST",
            headers=headers, json=data)["data"].popitem()[1]

    def items(self):
        for element in self.elements():
            element["date"] = self.parse_datetime_iso(element.get("createdAt"))

            if caption := element.pop("generatedCaption", None):
                element["description"] = caption.get("text", "")
            else:
                element["description"] = ""

            files = self._extract_files(element)
            element["count"] = len(files)

            yield Message.Directory, "", element
            for file in files:
                file.update(element)
                yield Message.Url, file["url"], file

    def _extract_files(self, ele):
        media = ele.pop("media")

        if medias := ele.pop("multipleMedia"):
            files = []
            for num, media in enumerate(medias, 1):
                media["num"] = num
                files.append(self._extract_media(media))
            return files

        return (self._extract_media(media),)

    def _extract_media(self, media):
        url = media["url"]
        if "mux" in media:
            mux = media["mux"]
            media["url"] = "ytdl:" + mux["playbackUrl"]
            media["_ytdl_manifest"] = "hls"
            media["_fallback"] = (mux.get("downloadableUrl") or
                                  mux.get("mp4Url"),)
            media["filename"] = url[url.rfind("/")+1:-4]
            media["extension"] = "mp4"
        else:
            media["url"] = f"{url}?format={self.fmt}"
            media["filename"] = url[url.rfind("/")+1:]
            media["extension"] = self.fmt
        return media

    def _pagination(self, opname, variables, unpack=False):
        while True:
            data = self.request_graphql(opname, variables)

            if unpack:
                for item in data["items"]:
                    yield item["element"]
            else:
                yield from data["items"]

            try:
                variables["pageCursor"] = cursor = data["meta"].get(
                    "nextPageCursor")
                if not cursor:
                    break
            except Exception as exc:
                self.traceback(exc)
                break


class CosmosElementExtractor(CosmosExtractor):
    subcategory = "element"
    pattern = BASE_PATTERN + r"/e/(\d+)"
    example = "https://cosmos.so/e/1234567890"

    def elements(self):
        return (self.request_graphql("GetElementDetails", {
            "elementId" : int(self.groups[0]),
            "userId"    : 0,
            "isLoggedIn": False,
        })["element"],)


class CosmosSearchExtractor(CosmosExtractor):
    subcategory = "search"
    directory_fmt = ("{category}", "Search", "{search_tags}")
    pattern = BASE_PATTERN + r"/search/elements/([^/?#]+)"
    example = "https://www.cosmos.so/search/elements/QUERY"

    def elements(self):
        self.kwdict["search_tags"] = tag = text.unquote(self.groups[0])
        return self._pagination("SearchGlobalElements", {
            "searchTerm" : tag,
            "origin"     : "SEARCH_BOX",
            "contentType": None,
            "order"      : None,
            "color"      : None,
        })


class CosmosCollectionExtractor(CosmosExtractor):
    subcategory = "collection"
    directory_fmt = ("{category}", "{user[username]} ({user[id]})",
                     "{collection[name]} ({collection[id]})")
    pattern = BASE_PATTERN + r"/([^/?#]+)/([^/?#]+)"
    example = "https://cosmos.so/USER/COLLECTION"

    def elements(self):
        username, collection = self.groups
        variables = {
            "slug"           : text.unquote(collection),
            "ownerUsername"  : text.unquote(username),
            "userId"         : 0,
            "fetchSubCluster": False,
            "isLoggedIn"     : False,
        }
        self.kwdict["collection"] = cluster = self.request_graphql(
            "GetClusterBasic", variables)
        self.kwdict["user"] = cluster.pop("owner", None)

        variables = {
            "clusterId"       : cluster["id"],
            "userId"          : 0,
            "isLoggedIn"      : False,
            "showCollaborator": False,
        }
        return self._pagination("GetClusterElements", variables, True)


class CosmosUserExtractor(CosmosExtractor):
    subcategory = "user"
    directory_fmt = ("{category}", "{user[username]} ({user[id]})")
    pattern = BASE_PATTERN + r"/(\w+)"
    example = "https://cosmos.so/USER"

    def elements(self):
        user = self.kwdict["user"] = self._extract_user(self.groups[0])
        variables = {
            "userId"       : user["id"],
            "callingUserId": 0,
            "isLoggedIn"   : False,
        }
        return self._pagination("GetUserPublicElementsV2", variables)

    def _extract_user(self, username):
        try:
            page = self.request(f"{self.root}/{username}").text
            data = text.extr(page, '":{"data":{"user":{', '},"networkStatus"')
            return util.json_loads(f'{{"user":{{{data}}}')["user"]
        except Exception:
            raise self.exc.NotFoundError("user")
