# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import framedsc


__tests__ = (
    {
        "#url"     : "https://cdn.framedsc.com/images/1770839864.63_44.png",
        "#category": ("", "framedsc", "raw"),
        "#class"   : framedsc.FramedscRawExtractor,
        "#count"   : 1,
        "#results" : "https://cdn.framedsc.com/images/1770839864.63_44.png"
    },
    {
        "#url"     : "https://framedsc.com/HallOfFramed/?imageId=1771252719",
        "#category": ("", "framedsc", "image"),
        "#class"   : framedsc.FramedscImageExtractor,
        "#count"   : 1,
        "#results" : "https://cdn.framedsc.com/images/1770839864.63_44.png",
    },
    {
        "#url"     : "https://framedsc.com/HallOfFramed/?author=Flurdy&before=2026-04-27",
        "#category": ("", "framedsc", "search"),
        "#class"   : framedsc.FramedscSearchExtractor,
        "#count"   : 6,
        "#results": ("https://cdn.framedsc.com/images/1590578979_NMS_2020_05_25_13_34_11_393-g.png",
                     "https://cdn.framedsc.com/images/1590578987_NMS_2020_05_26_13_38_52_15.png",
                     "https://cdn.framedsc.com/images/1620912616_AbzuGame-Win64-Shipping_2021_05_11_13_13_40_897.png",
                     "https://cdn.framedsc.com/images/1635862091_hl2ep1_2021_10_31_18_25_06_084-gp.png",
                     "https://cdn.framedsc.com/images/1636057094_hl2ep1_2021_10_31_19_56_50_595-gp.png",
                     "https://cdn.framedsc.com/images/1676764490_Dead_Space_2023-02-06_23-48-53.png")
    },
    {
        "#url"     : "https://framedsc.com/HallOfFramed/?title=ADR1FT&before=2026-04-27",
        "#category": ("", "framedsc", "search"),
        "#class"   : framedsc.FramedscSearchExtractor,
        "#count"   : 5,
        "#results": ("https://cdn.framedsc.com/images/1623421152_ADR1FT-Win64-Shipping_2021_06_09_11_58_27_011.png",
                     "https://cdn.framedsc.com/images/1624727132_ADR1FT-Win64-Shipping_2021_06_23_11_41_21_342.png",
                     "https://cdn.framedsc.com/images/1624828941_ADR1FT-Win64-Shipping_2021_06_23_12_15_52_588.png",
                     "https://cdn.framedsc.com/images/1624887917_ADR1FT-Win64-Shipping_2021_06_23_12_50_06_488.png",
                     "https://cdn.framedsc.com/images/1625867648_ADR1FT-Win64-Shipping_2021_07_08_11_46_54_438.png")
    },
    {
        "#url"     : "https://framedsc.com/HallOfFramed/?color=lawngreen&before=2026-04-27",
        "#category": ("", "framedsc", "search"),
        "#class"   : framedsc.FramedscSearchExtractor,
        "#count"   : 1,
        "#results": "https://cdn.framedsc.com/images/1632333696_MirrorsEdgeCatalyst_2021-09-15_22-36-35.png"
    }
)
