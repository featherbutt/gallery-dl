# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import cosplayrule34


__tests__ = (
{
    "#url"     : "https://cosplayrule34.com/post/101851",
    "#class"   : cosplayrule34.Cosplayrule34PostExtractor,
    "#pattern" : r"https://cosplayrule34\.com/images/a/1280/\-10000001/10014597/\d+\.webp",
    "#count"   : 21,

    "album_id"   : "10014597",
    "cosplay"    : ["Shadowheart"],
    "count"      : 21,
    "num"        : range(1, 21),
    "counter"    : int,
    "description": "Experience the enchanting allure of Atina, as we present 21 leaked photos of this captivating model. Delve into the world of sensuality and beauty as you explore these exclusive images, obtained from Onlyfans, Patreon, and Fansly.",
    "download"   : int,
    "download_id": 0,
    "extension"  : "webp",
    "fandom"     : ["Baldurs Gate"],
    "id"         : 101851,
    "model"      : ["Atina"],
    "owner_id"   : "-10000001",
    "title"      : "Atina - Shadowheart - Baldurs Gate",
    "tags"       : [
        "Atina",
        "Shadowheart",
        "Baldurs Gate",
    ],
},

{
    "#url"     : "https://cosplayrule34.com/post/89135",
    "#class"   : cosplayrule34.Cosplayrule34PostExtractor,
    "#pattern" : r"https://cosplayrule34\.com/images/a/1280/\-10000001/10004553/\d+\.webp",
    "#count"   : 29,

    "album_id"   : "10004553",
    "cosplay"    : ["Illustrious"],
    "count"      : 29,
    "counter"    : 3,
    "description": "Experience the enchanting allure of Cosplaytales, as we present 29 leaked photos of this captivating model. Delve into the world of sensuality and beauty as you explore these exclusive images, obtained from Onlyfans, Patreon, and Fansly.",
    "download"   : 1,
    "download_id": 0,
    "extension"  : "webp",
    "fandom"     : ["Azur Lane"],
    "id"         : 89135,
    "model"      : ["Cosplaytales"],
    "owner_id"   : "-10000001",
    "title"      : "COSPLAYTALES - Illustrious",
    "tags"       : [
        "Cosplaytales",
        "Illustrious",
        "Azur Lane",
    ],
},

{
    "#url"     : "https://cosplayrule34.com/model/Cosplaytales",
    "#category": ("", "cosplayrule34", "model"),
    "#class"   : cosplayrule34.Cosplayrule34ListingExtractor,
    "#results" : (
        "https://cosplayrule34.com/post/101915",
        "https://cosplayrule34.com/post/101866",
        "https://cosplayrule34.com/post/89135",
    ),
},

{
    "#url"     : "https://cosplayrule34.com/cosplay/Illustrious",
    "#category": ("", "cosplayrule34", "cosplay"),
    "#class"   : cosplayrule34.Cosplayrule34ListingExtractor,
    "#results" : (
        "https://cosplayrule34.com/post/92725",
        "https://cosplayrule34.com/post/89135",
        "https://cosplayrule34.com/post/84354",
        "https://cosplayrule34.com/post/84074",
    ),
},

{
    "#url"     : "https://cosplayrule34.com/fandom/Azur-Lane",
    "#category": ("", "cosplayrule34", "fandom"),
    "#class"   : cosplayrule34.Cosplayrule34ListingExtractor,
    "#pattern" : cosplayrule34.Cosplayrule34PostExtractor.pattern,
    "#range"   : "1-30",
    "#count"   : 30,
},

{
    "#url"     : "https://cosplayrule34.com/category/cosplay",
    "#category": ("", "cosplayrule34", "category"),
    "#class"   : cosplayrule34.Cosplayrule34ListingExtractor,
    "#pattern" : cosplayrule34.Cosplayrule34PostExtractor.pattern,
    "#range"   : "1-30",
    "#count"   : 30,
},

{
    "#url"     : "https://cosplayrule34.com/search/azur",
    "#category": ("", "cosplayrule34", "search"),
    "#class"   : cosplayrule34.Cosplayrule34ListingExtractor,
    "#pattern" : cosplayrule34.Cosplayrule34PostExtractor.pattern,
    "#range"   : "1-30",
    "#count"   : 30,
},

{
    "#url"     : "https://cosplayrule34.com/top",
    "#class"   : cosplayrule34.Cosplayrule34TopExtractor,
    "#pattern" : cosplayrule34.Cosplayrule34PostExtractor.pattern,
    "#range"   : "1-20",
    "#count"   : 20,
},

{
    "#url"     : "https://cosplayrule34.com/",
    "#class"   : cosplayrule34.Cosplayrule34PostsExtractor,
    "#pattern" : cosplayrule34.Cosplayrule34PostExtractor.pattern,
    "#range"   : "1-20",
    "#count"   : 20,
},

)
