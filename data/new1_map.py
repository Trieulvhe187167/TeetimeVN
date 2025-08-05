# -*- coding: utf-8 -*-
"""
seed_north_vn_plus_halong.py
----------------------------
向 teetimevn_dev.db 写入：
  - 北越最佳球场 5 个
  - 下龙湾球场   2 个
共 7 条记录，含 6 语言翻译（简体、中繁、英、越、日、韩）、示例价格、Maps Embed、当天汇率。
新增：每个球场的英文简介 overview_en 字段，用作原始语言。
"""

import sqlite3
from pathlib import Path
from datetime import date

DB_PATH = Path("data/teetimevn_dev.db")   # 如数据库在 data/ 目录请改为 Path("data/teetimevn_dev.db")
TODAY   = date.today().isoformat()


conn = sqlite3.connect(DB_PATH)
cur  = conn.cursor()


# reset golf_course id sequence
cur.execute("DELETE FROM golf_course;")
cur.execute("DELETE FROM sqlite_sequence WHERE name='golf_course';")
cur.execute("DELETE FROM golf_course_i18n;")
cur.execute("DELETE FROM course_price;")

# ────────────────────────────────────────────────
# 1. 统一示例价格 & 汇率（含今天日期）
# ────────────────────────────────────────────────
PRICES = [
    ("weekday", 2500000, 2250000, "-10%"),
    ("weekend", 3200000, 2900000, "-9%"),
    ("twilight", 1800000, 1600000, "-11%"),
]

FX = [
    (TODAY, "USD", 25500),
    (TODAY, "CNY", 3550),
    (TODAY, "KRW", 19.5),
    (TODAY, "JPY", 170),
    (TODAY, "TWD", 830),
]

