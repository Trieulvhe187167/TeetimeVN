# -*- coding: utf-8 -*-
"""
seed_extra_10_vn_courses.py
---------------------------
向 teetimevn_dev.db 增补 10 个越南高尔夫球场示例数据，添加多语言支持（简体、中繁、英、越、日、韩），
并将 Google Maps 给出的 <iframe> embed 代码存入 maps_url 字段，每条记录新增 overview_en 英文简介。
"""

import sqlite3
from pathlib import Path
from datetime import date

DB_PATH = Path("data/teetimevn_dev.db")
TODAY   = date.today().isoformat()

# ────────────────────────────────────────────────
# 1. 统一示例价格 & 当天汇率
# ────────────────────────────────────────────────
PRICES = [
    ("weekday", 2400000, 2150000, "-10%"),
    ("weekend", 3000000, 2700000, "-10%"),
    ("twilight", 1800000, 1580000, "-12%"),
]

FX = [
    (TODAY, "USD", 23500),
    (TODAY, "EUR", 26000),
    (TODAY, "JPY", 180),
    (TODAY, "KRW", 19),
    (TODAY, "CNY", 3450),
]

# ────────────────────────────────────────────────
# 2. 示例球场数据（10 条），含 maps (完整 <iframe> 代码) & overview_en
# ────────────────────────────────────────────────
COURSES = [
    {
        "slug": "trang-an-golf-ninh-binh",
        "names": {
            "zh-CN": "	长安高尔夫乡村俱乐部", "zh-TW": "長安高爾夫鄉村俱樂部",
            "en":    "Trang An Golf & Country Club", "vi":    "Tràng An Golf & Country Club",
            "ja":    "チャンアン ゴルフ＆カントリークラブ","ko":   "짱안 골프 앤 컨트리 클럽",
        },
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 18, "par": 72, "length": 7074 , "year": 2016,
        "lat": 20.25667, "lng": 105.89639, "designer": "Golf East",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4236.193406167881!2d105.7894003!3d20.223988999999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x313687809c83da63%3A0xb1c122015ff61743!2zU8OibiBHb2xmIFRyw6BuZyBBbg!5e1!3m2!1svi!2s!4v1747392138151!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },

    {
        "slug": "hoang-gia-royal-golf-course",
        "names": {
            "zh-CN": "	皇家高尔夫球场", "zh-TW": "皇家高爾夫球場",
            "en":    "Royal Golf Course", "vi":    "Sân golf Hoàng Gia – Royal Golf Course",
            "ja":    "ロイヤルゴルフコース","ko":   "로얄 골프 코스",
        },
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 54, "par": 72, "length": 7037 , "year": 2010,
        "lat": 20.16306, "lng": 105.91583, "designer": "Peter Rousseau ",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3538.7954834700745!2d105.96438292796527!3d20.125999680478238!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3136657cc0863b41%3A0x93831baed02a8932!2sS%C3%A2n%20Golf%20Ho%C3%A0ng%20Gia%20-%20Royal%20Golf%20Course!5e1!3m2!1svi!2s!4v1747392820379!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },
    
    {
        "slug": "dragon-golf-links",
        "names": {
            "zh-CN": "	龙高尔夫林克斯球场", "zh-TW": "龍高爾夫林克斯球場",
            "en":    "Dragon Golf Links", "vi":    "Dragon Golf Links",
            "ja":    "ドラゴン・ゴルフ・リンクス","ko":   "드래곤 골프 링크스",
        },
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 27, "par": 72, "length": 10064 , "year": 2023,
        "lat": 21.05851, "lng": 105.47847, "designer": "Greg Norman Golf Course Design",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4223.275463025954!2d106.77098287566156!3d20.693042299223855!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x314a6ddbdf801009%3A0x5485a2c0107ac8db!2sDragon%20Golf%20Links!5e1!3m2!1svi!2s!4v1747393636491!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>"""
    },

        {
        "slug": "vinpearl-golf-hai-phong",
        "names": {
            "zh-CN": "	海防珍珠高尔夫球场", "zh-TW": "海防珍珠高爾夫球場",
            "en":    "	Vinpearl Golf Hai Phong", "vi":    "Sân golf Vinpearl Hải Phòng",
            "ja":    "ビンパール・ゴルフ・ハイフォン","ko":   "빈펄 골프 하이퐁",
        },
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 36, "par": 72, "length": 7318 , "year": 2017,
        "lat": 21.058509714283947, "lng": 105.47847025852653, "designer": "IMG Worldwide",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4218.270829389241!2d106.72568707566506!3d20.872050393141876!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x314a652ce4c9bf89%3A0xa3acc8fd63b55a4!2zVmlucGVhcmwgR29sZiBI4bqjaSBQaMOybmc!5e1!3m2!1svi!2s!4v1747393710977!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },

            {
        "slug": "sono-felice-country-club-hai-phong",
        "names": {
            "zh-CN": "	海防索诺菲利斯乡村俱乐部", "zh-TW": "海防索諾菲利斯鄉村俱樂部",
            "en":    "	Sono Felice Country Club Hai Phong", "vi":    "Sono Felice Country Club Hải Phòng",
            "ja":    "ハイフォン・ソノフェリーチ・カントリークラブ","ko":   "하이퐁 소노펠리체 컨트리 클럽",
        },
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 18, "par": 71, "length":  7123 , "year": 2011,
        "lat": 20.91759, "lng": 106.675034, "designer": "Pacific Coast Design",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4215.796680601651!2d106.67766017566683!3d20.9600071901356!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x314a7cf7ff0c61f9%3A0x4df4bd03740b338d!2sS%C3%A2n%20golf%20Sono%20Felice%20Country%20Club%20H%E1%BA%A3i%20Ph%C3%B2ng!5e1!3m2!1svi!2s!4v1747394090015!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },

    
            {
        "slug": "ruby-tree-golf-resort-hai-phong",
        "names": {
            "zh-CN": "	海防红宝石树高尔夫度假村", "zh-TW": "海防紅寶石樹高爾夫度假村",
            "en":    "	Ruby Tree Golf Resort Hai Phong", "vi":    "Sân golf Ruby Tree Hải Phòng",
            "ja":    "ハイフォン・ルビーツリー・ゴルフリゾート","ko":   "하이퐁 루비 트리 골프 리조트",
        },
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 18, "par": 71, "length":  7123 , "year": 2011,
        "lat": 20.91759, "lng": 106.675034, "designer": "Pacific Coast Design",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4222.191336313437!2d106.77561807566221!3d20.73194519790609!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x314a6e82730340d5%3A0x6bd3445f80d41c6a!2zU8OibiBnb2xmIFJ1YnkgVHJlZSBI4bqjaSBQaMOybmc!5e1!3m2!1svi!2s!4v1747394370152!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },

              {
        "slug": "mong-cai-international-golf",
        "names": {
            "zh-CN": "	芒街国际高尔夫俱乐部", "zh-TW": "芒街國際高爾夫俱樂部",
            "en":    "	Mong Cai International Golf Club", "vi":    "Câu lạc bộ Golf Quốc tế Móng Cái",
            "ja":    "ハイフォン・ルビーツリー・ゴルフリゾート","ko":   "하이퐁 루비 트리 골프 리조트",
        },
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 18, "par": 72, "length":  7204  , "year": 2008,
        "lat": 21.5460, "lng": 108.0410, "designer": "Pacific Coast Design",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1187.347890137407!2d108.05544572266908!3d21.48626965368987!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x314ca9c555555555%3A0x1ed9617c616100c3!2zQ8OCVSBM4bqgQyBC4buYIEdPTEYgUVXhu5BDIFThur4gTcOTTkcgQ8OBSQ!5e1!3m2!1svi!2s!4v1747394680414!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },
            {
        "slug": "amber-hills-golf-resort",
        "names": {
            "zh-CN": "	琥珀山高尔夫度假村", "zh-TW": "琥珀山高爾夫度假村",
            "en":    "	Amber Hills Golf & Resort", "vi":    "Sân Golf Amber Hills",
            "ja":    "アンバー ヒルズ ゴルフ＆リゾート","ko":   "앰버 힐스 골프 & 리조트",
        },
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 36, "par": 72, "length":  7203   , "year": 2017,
        "lat": 21.2667, "lng": 106.2500, "designer": "Albanese & Lutzke",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4208.6011305609!2d106.17945487567196!3d21.213831781395562!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x313572e415727eb9%3A0xc0bcd3112cbb4f85!2sS%C3%A2n%20Golf%20Amber%20Hills!5e1!3m2!1svi!2s!4v1747395243060!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },

                {
        "slug": "stone-highland-golf-resort",
        "names": {
            "zh-CN": "	石高原高尔夫度假村", "zh-TW": "石高原高爾夫度假村",
            "en":    "	Stone Highland Golf & Resort", "vi":    "Sân golf Stone Highland Golf & Resort",
            "ja":    "ストーンハイランド ゴルフ＆リゾート","ko":   "스톤 하이랜드 골프 & 리조트",
        },
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 36, "par": 72, "length":  7105   , "year": 2023,
        "lat": 21.2500, "lng": 106.2500, "designer": "Brian Curley (Schmidt-Curley Design)",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4206.9366141567925!2d106.05793477567326!3d21.272136279374234!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x313511f0cfce769f%3A0x3c9825e02e4672ac!2sS%C3%A2n%20golf%20Stone%20Highland%20Golf%20%26%20Resort!5e1!3m2!1svi!2s!4v1747395441558!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },


    
                {
        "slug": "yen-bai-star-golf-resort",
        "names": {
            "zh-CN": "	延拜星高尔夫度假村", "zh-TW": "延拜星高爾夫度假村",
            "en":    "	Yen Bai Star Golf & Resort", "vi":    "Sân Golf Ngôi Sao Yên Bái",
            "ja":    "イェンバイ・スター・ゴルフ＆リゾート","ko":   "옌바이 스타 골프 & 리조트",
        },
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 27, "par": 72, "length":  7000   , "year": 2024,
        "lat": 21.6500, "lng": 104.9000, "designer": "Peter John Waddell",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4196.0753909672585!2d104.89361867568086!3d21.64890556618962!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31335d99934e7903%3A0xc4d83f766730ebea!2zU8OibiBHb2xmIE5nw7RpIFNhbyBZw6puIELDoWk!5e1!3m2!1svi!2s!4v1747395639811!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },


                    {
        "slug": "sapa-grand-golf-course",
        "names": {
            "zh-CN": "	萨帕大高尔夫球场", "zh-TW": " 薩帕大高爾夫球場",
            "en":    "	Sapa Grand Golf Course", "vi":    "Sân Golf Sapa Grand",
            "ja":    "サパ・グランド・ゴルフコース","ko":   "사파 그랜드 골프 코스",
        },
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 18, "par": 72, "length":  6850    , "year": 2023,
        "lat": 22.356464, "lng": 103.873802, "designer": "IMG",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4169.053702248778!2d103.88596307570042!3d22.560277233421047!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x36cd6d2ee2b1f387%3A0xeaaefbe86a6aa61c!2sS%C3%A2n%20Golf%20Sapa%20Grand%20-%20Sapa%20Grand%20Golf%20Course!5e1!3m2!1svi!2s!4v1747395857494!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },


                        {
        "slug": "corn-hill-golf-resort-luc-nam",
        "names": {
            "zh-CN": "	玉米山高尔夫度假村", "zh-TW": " 玉米山高爾夫渡假村",
            "en":    "	Corn Hill Golf & Resort", "vi":    "Sân golf Đồi Ngô ",
            "ja":    "コーンヒル ゴルフ＆リゾート","ko":   "콘 힐 골프 & 리조트",
        },
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 36 , "par": 74.3, "length":  7185     , "year": 2024,
        "lat": 21.2936, "lng": 106.4936, "designer": "Brett Mogg (Nelson & Haworth)",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d36706.03656950522!2d106.44816732767163!3d21.254236946837167!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x313565765709b011%3A0x7acaf45d18adb18b!2zU8OibiBnb2xmIMSQ4buSSSBOR8OUIC0gQ09STiBISUxMIEdPTEYgJiBSRVNPUlQ!5e1!3m2!1svi!2s!4v1747396040292!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>  
"""
    },
                          {
        "slug": "van-lang-empire-golf-club",
        "names": {
            "zh-CN": "	文郎帝国高尔夫俱乐部", "zh-TW": " 文郎帝國高爾夫俱樂部",
            "en":    "	Van Lang Empire Golf Club", "vi":    "Sân golf Văn Lang Empire ",
            "ja":    "ヴァンラン・エンパイア・ゴルフクラブ","ko":   "반랑 엠파이어 골프 클럽",
        },
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 36 , "par": 72, "length":  2010463.2       , "year": 2024,
        "lat": 21.3050, "lng": 105.2920, "designer": "Greg Norman",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d36706.03656950522!2d106.44816732767163!3d21.254236946837167!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x313565765709b011%3A0x7acaf45d18adb18b!2zU8OibiBnb2xmIMSQ4buSSSBOR8OUIC0gQ09STiBISUxMIEdPTEYgJiBSRVNPUlQ!5e1!3m2!1svi!2s!4v1747396040292!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>  
"""
    },
]

conn = sqlite3.connect(DB_PATH)
cur  = conn.cursor()



for c in COURSES:
    # 删除旧 golf_course
    cur.execute("DELETE FROM golf_course WHERE slug=?", (c["slug"],))

    # 插入主表，maps_url 字段存放完整 <iframe> 代码
    cur.execute("""
        INSERT INTO golf_course
        (slug, holes, par, length_yards, opened_year, lat, lng, maps_url, scorecard_pdf)
        VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        c["slug"], c["holes"], c["par"], c["length"],
        c["year"], c["lat"], c["lng"],
        c["maps"],
        f"/static/media/{c['slug']}_scorecard.pdf"
    ))
    cid = cur.lastrowid

    # 删除旧翻译并插入多语言
    cur.execute("DELETE FROM golf_course_i18n WHERE course_id=?", (cid,))
    i18n_rows = []
    for lang in ["zh-CN","zh-TW","en","vi","ja","ko"]:
        name = c["names"][lang]
        ov_key = "overview" if lang=="zh-CN" else f"overview_{lang.replace('-','_')}"
        overview = c.get(ov_key, "")
        address = {
            "zh-CN":"河内","zh-TW":"河內","en":"Hanoi","vi":"Hà Nội","ja":"ハノイ","ko":"하노이"
        }[lang]
        seo_title = f"{name} | Vietnam Golf" if lang!="zh-CN" else f"{name} - 越南高尔夫"
        fee_note  = {
            "zh-CN":"已含球童球车税费","zh-TW":"已含桿童球車稅費",
            "en":"Include caddie/cart/VAT","vi":"Bao gồm caddie, xe điện, VAT",
            "ja":"キャディ・カート・VAT込み","ko":"캐디·카트·부가세 포함",
        }[lang]
        best_season = {
            "zh-CN":"10–4月最佳","zh-TW":"10–4月最佳",
            "en":"Oct–Apr","vi":"10–4","ja":"10月–4月","ko":"10월–4월",
        }[lang]
        i18n_rows.append((
            lang, name, c["designer"], address,
            seo_title, "", "",
            overview, "", fee_note, best_season, ""
        ))
    cur.executemany("""
        INSERT INTO golf_course_i18n
        (course_id,lang,name,designer_name,address,
         seo_title,seo_description,meta_keywords,
         overview,content,fee_note,best_season,tips_note)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, [(cid, *row) for row in i18n_rows])

    # 更新价格
    cur.execute("DELETE FROM course_price WHERE course_id=?", (cid,))
    cur.executemany("""
        INSERT INTO course_price
        (course_id,tier_type,rack_price_vnd,discount_price_vnd,discount_note,
         inc_caddie,inc_cart,inc_tax)
        VALUES (?,?,?,?,?,1,1,1)
    """, [(cid,*p) for p in PRICES])

# 更新汇率（若今天尚未存在）
if not cur.execute("SELECT 1 FROM fx_rate WHERE rate_date=?", (TODAY,)).fetchone():
    cur.executemany(
        "INSERT INTO fx_rate (rate_date,currency,rate_to_vnd,source) VALUES (?,?,?,'seed')",
        FX
    )

conn.commit()
cur.close()
conn.close()

print("✅ 已写入 10 个球场数据（含多语言、直接 embed 地图 iframe 代码、英文简介、汇率）")
