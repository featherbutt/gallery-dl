# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import telegraph


__tests__ = (
{
    "#url"     : "https://telegra.ph/Telegraph-Test-03-28",
    "#class"   : telegraph.TelegraphGalleryExtractor,
    "#results" : (
        "https://telegra.ph/file/971bc733bc36e0afbebc9.png",
        "https://telegra.ph/file/c6a424b5a57304b8d03ff.png",
    ),

    "author"       : "mikf",
    "caption"      : {"test", ""},
    "count"        : 2,
    "date"         : "dt:2022-03-28 16:01:36",
    "description"  : "Just a test",
    "extension"    : "png",
    "filename"     : str,
    "html"         : """<h1>Telegra.ph Test<br></h1><address>mikf<br></address><p>Just a test</p><figure><img src="/file/971bc733bc36e0afbebc9.png"><figcaption>test</figcaption></figure><p>テストです</p><figure><img src="/file/c6a424b5a57304b8d03ff.png"><figcaption></figcaption></figure><figure><iframe src="/embed/youtube?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DBaW_jenozKc%26t%3D1s%26end%3D9" width="640" height="360" frameborder="0" allowtransparency="true" allowfullscreen="true" scrolling="no"></iframe><figcaption>テスト</figcaption></figure><p><br></p><p><br></p>""",
    "links"        : [],
    "num"          : {1, 2},
    "num_formatted": {"1", "2"},
    "post_url"     : "https://telegra.ph/Telegraph-Test-03-28",
    "slug"         : "Telegraph-Test-03-28",
    "title"        : "Telegra.ph Test",
    "url"          : r"re:https://telegra.ph/file/\w+.png",
},

{
    "#url"     : "https://telegra.ph/森-03-28",
    "#class"   : telegraph.TelegraphGalleryExtractor,
    "#pattern" : "https://telegra.ph/file/3ea79d23b0dd0889f215a.jpg",
    "#count"   : 1,

    "author"       : "&",
    "caption"      : "kokiri",
    "count"        : 1,
    "date"         : "dt:2022-03-28 16:31:26",
    "description"  : "コキリの森",
    "extension"    : "jpg",
    "filename"     : "3ea79d23b0dd0889f215a",
    "num"          : 1,
    "num_formatted": "1",
    "post_url"     : "https://telegra.ph/森-03-28",
    "slug"         : "森-03-28",
    "title"        : "\"森\"",
    "url"          : "https://telegra.ph/file/3ea79d23b0dd0889f215a.jpg",
},

{
    "#url"     : "https://telegra.ph/Vsyo-o-druzyah-moej-sestricy-05-27",
    "#class"   : telegraph.TelegraphGalleryExtractor,
    "#pattern" : r"^https://pith1\.ru/uploads/posts/2019-12/\d+_\d+\.jpg$",
    "#sha1_url": "c1f3048e5d94bee53af30a8c27f70b0d3b15438e",

    "author"       : "Shotacon - заходи сюда",
    "caption"      : "",
    "count"        : 19,
    "date"         : "dt:2022-05-27 16:17:27",
    "description"  : "",
    "num_formatted": r"re:^\d{2}$",
    "post_url"     : "https://telegra.ph/Vsyo-o-druzyah-moej-sestricy-05-27",
    "slug"         : "Vsyo-o-druzyah-moej-sestricy-05-27",
    "title"        : "Всё о друзьях моей сестрицы",
},

{
    "#url"     : "https://telegra.ph/Disharmonica---Saber-Nero-02-21",
    "#class"   : telegraph.TelegraphGalleryExtractor,
    "#pattern" : r"https://telegra\.ph/file/[0-9a-f]+\.(jpg|png)",

    "author"       : "cosmos",
    "caption"      : "",
    "count"        : 89,
    "date"         : "dt:2022-02-21 05:57:39",
    "description"  : "",
    "num_formatted": r"re:^\d{2}$",
    "post_url"     : "https://telegra.ph/Disharmonica---Saber-Nero-02-21",
    "slug"         : "Disharmonica---Saber-Nero-02-21",
    "title"        : "Disharmonica - Saber Nero",
},

{
    "#url"     : "https://telegra.ph/lumosup-06-23",
    "#class"   : telegraph.TelegraphGalleryExtractor,
    "#pattern" : r"https://telegra\.ph/file/\w+\.(jpg|png)",
    "#count"   : 30,

    "author"       : "Webcam Патруль",
    "caption"      : "",
    "count"        : 30,
    "date"         : "dt:2023-06-23 16:10:12",
    "extension"    : {"jpg", "png"},
    "filename"     : str,
    "html"         : """<h1>lumosup<br></h1><address><a href="https://t.me/+L3UKIb3pAIY0Yzcy" target="_blank">Webcam Патруль</a><br></address><figure><img src="/file/94bcfab269efb7e4d387d.jpg"><figcaption></figcaption></figure><p>Индира с города Алматы если вам есть что дополнить о ней напишите Админу анонимность гарантируем</p><p>её <a href="https://www.instagram.com/indirakhanim/" target="_blank">Instagram</a></p><p>её <a href="https://www.tiktok.com/@indirakhanim?_t=8dUd077R5JR&amp;_r=1" target="_blank">TikTok</a></p><figure><img src="/file/5c3adee3109269f6c6e3a.png"><figcaption></figcaption></figure><figure><img src="/file/101a070b7c5af0bf68de0.png"><figcaption></figcaption></figure><figure><img src="/file/03d32a80a0f2b4d8fa6bd.png"><figcaption></figcaption></figure><figure><img src="/file/34293c69df000e4acd687.png"><figcaption></figcaption></figure><p><br></p><figure><img src="/file/705f4760da4e0a0138536.jpg"><figcaption></figcaption></figure><figure><img src="/file/255bc66961b29e8c363b9.jpg"><figcaption></figcaption></figure><figure><img src="/file/cb2fe36a737adac142c85.jpg"><figcaption></figcaption></figure><figure><img src="/file/2ba135e2eb23d35b91369.jpg"><figcaption></figcaption></figure><figure><img src="/file/da9dd0f484b08c2fe2c31.jpg"><figcaption></figcaption></figure><figure><img src="/file/31e2d0d9397a98dce1410.jpg"><figcaption></figcaption></figure><figure><img src="/file/86d996fc47ab083ced74f.jpg"><figcaption></figcaption></figure><figure><img src="/file/218945117a531f88ccfcb.jpg"><figcaption></figcaption></figure><figure><img src="/file/11284090543afcc80888e.jpg"><figcaption></figcaption></figure><figure><img src="/file/fde96da95d232c8391bf8.jpg"><figcaption></figcaption></figure><figure><img src="/file/5291ba35c303313cb20f0.jpg"><figcaption></figcaption></figure><figure><img src="/file/77d04a58535115ea3b7bc.jpg"><figcaption></figcaption></figure><figure><img src="/file/16e8ac4a8eefe6a8309a2.jpg"><figcaption></figcaption></figure><figure><img src="/file/0ed695cab83105d06a7a5.jpg"><figcaption></figcaption></figure><figure><img src="/file/ca5d0cf6565ee185ce0dc.jpg"><figcaption></figcaption></figure><figure><img src="/file/c02dd7c1a2e74e4e5d863.jpg"><figcaption></figcaption></figure><figure><img src="/file/bfa76da71de870de5e0c5.jpg"><figcaption></figcaption></figure><figure><img src="/file/1a03ce6132ea88b63b57b.jpg"><figcaption></figcaption></figure><figure><img src="/file/f43a1a8bdac9eb747be52.jpg"><figcaption></figcaption></figure><figure><img src="/file/0a84cfd1600a1fcdbbfd8.jpg"><figcaption></figcaption></figure><figure><img src="/file/c7f78d779d7c702461711.jpg"><figcaption></figcaption></figure><figure><img src="/file/3c4c5283a72dfd4bd7cb9.jpg"><figcaption></figcaption></figure><figure><img src="/file/b48da0d310b6d08fe69fb.jpg"><figcaption></figcaption></figure><figure><img src="/file/ba2f20f7691403db86ade.jpg"><figcaption></figcaption></figure><figure><img src="/file/6dc2660876fb0ed3cf6d5.jpg"><figcaption></figcaption></figure><p><br></p>""",
    "num"          : range(1, 30),
    "num_formatted": r"re:^[0123]\d$",
    "post_url"     : "https://telegra.ph/lumosup-06-23",
    "slug"         : "lumosup-06-23",
    "title"        : "lumosup",
    "url"          : r"re:https://telegra.ph/file/\w+.(jpg|png)",
    "description"  : """\
Индира с города Алматы если вам есть что дополнить о ней напишите Админу анонимность гарантируем
её Instagram
её TikTok\
""",
    "links"        : [
        "https://t.me/+L3UKIb3pAIY0Yzcy",
        "https://www.instagram.com/indirakhanim/",
        "https://www.tiktok.com/@indirakhanim?_t=8dUd077R5JR&amp;_r=1",
    ],
},

)