# ────────────────────────────────────────────────
# 2. 球场资料（包含 <iframe> embed code，新增 overview_en 英文简介）
# ────────────────────────────────────────────────
courses = [
    {
        "slug": "brg-kings-island",
        "names": {
            "zh-CN":"BRG帝王岛高尔夫度假俱乐部",
            "zh-TW":"BRG帝王島高爾夫度假俱樂部",
            "en":"BRG Kings Island Golf Resort",
            "vi":"Khu nghỉ dưỡng & Sân golf BRG Kings Island",
            "ja":"BRGキングスアイランドゴルフリゾート",
            "ko":"BRG 킹스 아일랜드 골프 리조트",
        },
        "holes":36, "par":72, "length":7461, "year":1997,
        "lat":21.0903, "lng":105.4338,
        "designer":"Robert McFarland / Luke Donald",
        "maps_embed": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d16852.056386306995!2d105.47847025852653!3d21.058509714283947!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31345eba00b303cb%3A0xe16f6d07cad144f6!2zQlJHIEtpbmdzIElzbGFuZCBHb2xmIFJlc29ydCwgU8ahbiDEkMO0bmcsIFPGoW4gVMOieSwgSMOgIE7hu5lpLCBWaeG7h3QgTmFt!5e1!3m2!1svi!2s!4v1746792822583!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>""",
        "overview":    "位于东莫湖半岛与岛屿上，由湖景与山景两座18洞组成，是北越最早的度假型球场。",
        "overview_tw": "位於東莫湖半島與島嶼上，由湖景與山景兩座18洞組成，是北越最早的度假型球場。",
        "overview_vi": "Nằm trên bán đảo Đông Mô và đảo, gồm hai sân 18 hố với cảnh hồ và cảnh núi, là sân resort đầu tiên miền Bắc.",
        "overview_en": "Located on the Dong Mo Lake peninsula and island, this resort features two 18-hole courses with scenic lake and mountain views, and is northern Vietnam’s first resort-style golf course.",
        "overview_ja": "東モ湖の半島と島に位置し、湖景と山景の2つの18ホールで構成され、北部ベトナム初のリゾート型コースです。",
        "overview_ko": "동모호 반도와 섬에 위치해 호수 경관과 산 경관의 18홀 2개 코스로 구성된, 북부 베트남 최초의 리조트형 골프장입니다。",
    },
    {
        "slug": "chi-linh-star",
        "names": {
            "zh-CN":"芝玲星高尔夫乡村俱乐部",
            "zh-TW":"芝玲星高爾夫鄉村俱樂部",
            "en":"Chi Linh Star Golf & Country Club",
            "vi":"Câu lạc bộ golf Chi Linh Star",
            "ja":"チーリンスターゴルフ＆カントリークラブ",
            "ko":"치린스타 골프 앤 컨트리 클럽",
        },
        "holes":27, "par":72, "length":7002, "year":2003,
        "lat":21.0646, "lng":106.2949,
        "designer":"IGCS Pty Ltd",
        "maps_embed": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4211.846941985588!2d106.39798417566962!3d21.09969588533755!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x313579a7aaaaaaab%3A0xc1629d65a155cb14!2zU8OibiBnb2xmIENow60gTGluaA!5e1!3m2!1svi!2s!4v1746792446781!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
""",
        "overview":    "27洞丘陵环湖，数次承办越南公开赛，被誉为“北越最具挑战”。",
        "overview_tw": "27洞丘陵環湖，數次承辦越南公開賽，被譽為“北越最具挑戰”。",
        "overview_vi": "27 hố đồi bao quanh hồ, nhiều lần tổ chức Vietnam Open, được mệnh danh “thử thách nhất miền Bắc”.",
        "overview_en": "A 27-hole parkland and lakeside course that has hosted the Vietnam Open multiple times, renowned as the most challenging course in northern Vietnam.",
        "overview_ja": "27ホールの丘陵型レイクサイドコース。ベトナムオープンを数度開催し「北部で最も挑戦的」と称されます。",
        "overview_ko": "27홀 언덕형 호숫가 코스, 베트남 오픈을 여러 차례 개최하여 ‘북부에서 가장 도전적인 코스’로 불립니다。",
    },
    {
        "slug": "heron-lake-golf",
        "names": {
            "zh-CN":"苍鹭湖高尔夫球场",
            "zh-TW":"蒼鷺湖高爾夫球場",
            "en":"Heron Lake Golf Course",
            "vi":"Sân golf Heron Lake",
            "ja":"ヘロンレイクゴルフコース",
            "ko":"헤론 레이크 골프 코스",
        },
        "holes":18, "par":72, "length":7035, "year":2010,
        "lat":21.2828, "lng":105.6077,
        "designer":"Pacific Coast Design",
        "maps_embed": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4206.293221171542!2d105.61151727567359!3d21.294632178592906!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3134fab93ac6aaab%3A0x7bd1cb3b216fd9b1!2sHeron%20Lake%20Golf%20Course%20%26%20Resort!5e1!3m2!1svi!2s!4v1746792465063!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
""",
        "overview":    "生态湿地型布局，常有苍鹭白鹭栖息，果岭波浪明显。",
        "overview_tw": "生態濕地型布局，常有蒼鷺白鷺棲息，果嶺波浪明顯。",
        "overview_vi": "Thiết kế dạng đầm lầy sinh thái, cò trắng và vạc thường trú, green gợn sóng rõ rệt.",
        "overview_en": "An ecological wetland layout where herons and egrets gather, featuring pronounced undulating greens.",
        "overview_ja": "湿地生態型レイアウトで、シラサギやダイサギが生息。グリーンのウェーブが特徴です。",
        "overview_ko": "생태 습지형 레이아웃으로 왜가리와 백로가 서식하며 그린의 물결이 뚜렷합니다。",
    },
    {
        "slug": "long-bien-golf",
        "names": {
            "zh-CN":"龙边高尔夫俱乐部",
            "zh-TW":"龍邊高爾夫俱樂部",
            "en":"Long Bien Golf Course",
            "vi":"Sân golf Long Biên",
            "ja":"ロンビエンゴルフコース",
            "ko":"롱비엔 골프 코스",
        },
        "holes":27, "par":72, "length":7000, "year":2014,
        "lat":21.0390, "lng":105.8709,
        "designer":"Nelson & Haworth",
        "maps_embed": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4213.603375697634!2d105.89321437566842!3d21.03768618747118!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3135a96e8f185ef9%3A0xe695123a455d2c09!2zU8OibiBHb2xmIExvbmcgQmnDqm4!5e1!3m2!1svi!2s!4v1746792486196!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
""",
        "overview":    "距河内中心 20 分钟，夜灯设施可开球至凌晨。",
        "overview_tw": "距河內中心 20 分鐘，夜燈設施可開球至凌晨。",
        "overview_vi": "Cách trung tâm Hà Nội 20 phút, có đèn chiếu sáng chơi đến khuya.",
        "overview_en": "Just 20 minutes from central Hanoi, this course features night lighting so you can play until the early hours.",
        "overview_ja": "ハノイ中心部から車で20分。ナイトゴルフ用照明で深夜までプレー可。",
        "overview_ko": "하노이 중심부에서 차로 20분, 야간 조명 시설로 자정까지 플레이할 수 있습니다。",
    },
    {
        "slug": "sky-lake-resort",
        "names": {
            "zh-CN":"天湖高尔夫度假俱乐部",
            "zh-TW":"天湖高爾夫度假俱樂部",
            "en":"Sky Lake Resort & Golf Club",
            "vi":"Khu nghỉ dưỡng & Sân golf Sky Lake",
            "ja":"スカイレイクリゾート＆ゴルフクラブ",
            "ko":"스카이 레이크 리조트 & 골프 클럽",
        },
        "holes":36, "par":72, "length":7265, "year":2012,
        "lat":20.9336, "lng":105.6154,
        "designer":"Ahn Moon Hwan",
        "maps_embed": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4219.3314661264585!2d105.6166407756643!3d20.83423579443059!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x313448cb761f89a5%3A0xe1816fee44021931!2sS%C3%A2n%20golf%20Sky%20Lake!5e1!3m2!1svi!2s!4v1746792502762!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
""",
        "overview":    "分 Sky 竞赛场与 Lake 度假场，两度获评越南最佳球场。",
        "overview_tw": "分 Sky競賽場與Lake度假場，兩度獲評越南最佳球場。",
        "overview_vi": "Chia thành sân Sky thi đấu và sân Lake nghỉ dưỡng, hai lần được bình chọn sân golf tốt nhất VN.",
        "overview_en": "Featuring a competitive Sky course and a resort-style Lake course, each voted Vietnam’s Best Golf Course twice.",
        "overview_ja": "Sky競技コースとLakeリゾートコースに分かれ、2度ベトナムベストコースに選出。",
        "overview_ko": "경기용 Sky 코스와 리조트형 Lake 코스로 구분되며, 베트남 최고의 골프장으로 두 차례 선정되었습니다。",
    },
    {
        "slug": "flc-halong-golf",
        "names": {
            "zh-CN":"FLC下龙湾高尔夫球场",
            "zh-TW":"FLC下龍灣高爾夫球場",
            "en":"FLC Halong Bay Golf Club",
            "vi":"Sân golf FLC Hạ Long Bay",
            "ja":"FLCハロンベイゴルフクラブ",
            "ko":"FLC 하롱베이 골프 클럽",
        },
        "holes":18, "par":71, "length":6900, "year":2017,
        "lat":20.9734, "lng":107.0371,
        "designer":"Schmidt-Curley",
        "maps_embed": """
<iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d4215.960280739688!2d107.1104125256668!3d20.954202040334387!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1s%09FLC%20Halong%20Bay%20Golf%20Club!5e1!3m2!1svi!2s!4v1746792520852!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
""",
        "overview":    "坐拥世界遗产下龙湾全景，被誉为“空中球场”，每一洞都是观景台。",
        "overview_tw": "坐擁世界遺產下龍灣全景，被譽為“空中球場”，每一洞都是觀景台。",
        "overview_vi": "Tận hưởng toàn cảnh vịnh Hạ Long, mệnh danh “sân golf trên không”, mỗi hố là đài quan sát.",
        "overview_en": "Perched above the World Heritage site of Ha Long Bay, each hole serves as an aerial viewing platform—hence its nickname, the “Sky Course.”",
        "overview_ja": "世界遺産ハロン湾の全景が望め、“空中ゴルフ場”と称されます。全ホールが展望台です。",
        "overview_ko": "세계유산 하롱베이 전경을 감상할 수 있는 ‘공중 골프장’으로, 모든 홀이 전망대입니다。",
    },
    {
        "slug": "tuan-chau-golf",
        "names": {
            "zh-CN":"珍珠岛传奇高尔夫",
            "zh-TW":"珍珠島傳奇高爾夫",
            "en":"Tuan Chau Golf Resort",
            "vi":"Sân golf Khu nghỉ dưỡng Tuần Châu",
            "ja":"トゥアンチャウゴルフリゾート",
            "ko":"투안짜우 골프 리조트",
        },
        "holes":18, "par":72, "length":7400, "year":2021,
        "lat":20.9345, "lng":106.9655,
        "designer":"Brian Curley",
        "maps_embed": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4216.45324568235!2d106.96944057566633!3d20.936700490933337!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31356d00216b9835%3A0x928ef3ae99fd91b!2sTuan%20Chau%20Golf%20Resort!5e1!3m2!1svi!2s!4v1746792557851!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
""",
        "overview":    "下龙湾珍珠岛最新 18 洞林克斯风格球场，白沙护堡果岭极具挑战。",
        "overview_tw": "下龍灣珍珠島最新18洞林克斯風格球場，白沙護堡果嶺極具挑戰。",
        "overview_vi": "Sân Links 18 hố mới trên đảo Ngọc Tuần Châu, bunker cát trắng và green đầy thách thức.",
        "overview_en": "The latest 18-hole links course on Pearl Island features white-sand bunkers and challenging greens against a backdrop of Ha Long Bay.",
        "overview_ja": "下龍湾の真珠島にある最新18ホールリンクスコース。白い砂のバンカーと挑戦的なグリーンが特徴です。",
        "overview_ko": "하롱베이 진주섬의 최신 18홀 링크스 코스, 백사장 벙커와 도전적인 그린이 특징입니다。",
    },
]

