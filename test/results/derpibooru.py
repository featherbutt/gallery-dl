# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import philomena


__tests__ = (
{
    "#url"     : "https://derpibooru.org/images/1",
    "#category": ("philomena", "derpibooru", "post"),
    "#class"   : philomena.PhilomenaPostExtractor,
    "#count"       : 1,
    "#sha1_content": "88449eeb0c4fa5d3583d0b794f6bc1d70bf7f889",

    "animated"        : False,
    "aspect_ratio"    : 1.0,
    "comment_count"   : int,
    "created_at"      : "2012-01-02T03:12:33Z",
    "date"            : "dt:2012-01-02 03:12:33",
    "deletion_reason" : None,
    "description"     : "",
    "downvotes"       : int,
    "duplicate_of"    : None,
    "duration"        : 0.04,
    "extension"       : "png",
    "faves"           : int,
    "first_seen_at"   : "2012-01-02T03:12:33Z",
    "format"          : "png",
    "height"          : 900,
    "hidden_from_users": False,
    "id"              : 1,
    "mime_type"       : "image/png",
    "name"            : "1__safe_fluttershy_solo_cloud_happy_flying_upvotes+galore_artist-colon-speccysy_get_sunshine",
    "orig_sha512_hash": None,
    "processed"       : True,
    "representations" : dict,
    "score"           : int,
    "sha512_hash"     : "f16c98e2848c2f1bfff3985e8f1a54375cc49f78125391aeb80534ce011ead14e3e452a5c4bc98a66f56bdfcd07ef7800663b994f3f343c572da5ecc22a9660f",
    "size"            : 860914,
    "source_url"      : "https://web.archive.org/web/20110702164313/http://speccysy.deviantart.com:80/art/Afternoon-Flight-215193985",
    "spoilered"       : False,
    "tag_count"       : int,
    "tag_ids"         : list,
    "tags"            : list,
    "thumbnails_generated": True,
    "updated_at"      : r"re:\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ",
    "uploader"        : "Clover the Clever",
    "uploader_id"     : 211188,
    "upvotes"         : int,
    "view_url"        : str,
    "width"           : 900,
    "wilson_score"    : float,
},

{
    "#url"     : "https://derpibooru.org/images/3334658",
    "#comment" : "svg (#5643)",
    "#category": ("philomena", "derpibooru", "post"),
    "#class"   : philomena.PhilomenaPostExtractor,
    "#results"     : "https://derpicdn.net/img/view/2024/4/1/3334658.svg",
    "#sha1_content": "eec5adf02e2a4fe83b9211c0444d57dc03e21f50",

    "extension": "svg",
    "format"   : "svg",
},

{
    "#url"     : "https://derpibooru.org/1",
    "#category": ("philomena", "derpibooru", "post"),
    "#class"   : philomena.PhilomenaPostExtractor,
},

{
    "#url"     : "https://www.derpibooru.org/1",
    "#category": ("philomena", "derpibooru", "post"),
    "#class"   : philomena.PhilomenaPostExtractor,
},

{
    "#url"     : "https://www.derpibooru.org/images/1",
    "#category": ("philomena", "derpibooru", "post"),
    "#class"   : philomena.PhilomenaPostExtractor,
},

{
    "#url"     : "https://derpibooru.org/images/25361",
    "#comment" : "'comments' metadata (gh#9478)",
    "#category": ("philomena", "derpibooru", "post"),
    "#class"   : philomena.PhilomenaPostExtractor,
    "#options" : {"comments": True},
    "#results" : "https://derpicdn.net/img/view/2012/6/29/25361.jpg",

    "date"    : "dt:2012-06-29 16:07:57",
    "id"      : 25361,
    "comments": [
        {
            "author"     : "Cheril1",
            "avatar"     : "https://derpicdn.net/avatars/2024/5/29/aa19802c-1dcc-11ef-99e7-02420a010003.jpg",
            "body"       : "wub",
            "created_at" : "2024-05-29T17:05:47Z",
            "edit_reason": None,
            "edited_at"  : None,
            "id"         : 10921415,
            "image_id"   : 25361,
            "updated_at" : "2024-05-29T17:05:47Z",
            "user_id"    : 697879,
        },
        {
            "author"     : "Johnnybro288",
            "avatar"     : "https://derpicdn.net/avatars/2021/8/9/16284681457095980117977126.gif",
            "body"       : "yes",
            "created_at" : "2023-04-03T15:17:57Z",
            "edit_reason": None,
            "edited_at"  : None,
            "id"         : 10475066,
            "image_id"   : 25361,
            "updated_at" : "2023-04-03T15:17:57Z",
            "user_id"    : 556710,
        },
        {
            "author"     : "Background Pony #2674",
            "avatar"     : "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjUiIGhlaWdodD0iMTI1IiB2aWV3Qm94PSIwIDAgMTI1IDEyNSIgY2xhc3M9ImF2YXRhci1zdmciPjxyZWN0IHdpZHRoPSIxMjUiIGhlaWdodD0iMTI1IiBmaWxsPSIjYzZkZmYyIi8+PHBhdGggZD0iTTE1LjQ1NiAxMDkuMTVDMTIuMDIgOTcuODA1IDYuNDQgOTUuMDM2LS43OTQgOTguODl2MTkuMTAyYzUuMTMtMTAuMDkgMTAuMjYzLTguMjk0IDE1LjM5NS01LjciIGZpbGw9IiM2Q0EzQTUiLz48cGF0aCBkPSJNNzMuMDU0IDI0LjQ2YzI1Ljg4NiAwIDM5LjE0NCAyNi4zOSAyOC45MTYgNDQuOTUgMS4yNjMuMzggNC45MjQgMi4yNzQgMy40MSA0LjgtMS41MTYgMi41MjUtNy41NzcgMTYuMjg4LTI3Ljc4IDE0Ljc3My0xLjAxIDYuNDQtLjMzIDEyLjYxMyAxLjY0MiAyMi44NTQgMS4zOSA3LjIyNC0uNjMyIDE0LjY0OC0uNjMyIDE0LjY0OHMtNDcuNzg1LjIxNi03My43NC0uMTI3Yy0xLjg4My02LjM4NyA4Ljk2NC0yNS43NiAyMC44MzMtMjQuNzQ4IDE1LjY3NCAxLjMzNCAxOS4xOTMgMS42NCAyMS41OTItMi4wMiAyLjQtMy42NjIgMC0yMy4yMzQtMy41MzUtMzAuODEtMy41MzYtNy41NzctNy44My00MC43ODUgMjkuMjk0LTQ0LjMyeiIgZmlsbD0iIzZCODJBMCIvPjxwYXRoIGQ9Ik05Mi43MTUgMzYuMzEzYzguNjM3IDIuNDY1IDEwLjcxMyA0LjQ2NCAyNS4xNyAxNi42MTIuMy01LjY2Ny0xLjUtMTEuMzM0LTUuNTU2LTE3IDMuMjkgMS42NjYgNi4zOSAzLjMzMyA4LjgyIDUtMy41OS01LjkxNy0uNjQtMTEuNTI3LTEzLjQyOC0yMC4xNjUgNC4zIDEuMzg3IDcuNzY0LTEuNzIyIDExLjE3Ny01LjExLTE4LjY3LS4zMzQtMjcuNDctMTkuMjk3LTQ2LjY2IDMuNjUtLjI3NS0zLjA0MiAxLjI0LTYuMDg0IDMuNjI1LTkuMTI1LTYuODEzIDEuMjg1LTExLjc5IDUuNTY2LTE1LjQ5OCAxMi01LjY5OC01LjUwNy0xMy4wODUgMS4wMDMtMTguNDkgMi42NjctNi44OS0xNC42Ni0xNS42MTYtMTAuMTY2LTIxLjE2Ny00LjY2LTkuMjgzIDkuMjEtOC4wOCAyNS44Ny0uMzAzIDQ2LjY0IDIuMTA1IDUuNjIyLTUuNjg0IDQuNzM0LTguNTk3IDIuMjA2bDEuMzUgNy42NDdjLTIuNTQtMi41LTMuNjMtNS44NjYtNC45MTMtOS4xMTctMS42MjggMTMuOTIgMjIuMjA1IDQzLjQ4NiAzMC4zNDctLjkyNiAxLjYgMy4wNzUgNC4wNDQgNS4zMjIgNi4yOCA0LjU4OC0xLjU2Ni04LjgwOCAzLjQ2LTI0LjUxMiA3LjkxNy0yOS4xNzYgNS4zNjgtNC4yOTIgMTYuOS0xMy43OSAyOS4zMy0xMS43NSA0LjAyIDEuMzU4IDcuOTY4IDIuODEzIDEwLjYgNi4wMnoiIGZpbGw9IiM2Q0EzQTUiLz48cGF0aCBkPSJNNDMuMjY3IDEwNy4zMjRzLTYuODI1LTE0LjEzNy03LjY0LTMwLjE2NmMtLjgxNy0xNi4wMy00LjE5Ny0zMS40NjgtMTAuNTUtNDAuNjg4LTYuMzU0LTkuMjItMTMuMjcyLTkuNzMtMTEuOTk3LTMuOTgyIDEuMjc1IDUuNzQ4IDExLjEyMyAzMy4wMTYgMTIuMTI4IDM1Ljk1NEMyMy4wNDIgNjUuNjQ4IDcuMDM4IDQxLjExLS40MyAzNy4yMjJjLTcuNDctMy44ODYtOC45Ni4zNDYtNi44OTIgNS44ODUgMi4wNjggNS41NCAxOC41MDcgMzAuODQ0IDIwLjg4NiAzMy41MDItMi43MzgtMS42ODUtMTIuMjU2LTkuMDM2LTE2Ljk5Ny04Ljk5Ni00Ljc0Mi4wNC00LjkxIDUuMzY2LTIuNjE3IDguNTI2IDIuMjkyIDMuMTYyIDIwLjkxMiAxOS4xNzMgMjUuMTUgMjAuOTQ1LTUuMzUuMjgtMTAuMzg0IDEuOTk2LTkuMTg2IDYuMDA0IDEuMiA0LjAwNiAxMS4zODQgMTQuMDYzIDI4LjUzIDEyLjM3NyAyLjU3Ni0yLjgzNCA0LjgyMy04LjE0MyA0LjgyMy04LjE0M3oiIGZpbGw9IiM2QjgyQTAiLz48cGF0aCBkPSJNNjQuMzQyIDM1LjU3czMuMjgzLTguMDgtNy4zMjQtMTkuMzE4Yy0xLjc2OC0xLjc2OC0zLjAzLTIuMjczLTQuNjcyLS43NTgtMS42NCAxLjUxNS0xNy4wNDYgMTYuMDM2LjI1MyAzOC4yNi41MDQtMi40IDEuMTM1LTkuNTk3IDEuMTM1LTkuNTk3eiIgZmlsbD0iIzZCODJBMCIvPjwvc3ZnPg==",
            "body"       : "WUB WUB WUB.",
            "created_at" : "2014-07-13T20:32:54Z",
            "edit_reason": None,
            "edited_at"  : None,
            "id"         : 2682502,
            "image_id"   : 25361,
            "updated_at" : "2015-08-22T08:12:42Z",
            "user_id"    : None,
        },
        {
            "author"     : "WingbeatPony",
            "avatar"     : "https://derpicdn.net/avatars/2012/6/19/0c43dc4457c0732e1a.jpeg",
            "body"       : "Well now that I've merged your comment with the higher-res duplicate, you know! Isn't that amazing?",
            "created_at" : "2012-07-09T18:05:50Z",
            "edit_reason": None,
            "edited_at"  : None,
            "id"         : 158386,
            "image_id"   : 25361,
            "updated_at" : "2015-08-22T08:12:42Z",
            "user_id"    : 213996,
        },
        {
            "author"     : "Berzerker_Mohawk",
            "avatar"     : "https://derpicdn.net/avatars/2015/06/25/10_15_49_9_tumblr_nq4m0sQKvI1r89jc0o7_250.png",
            "created_at" : "2012-06-19T19:57:21Z",
            "edit_reason": None,
            "edited_at"  : None,
            "id"         : 103104,
            "image_id"   : 25361,
            "updated_at" : "2015-08-22T08:12:42Z",
            "user_id"    : 214095,
            "body"       : """\
Vinyl looks Really good in this one  
I must Know the Artist!\
""",
        },
    ],
},

{
    "#url"     : "https://derpibooru.org/search?q=cute",
    "#category": ("philomena", "derpibooru", "search"),
    "#class"   : philomena.PhilomenaSearchExtractor,
    "#range"   : "40-60",
    "#count"   : 21,
},

{
    "#url"     : "https://derpibooru.org/tags/cute",
    "#category": ("philomena", "derpibooru", "search"),
    "#class"   : philomena.PhilomenaSearchExtractor,
    "#range"   : "40-60",
    "#count"   : 21,
},

{
    "#url"     : "https://derpibooru.org/tags/artist-colon--dash-_-fwslash--fwslash-%255Bkorroki%255D_aternak",
    "#category": ("philomena", "derpibooru", "search"),
    "#class"   : philomena.PhilomenaSearchExtractor,
    "#count"   : ">= 2",
},

{
    "#url"     : "https://derpibooru.org/galleries/1",
    "#category": ("philomena", "derpibooru", "gallery"),
    "#class"   : philomena.PhilomenaGalleryExtractor,
    "#pattern" : r"https://derpicdn\.net/img/view/\d+/\d+/\d+/\d+[^/]+$",

    "gallery": {
        "description"    : "Indexes start at 1 :P",
        "id"             : 1,
        "spoiler_warning": "",
        "thumbnail_id"   : 1,
        "title"          : "The Very First Gallery",
        "user"           : "DeliciousBlackInk",
        "user_id"        : 365446,
    },
},

)
