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
        "slug": "van-tri-golf",
        "names": {
            "zh-CN": "云池高尔夫俱乐部", "zh-TW": "雲池高爾夫俱樂部",
            "en":    "Van Tri Golf Club", "vi":    "Sân golf Vân Trì",
            "ja":    "ヴァンチーゴルフクラブ","ko":   "반찌 골프 클럽",
        },
        "overview":    "河内唯一纯会员制球场，常年草质优异。",
        "overview_tw": "河內唯一純會員制球場，常年草質優異。",
        "overview_vi": "Sân golf thành viên duy nhất ở Hà Nội, chất lượng cỏ tuyệt hảo quanh năm.",
        "overview_en": "Hanoi’s only private membership course, with top‐quality turf year-round.",
        "overview_ja": "ハノイ唯一の会員制コース。年間を通じて芝質が優れています。",
        "overview_ko": "하노이 유일의 멤버십 전용 골프장, 연중 최상의 코스 상태를 유지합니다。",
        "holes": 18, "par": 72, "length": 7200, "year": 2007,
        "lat": 21.1114, "lng": 105.8309, "designer": "Peter Rousseau",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4210.4789927614775!2d105.79604617567064!3d21.14787018367609!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3135003b61ed7907%3A0x98e52563a31d108!2zU8OibiBHb2xmIFbDom4gVHLDrA!5e1!3m2!1svi!2s!4v1746792573637!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },
    {
        "slug": "tam-dao-golf",
        "names": {
            "zh-CN": "三岛高尔夫度假俱乐部","zh-TW": "三島高爾夫度假俱樂部",
            "en":    "Tam Dao Golf Resort",  "vi":    "Sân golf Tam Đảo",
            "ja":    "タムダオゴルフリゾート","ko":   "탐다오 골프 리조트",
        },
        "overview":    "坐落三岛山脚，海拔高温度低，是夏季避暑首选。",
        "overview_tw": "坐落三島山腳，海拔高溫度低，是夏季避暑首選。",
        "overview_vi": "Nằm dưới chân núi Tam Đảo, độ cao mang lại khí hậu mát mẻ, tránh nóng lý tưởng.",
        "overview_en": "Nestled at the foot of Tam Dao mountain—its elevation provides a perfect summer retreat.",
        "overview_ja": "タムダオ山麓に位置し、標高が高く涼しい夏の避暑地として最適です。",
        "overview_ko": "탐다오 산기슭에 위치해 해발이 높아 여름철 피서지로 인기가 많습니다。",
        "holes": 18, "par": 72, "length": 7200, "year": 2005,
        "lat": 21.3816, "lng": 105.5607, "designer": "IMG",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4202.9868819280255!2d105.62415317567593!3d21.409881074578603!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3134e5552da78f71%3A0x5810f597c998af75!2zU8OibiBHb2xmIFRhbSDEkOG6o28!5e1!3m2!1svi!2s!4v1746792600397!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },
    {
        "slug": "montgomerie-links",
        "names": {
            "zh-CN": "蒙哥马利林克斯高尔夫","zh-TW": "蒙哥馬利林克斯高爾夫",
            "en":    "Montgomerie Links Vietnam","vi":    "Montgomerie Links Việt Nam",
            "ja":    "モンゴメリーリンクスベトナム","ko":   "몽고메리 링크스 베트남",
        },
        "overview":    "会安-岘港海岸线上经典林克斯风格，海风大考验控球。",
        "overview_tw": "會安-峴港海岸線上經典林克斯風格，海風大考驗控球。",
        "overview_vi": "Phong cách links cổ điển ven biển Hội An–Đà Nẵng, gió biển thách thức kiểm soát bóng.",
        "overview_en": "Classic seaside links on the Hoi An–Da Nang coast—wind is the ultimate test of shot control.",
        "overview_ja": "ホイアン–ダナン海岸線沿いのクラシックリンクス。海風がコントロールを試します。",
        "overview_ko": "호이안–다낭 해안선을 따라 펼쳐진 클래식 링크스, 바닷바람이 샷 컨트롤을 시험합니다。",
        "holes": 18, "par": 72, "length": 7090, "year": 2009,
        "lat": 15.9512, "lng": 108.2520, "designer": "Colin Montgomerie",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4340.438649077087!2d108.28250697558045!3d15.963005942271991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x314210526bf356ab%3A0x845407b189779099!2sCLB%20Golf%20Montgomerie%20Links%20Vietnam!5e1!3m2!1svi!2s!4v1746792618380!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },
    {
        "slug": "laguna-langco",
        "names": {
            "zh-CN": "朗珂拉古娜高尔夫俱乐部","zh-TW": "朗珂拉古娜高爾夫俱樂部",
            "en":    "Laguna Lang Co Golf Club","vi":    "Sân golf Laguna Lăng Cô",
            "ja":    "ラグーナランコーゴルフクラブ","ko":   "라구나 랑코 골프 클럽",
        },
        "overview":    "海滩、稻田、溪谷三种景观贯穿，2019亚洲最佳度假球场。",
        "overview_tw": "海灘、稻田、溪谷三種景觀貫穿，2019亞洲最佳度假球場。",
        "overview_vi": "Ba cảnh quan—biển, ruộng lúa, thung lũng—Asia’s Best Resort Course 2019.",
        "overview_en": "Three vistas—beach, rice paddies, valleys—crowned Asia’s Best Resort Course 2019.",
        "overview_ja": "ビーチ、田んぼ、渓谷の3つの景観を融合。2019年アジア最高リゾートコース。",
        "overview_ko": "해변·논·계곡 3경 완벽 조화. 2019년 아시아 최고 리조트 코스 선정.",
        "holes": 18, "par": 71, "length": 6958, "year": 2013,
        "lat": 16.2989, "lng": 107.9541, "designer": "Nick Faldo",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4332.369610833168!2d107.95325847558588!3d16.331240932369493!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3141860a320501ff%3A0xe0b3297f8385c84!2zU8OibiBnb2xmIExhZ3VuYSBMxINuZyBDw7Q!5e1!3m2!1svi!2s!4v1746792642770!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },
    {
        "slug": "banahills-gc-light",
        "names": {
            "zh-CN":"巴拿山光影高尔夫俱乐部","zh-TW":"巴拿山光影高爾夫俱樂部",
            "en":"Ba Na Hills GC Light Course","vi":"Sân golf Ba Na Hills Light",
            "ja":"バナヒルズGCライトコース","ko":"바나힐스 GC 라이트 코스",
        },
        "overview":    "巴拿山夜间9洞灯光场，兼顾练习与亲子体验。",
        "overview_tw":"巴拿山夜間9洞燈光場，兼顧練習與親子體驗。",
        "overview_vi":"Sân 9 hố đêm Ba Na Hills—luyện tập và giải trí gia đình.",
        "overview_en":"9-hole floodlit night course at Ba Na Hills—perfect for practice and family fun.",
        "overview_ja":"バナヒルズのナイト9ホール。練習と家族体験を両立。",
        "overview_ko":"바나힐스 9홀 야간 코스—연습과 가족 체험에 최적.",
        "holes": 9,  "par": 36, "length": 3400, "year": 2024,
        "lat": 16.0600, "lng": 108.0188, "designer": "Luke Donald",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4339.25516981932!2d108.04661167558116!3d16.017530340818904!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31421df6e3a730bb%3A0xd899060c1d60086f!2sB%C3%A0%20N%C3%A0%20Hills%20Golf%20Club!5e1!3m2!1svi!2s!4v1746792662547!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },
    {
        "slug": "vietnam-golf-cc",
        "names": {
            "zh-CN":"越南高尔夫乡村俱乐部","zh-TW":"越南高爾夫鄉村俱樂部",
            "en":"Vietnam Golf & Country Club","vi":"Câu lạc bộ golf Việt Nam",
            "ja":"ベトナムゴルフ＆カントリークラブ","ko":"베트남 골프 & 컨트리 클럽",
        },
        "overview":    "距胡志明 30 分钟车程，是越南历史最悠久的36洞。",
        "overview_tw":"距胡志明市30分鐘車程，是越南歷史最悠久的36洞球場。",
        "overview_vi":"Cách TP.HCM 30 phút—sân 36 hố lâu đời nhất Việt Nam.",
        "overview_en":"Just 30 minutes from Ho Chi Minh City—home to Vietnam’s oldest 36-hole facility.",
        "overview_ja":"ホーチミンから車で30分、ベトナム最古の36ホールコース。",
        "overview_ko":"호치민에서 차로 30분—베트남에서 가장 오래된 36홀 코스。",
        "holes": 36, "par": 72, "length": 7106, "year": 1995,
        "lat": 10.8842, "lng": 106.7329, "designer": "Lee Trevino / PCD",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4433.575282403004!2d106.82114997552179!3d10.866251657529443!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x317521736362a271%3A0x23d2d0e360484be7!2sVietnam%20Golf%20%26%20Country%20Club!5e1!3m2!1svi!2s!4v1746792681586!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },
    {
        "slug": "twin-doves-golf",
        "names": {
            "zh-CN":"双鸽高尔夫俱乐部","zh-TW":"雙鴿高爾夫俱樂部",
            "en":"Twin Doves Golf Club","vi":"Sân golf Twin Doves",
            "ja":"ツインダヴズゴルフクラブ","ko":"트윈 도브스 골프 클럽",
        },
        "overview":    "三组9洞环湖布局，果岭速度快以锦标赛规格养护。",
        "overview_tw":"三組9洞環湖布局，果嶺速度快以錦標賽規格養護。",
        "overview_vi":"Three 9-hole loops around a lake with tournament-speed greens.",
        "overview_en":"Three 9-hole loops around a lake with tournament-speed greens.",
        "overview_ja":"湖畔に3×9ホールのレイアウト。グリーンは競技用速度。",
        "overview_ko":"호수 주변 3×9홀 구성, 그린은 토너먼트 스피드로 유지됩니다。",
        "holes": 27, "par": 72, "length": 7200, "year": 2011,
        "lat": 10.9286, "lng": 106.7038, "designer": "Peter Rousseau",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4431.232782565991!2d106.66560937552315!3d11.022840154599264!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3174d1ba10079c09%3A0xe3a3c15b06c08800!2sTwin%20Doves%20Golf%20Club!5e1!3m2!1svi!2s!4v1746792698028!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },
    {
        "slug": "sanctuary-ho-tram",
        "names": {
            "zh-CN":"后潭圣地高尔夫","zh-TW":"後潭聖地高爾夫",
            "en":"Sanctuary Ho Tram Golf","vi":"Sân golf Sanctuary Hồ Tràm",
            "ja":"サンクチュアリーホーチャムゴルフ","ko":"산츄어리 호짬 골프",
        },
        "overview":    "2022年全新林克斯，白沙丘与海风塑造纯正外观。",
        "overview_tw":"2022年全新林克斯，白沙丘與海風塑造純正外觀。",
        "overview_vi":"Links hoàn toàn mới 2022, đồi cát trắng và gió biển đặc trưng.",
        "overview_en":"A brand-new links in 2022 featuring white sand dunes and sea breezes for an authentic coastal experience.",
        "overview_ja":"2022年開場の新リンクス。白砂丘と海風が特徴です。",
        "overview_ko":"2022년 개장 링크스 코스, 백사장과 해풍이 특징입니다。",
        "holes": 18, "par": 71, "length": 7000, "year": 2022,
        "lat": 10.4941, "lng": 107.4089, "designer": "Robert Trent Jones II",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d8878.554660407843!2d107.4336645933796!3d10.475428558672062!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1sSanctuary%20Ho%20Tram%20Golf!5e1!3m2!1svi!2s!4v1746792720931!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },
    {
        "slug": "vinpearl-phu-quoc",
        "names": {
            "zh-CN":"珍珠富国高尔夫俱乐部","zh-TW":"珍珠富國高爾夫俱樂部",
            "en":"Vinpearl Golf Phu Quoc","vi":"Sân golf Vinpearl Phú Quốc",
            "ja":"ヴィンパールゴルフフーコック","ko":"빈펄 골프 푸꾸옥",
        },
        "overview":    "富国岛北部热带森林环抱，球道宽阔，度假氛围浓厚。",
        "overview_tw":"富國島北部熱帶森林環抱，球道寬闊，度假氛圍濃厚。",
        "overview_vi":"Bắc Phú Quốc ôm trọn rừng nhiệt đới, fairway rộng, không khí nghỉ dưỡng đậm đà.",
        "overview_en":"Surrounded by tropical forest in north Phu Quoc—wide fairways and a rich resort atmosphere.",
        "overview_ja":"フーコック北部の熱帯雨林に囲まれ、フェアウェイが広くリゾート感満載。",
        "overview_ko":"푸꾸옥 북부 열대우림에 둘러싸인 넓은 페어웨이와 휴양 분위기 가득。",
        "holes": 27, "par": 72, "length": 7080, "year": 2015,
        "lat": 10.2680, "lng": 103.9669, "designer": "IMG",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4441.138931679889!2d103.8510828755175!3d10.344673167008079!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31081e467f316a51%3A0xc7cc60267a508cda!2zVmlucGVhcmwgR29sZiBQaMO6IFF14buRYw!5e1!3m2!1svi!2s!4v1746792745743!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
"""
    },
    {
        "slug": "dalat-1200-golf",
        "names": {
            "zh-CN":"大叻1200高尔夫俱乐部","zh-TW":"大叻1200高爾夫俱樂部",
            "en":"The Dalat 1200 Golf Club","vi":"Sân golf Đà Lạt 1200",
            "ja":"ザ・ダラット1200ゴルフクラブ","ko":"달랏 1200 골프 클럽",
        },
        "overview":    "坐落海拔 1200 米高原湖畔，全年平均 20°C，被誉为“亚洲瑞士”。",
        "overview_tw":"位於海拔1200米高原湖畔，全年平均20°C，被譽為「亞洲瑞士」。",
        "overview_vi":"Nằm ở cao nguyên 1.200m ven hồ, nhiệt độ trung bình 20°C, được mệnh danh “Thụy Sĩ châu Á”.",
        "overview_en":"Perched at 1,200m elevation by a highland lake—year-round 20°C, known as the “Switzerland of Asia.”",
        "overview_ja":"標高1200mの高原湖畔に位置し、年間平均20°Cで「アジアのスイス」と称されます。",
        "overview_ko":"해발 1,200m 고원 호숫가에 위치, 연평균 20°C로 “아시아의 스위스”로 불립니다。",
        "holes": 18, "par": 73, "length": 7217, "year": 2015,
        "lat": 11.8686, "lng": 108.4410, "designer": "Peter Rousseau",
        "maps": """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4419.282452595323!2d108.45334767553022!3d11.78975043968526!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31713fbe98af9201%3A0x14cade8e214e3476!2sS%C3%A2n%20Golf%20The%20D%C3%A0lat%20at%201200!5e1!3m2!1svi!2s!4v1746792760845!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
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