# ────────────────────────────────────────────────
# 3. 插入数据库
# ────────────────────────────────────────────────


for c in courses:
    # 删除旧 golf_course
    cur.execute("DELETE FROM golf_course WHERE slug=?", (c["slug"],))
    # 插入主表，maps_url 字段存放 <iframe> HTML
    cur.execute("""
        INSERT INTO golf_course
        (slug, holes, par, length_yards, opened_year, lat, lng, maps_url, scorecard_pdf)
        VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        c["slug"], c["holes"], c["par"], c["length"],
        c["year"], c["lat"], c["lng"],
        c["maps_embed"],                     # <-- embed HTML
        f"/static/media/{c['slug']}_scorecard.pdf"
    ))
    cid = cur.lastrowid

    # 删除旧 i18n 并插入 6 语言（包含英文 overview_en）
    cur.execute("DELETE FROM golf_course_i18n WHERE course_id=?", (cid,))
    i18n_rows = []
    for lang in ["zh-CN","zh-TW","en","vi","ja","ko"]:
        nm      = c["names"][lang]
        ov_key  = "overview" if lang=="zh-CN" else f"overview_{lang.replace('-','_')}"
        ov      = c.get(ov_key, "")
        addr_map = {
            "zh-CN":"河内/下龙湾","zh-TW":"河內/下龍灣",
            "en":"Hanoi / Ha Long Bay","vi":"Hà Nội / Hạ Long Bay",
            "ja":"ハノイ / ハロン湾","ko":"하노이 / 하롱베이"
        }
        addr    = addr_map[lang]
        seo_map = {
            "zh-CN": f"{nm} - 越南北部/下龙湾高尔夫",
            "zh-TW": f"{nm} - 越南北部/下龍灣高爾夫",
            "en":    f"{nm} | Vietnam Golf",
            "vi":    f"{nm} | Golf Việt Nam",
            "ja":    f"{nm} – ベトナムゴルフ",
            "ko":    f"{nm} – 베트남 골프",
        }
        fee_note_map = {
            "zh-CN":"已含球童球车税费","zh-TW":"已含桿童球車稅費",
            "en":"Include caddie/cart/VAT","vi":"Bao gồm caddie, xe điện, VAT",
            "ja":"キャディ・カート・VAT込み","ko":"캐디·카트·부가세 포함",
        }
        best_season_map = {
            "zh-CN":"10–4月最佳","zh-TW":"10–4月最佳",
            "en":"Oct–Apr","vi":"10–4","ja":"10月–4月","ko":"10월–4월",
        }
        i18n_rows.append((
            lang, nm, c["designer"], addr,
            seo_map[lang], "", "",
            ov, "", fee_note_map[lang], best_season_map[lang], ""
        ))

    cur.executemany("""
        INSERT INTO golf_course_i18n
        (course_id, lang, name, designer_name, address,
         seo_title, seo_description, meta_keywords,
         overview, content, fee_note, best_season, tips_note)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, [(cid, *row) for row in i18n_rows])

    # 更新价格：先删除再插入
    cur.execute("DELETE FROM course_price WHERE course_id=?", (cid,))
    cur.executemany("""
        INSERT INTO course_price
        (course_id, tier_type, rack_price_vnd, discount_price_vnd, discount_note,
         inc_caddie, inc_cart, inc_tax)
        VALUES (?,?,?,?,?,1,1,1)
    """, [(cid, *p) for p in PRICES])

# 更新汇率（若今日尚未存在）
if not cur.execute("SELECT 1 FROM fx_rate WHERE rate_date=?", (TODAY,)).fetchone():
    cur.executemany(
        "INSERT INTO fx_rate (rate_date, currency, rate_to_vnd, source) VALUES (?,?,?,'seed')",
        FX
    )

conn.commit()
cur.close()
conn.close()

print("✅ 已写入 5 个北越 + 2 个下龙湾球场数据 (含 6 语言 + embed 地图 + 汇率 + 英文简介)") 
