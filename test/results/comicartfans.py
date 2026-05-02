# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import comicartfans


__tests__ = (
{
    "#url"     : "https://www.comicartfans.com/gallerypiece.asp?piece=2076707",
    "#class"   : comicartfans.ComicartfansArtworkExtractor,
    "#results" : "https://cafansdet.b-cdn.net/images/Category_167080/subcat_215710/0_6k9vzX_241024090851.jpg",

    "art_type"     : "Interior Page",
    "comments"     : int,
    "count"        : 1,
    "date"         : "dt:2024-12-11 00:00:00",
    "description"  : "Original piece for sale - A3<br /><br><br>*shipping and bank fees not included.",
    "extension"    : "jpg",
    "file_url"     : "https://cafansdet.b-cdn.net/images/Category_167080/subcat_215710/0_6k9vzX_241024090851.jpg",
    "filename"     : "0_6k9vzX_241024090851",
    "id"           : 2076707,
    "likes"        : int,
    "location"     : "Eduardo Risso original art",
    "media_type"   : "Pen and Ink",
    "num"          : 0,
    "owner"        : "Nicolás Risso - NRissoart",
    "owner_country": "Argentina",
    "owner_date"   : "dt:2021-03-01 00:00:00",
    "owner_id"     : 167080,
    "owner_website": "http://www.nrissoart.com",
    "sale_status"  : "1900",
    "title"        : """Batman "the last halloween" page 24""",
    "views"        : range(400, 90_000),
    "artist"       : [
        "Eduardo  Risso",
        "Jeph Loeb",
    ],
},

{
    "#url"     : "https://www.comicartfans.com/GalleryPiece.asp?Piece=1875354&GSub=216548",
    "#class"   : comicartfans.ComicartfansArtworkExtractor,
    "#results" : (
        "https://cafansdet.b-cdn.net/images/Category_125715/subcat_216548/edurUsbo_0412221119121gpadd.JPEG",
        "https://cafansdet.b-cdn.net/images/Category_125715/subcat_216548/GY3vCHuo_1012221130231gpaiadd.jpg",
    ),

    "art_type"     : "Cover",
    "artist"       : ["Mark Brooks"],
    "comments"     : range(10, 900),
    "count"        : 2,
    "date"         : "dt:2022-12-04 00:00:00",
    "description"  : "A stunning painting of Psylocke set in feudal Japan from Peach Momoko's Demon Days story.  This piece is so vibrant and a sight to behold - love this reinterpretation of Psylocke and her bright outfit colors go so well with the snow and cherry blossoms of the background.  There's a nice callback to her psychic blade colors with the arc of her katana in the foreground that ties it further to her character.  Can't believe that Mark painted this in 3 days.  <br><br>A big thanks to Alberto for letting me add this to my collection!",
    "extension"    : {"jpg", "jpeg"},
    "file_url"     : r"re:https://cafansdet.b-cdn.net/images/Category_125715/subcat_216548/.+",
    "filename"     : {"edurUsbo_0412221119121gpadd", "GY3vCHuo_1012221130231gpaiadd"},
    "id"           : 1875354,
    "likes"        : range(20, 900),
    "location"     : "Marvel Covers",
    "media_type"   : "Paint - Acrylic",
    "num"          : {1, 2},
    "owner"        : "Pat L",
    "owner_country": "United states",
    "owner_date"   : "dt:2017-12-01 00:00:00",
    "owner_id"     : 125715,
    "owner_website": "",
    "sale_status"  : "NFS",
    "title"        : {"Demon Days: X-men 1 Cover", "Trade Dress"},
    "views"        : range(900, 90_000),
},

{
    "#url"     : "https://www.comicartfans.com/gallerydetail.asp?gcat=26857",
    "#class"   : comicartfans.ComicartfansGalleryExtractor,
    "#pattern" : comicartfans.ComicartfansArtworkExtractor.pattern,
    "#count"   : 122,
},

{
    "#url"     : "https://www.comicartfans.com/gallerydetail.asp?gcat=194018",
    "#comment" : "only 1 page of results",
    "#class"   : comicartfans.ComicartfansGalleryExtractor,
    "#results" : "https://www.comicartfans.com/gallerypiece.asp?piece=2063407",
},

{
    "#url"     : "https://www.comicartfans.com/gallerydetailsearch.asp?order=Date&gcat=194018",
    "#class"   : comicartfans.ComicartfansGalleryExtractor,
    "#results" : "https://www.comicartfans.com/gallerypiece.asp?piece=2063407",
},

{
    "#url"     : "https://www.comicartfans.com/comic-artists/Gabriele_Dell'Otto.asp",
    "#class"   : comicartfans.ComicartfansArtistExtractor,
    "#pattern" : comicartfans.ComicartfansArtworkExtractor.pattern,
    "#range"   : "1-100",
    "#count"   : 100,

    "search_tags": "Gabriele Dell'Otto",
},

{
    "#url"     : "https://www.comicartfans.com/searchresult.asp?txtsearch=Jim%20Lee",
    "#class"   : comicartfans.ComicartfansSearchExtractor,
    "#pattern" : comicartfans.ComicartfansArtworkExtractor.pattern,
    "#range"   : "1-100",
    "#count"   : 100,

    "search_tags": "Jim Lee",
},

)
