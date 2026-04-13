# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import xenforo


__tests__ = (
{
    "#url"     : "https://thefappeningblog.com/forum/threads/tecia-torres.89967/post-804808",
    "#category": ("xenforo", "thefappeningforum", "post"),
    "#class"   : xenforo.XenforoPostExtractor,
    "#results" : "https://thefappeningblog.com/forum/attachments/tecia-torres-mp4.1888997/",

    "count"       : 1,
    "extension"   : "mp4",
    "filename"    : "tecia-torres",
    "id"          : 1888997,
    "num"         : 1,
    "num_external": 0,
    "num_internal": 1,
    "type"        : "inline",
    "post"        : {
        "attachments": "",
        "author"     : "Party McFly",
        "author_id"  : "566042",
        "author_slug": "party-mcfly",
        "author_url" : "/forum/members/party-mcfly.566042/",
        "content"    : """<div class="bbWrapper"><a href="https://thefappeningblog.com/forum/attachments/tecia-torres-mp4.1888997/" target="_blank">View attachment Tecia Torres.mp4</a></div>""",
        "count"      : 1,
        "date"       : "dt:2023-04-26 04:57:36",
        "id"         : "804808",
    },
    "thread"      : {
        "author"     : "Party McFly",
        "author_id"  : "",
        "author_slug": "party-mcfly",
        "author_url" : "",
        "date"       : "dt:2023-04-26 04:54:13",
        "id"         : "89967",
        "posts"      : 3,
        "section"    : "Celebrity Sexy Photos",
        "tags"       : (),
        "title"      : "Tecia Torres",
        "url"        : "https://thefappeningblog.com/forum/threads/tecia-torres.89967/",
        "views"      : -1,
        "path"       : [
            "Home",
            "Forums",
            "Leaked, Nude and Sexy Photos and Videos",
            "Celebrity Sexy Photos",
        ],
    },
},

{
    "#url"     : "https://thefappeningblog.com/forum/threads/tecia-torres.89967/",
    "#category": ("xenforo", "thefappeningforum", "thread"),
    "#class"   : xenforo.XenforoThreadExtractor,
    "#count"   : 14,

    "post"        : dict,
    "thread"      : {
        "author"     : "Party McFly",
        "author_id"  : "",
        "author_slug": "party-mcfly",
        "author_url" : "",
        "date"       : "dt:2023-04-26 04:54:13",
        "id"         : "89967",
        "posts"      : 3,
        "section"    : "Celebrity Sexy Photos",
        "tags"       : (),
        "title"      : "Tecia Torres",
        "url"        : "https://thefappeningblog.com/forum/threads/tecia-torres.89967/",
        "views"      : -1,
        "path"       : [
            "Home",
            "Forums",
            "Leaked, Nude and Sexy Photos and Videos",
            "Celebrity Sexy Photos",
        ],
    },
},

{
    "#url"     : "https://thefappeningblog.com/forum/forums/celebrity-sexy-photos/",
    "#category": ("xenforo", "thefappeningforum", "forum"),
    "#class"   : xenforo.XenforoForumExtractor,
    "#pattern" : xenforo.XenforoThreadExtractor.pattern,
    "#range"   : "1-50",
    "#count"   : 50,
},

)
