# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import harvardlawnuremberg


__tests__ = (
{
    "#url"     : "https://nuremberg.law.harvard.edu/documents/450043-tribunal-order-concerning-a-medical?mode=image",
    "#category": ("", "harvardlawnuremberg", "document"),
    "#class"   : harvardlawnuremberg.HarvardlawnurembergDocumentExtractor,
    # 'sfo2' is the region where HLS hosts the bucket, not user-specific CDN (everyone gets same URL)
    "#pattern" : r"https://sfo2\.digitaloceanspaces\.com/harvard-law-library-nuremberg-documents/NRMB-[\w-]+\.jpg",
    "#count"   : 8,

    "count"      : 8,
    "num"        : range(1, 8),
    "document_id": "450043",
    "slug"       : "tribunal-order-concerning-a-medical",
    "title"      : "Tribunal order concerning a medical evaluation of Rudolf Hess's mental health and capacity to stand trial, reports by the doctors who examined Hess, and notice of a hearing for prosecution and defense to present arguments on the issue",
    "extension"  : "jpg",
},

{
    "#url"     : "https://nuremberg.law.harvard.edu/documents/453459-decree-on-the-duties",
    "#class"   : harvardlawnuremberg.HarvardlawnurembergDocumentExtractor,
    "#pattern" : r"https://sfo2\.digitaloceanspaces\.com/harvard-law-library-nuremberg-documents/NRMB-[\w-]+\.jpg",
    "#count"   : 2,

    "count"      : 2,
    "document_id": "453459",
    "slug"       : "decree-on-the-duties",
    "extension"  : "jpg",
},

)
