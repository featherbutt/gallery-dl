# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import blogger


__tests__ = (
{
    "#url"     : "https://julianbphotography.blogspot.com/2010/12/moon-rise.html",
    "#category": ("blogger", "blogspot", "post"),
    "#class"   : blogger.BloggerPostExtractor,
    "#results" : "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjH9WkPvLJq2moxKtyt3ieJZWSDFQwOi3PHRdlHVHEQHRwy-d86Jg6HWSMhxaa6EgvlXq-zDMmKM4kIPn27eJ9Hepk2X9e9HQhqwMfrT8RYTnFe65uexw7KSk5FdWHxRVp5crz3p_qph3Bj/s0/Icy-Moonrise---For-Web.jpg",

    "blog": {
        "date"       : "dt:2010-11-21 18:19:42",
        "description": "",
        "id"         : "5623928067739466034",
        "kind"       : "blogger#blog",
        "locale"     : dict,
        "name"       : "Julian Bunker Photography",
        "pages"      : int,
        "posts"      : int,
        "published"  : "2010-11-21T10:19:42-08:00",
        "updated"    : str,
        "url"        : "http://julianbphotography.blogspot.com/",
    },
    "post": {
        "author"   : "Julian Bunker",
        "content"  : str,
        "date"     : "dt:2010-12-26 01:08:00",
        "etag"     : str,
        "id"       : "6955139236418998998",
        "kind"     : "blogger#post",
        "published": "2010-12-25T17:08:00-08:00",
        "replies"  : "0",
        "title"    : "Moon Rise",
        "updated"  : "2011-12-06T05:21:24-08:00",
        "url"      : "http://julianbphotography.blogspot.com/2010/12/moon-rise.html",
    },
    "extension": "jpg",
    "filename" : "Icy-Moonrise---For-Web",
    "num"      : 1,
    "url"      : "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjH9WkPvLJq2moxKtyt3ieJZWSDFQwOi3PHRdlHVHEQHRwy-d86Jg6HWSMhxaa6EgvlXq-zDMmKM4kIPn27eJ9Hepk2X9e9HQhqwMfrT8RYTnFe65uexw7KSk5FdWHxRVp5crz3p_qph3Bj/s0/Icy-Moonrise---For-Web.jpg",
},

{
    "#url"     : "https://hotgrannysomas.blogspot.com/2012/08/para-amantes-del-buen-sexo-anal-los.html",
    "#comment" : "video",
    "#category": ("blogger", "blogspot", "post"),
    "#class"   : blogger.BloggerPostExtractor,
    "#pattern" : r"https://.+\.googlevideo\.com/videoplayback",
},

{
    "#url"     : "https://randomthingsthroughmyletterbox.blogspot.com/2022/01/bitter-flowers-by-gunnar-staalesen-blog.html",
    "#comment" : "new image domain (#2204)",
    "#category": ("blogger", "blogspot", "post"),
    "#class"   : blogger.BloggerPostExtractor,
    "#pattern" : r"https://blogger\.googleusercontent\.com/img/.+=s0$",
    "#count"   : 8,
},

{
    "#url"     : "https://lejean.blogspot.com/2009/08/my-workflow.html",
    "#comment" : "video (gh#9487)",
    "#category": ("blogger", "blogspot", "post"),
    "#class"   : blogger.BloggerPostExtractor,
    "#pattern" : (
        r"https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWSVrXVeJ3Ro03C5hefLD2LxomAmtePXOc-b0tgtXaQoDLLtma5z47KLlt0C_ffik8IQdTENLu7RB7qJSLtdbwVF8t-KVTgFu0rWU-3UZyCg01wdBB3QQK7fELi5m67FHXLTVHY5yu9CvG/s0/jequ.jpg",
        r"https://[^/?#]+\.googlevideo\.com/videoplayback\?expire=\d+&.+&itag=22&.+",
    ),

    "blog"     : {
        "date"       : "dt:2008-02-09 17:00:11",
        "description": "",
        "id"         : "8155490718269393715",
        "name"       : "rLéJean's Daily Sketch Grind",
        "published"  : "2008-02-10T02:00:11+09:00",
        "updated"    : "2024-11-01T21:01:52+09:00",
        "url"        : "https://lejean.blogspot.com/",
        "locale"     : {
            "country" : "US",
            "language": "en",
            "variant" : "",
        },
    },
    "post"     : {
        "author"   : "rLéJean",
        "content"  : str,
        "date"     : "dt:2009-08-30 10:25:00",
        "id"       : "5067046835459217828",
        "published": "2009-08-30T19:25:00+09:00",
        "title"    : "My workflow",
        "updated"  : "2011-01-06T13:34:01+09:00",
        "url"      : "https://lejean.blogspot.com/2009/08/my-workflow.html",
        "labels"   : [
            "fashion",
            "tutorial",
        ],
    },
},

{
    "#url"     : "https://julianbphotography.blogspot.com/",
    "#category": ("blogger", "blogspot", "blog"),
    "#class"   : blogger.BloggerBlogExtractor,
    "#pattern" : r"https://blogger\.googleusercontent\.com/img/.+/s0/",
    "#range"   : "1-25",
    "#count"   : 25,
},

{
    "#url"     : "https://julianbphotography.blogspot.com/search?q=400mm",
    "#category": ("blogger", "blogspot", "search"),
    "#class"   : blogger.BloggerSearchExtractor,
    "#count"   : "< 10",

    "query": "400mm",
},

{
    "#url"     : "https://dmmagazine.blogspot.com/search/label/D%26D",
    "#category": ("blogger", "blogspot", "label"),
    "#class"   : blogger.BloggerLabelExtractor,
    "#range"   : "1-25",
    "#count"   : 25,

    "label": "D&D",
},

)
