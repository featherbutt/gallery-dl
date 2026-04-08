# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import tcbscans


__tests__ = (
{
    "#url"     : "https://tcbonepiecechapters.com/chapters/4708/chainsaw-man-chapter-108",
    "#category": ("", "tcbscans", "chapter"),
    "#class"   : tcbscans.TcbscansChapterExtractor,
    "#pattern" : r"https://cdn\.[^/]+/(file|attachments/[^/]+)/[^/]+/[^.]+\.\w+",
    "#count"   : 17,

    "manga"        : "Chainsaw Man",
    "chapter"      : 108,
    "chapter_minor": "",
    "lang"         : "en",
    "language"     : "English",
},

{
    "#url"     : "https://tcbonepiecechapters.com/chapters/7719/jujutsu-kaisen-chapter-258",
    "#category": ("", "tcbscans", "chapter"),
    "#class"   : tcbscans.TcbscansChapterExtractor,
    "#pattern" : r"https://cdn\.[^/]+/(file|attachments/[^/]+)/[^/]+/[^.]+\.\w+",
    "#count"   : 15,

    "manga"        : "Jujutsu Kaisen",
    "chapter"      : 258,
    "chapter_minor": "",
    "lang"         : "en",
    "language"     : "English",
},

{
    "#url"     : "https://tcbonepiecechapters.com/mangas/13/chainsaw-man",
    "#category": ("", "tcbscans", "manga"),
    "#class"   : tcbscans.TcbscansMangaExtractor,
    "#pattern" : tcbscans.TcbscansChapterExtractor.pattern,
    "#range"   : "1-50",
    "#count"   : 50,
},

{
    "#url"     : "https://onepiecechapters.com/mangas/15/hunter-x-hunter",
    "#class"   : tcbscans.TcbscansMangaExtractor,
},

{
    "#url"     : "https://tcbscans.com/mangas/4/jujutsu-kaisen",
    "#class"   : tcbscans.TcbscansMangaExtractor,
},

{
    "#url"     : "https://tcbscans.me/chapters/7975/one-piece-chapter-1179",
    "#class"   : tcbscans.TcbscansChapterExtractor,
},

{
    "#url"     : "https://tcb-backup.bihar-mirchi.com/chapters/7719/jujutsu-kaisen-chapter-258",
    "#class"   : tcbscans.TcbscansChapterExtractor,
},

)
