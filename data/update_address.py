import sqlite3
conn = sqlite3.connect('data/teetimevn_dev.db')
cur = conn.cursor()

sql = """
-- course_id = 1 (BRG Kings Island – Bán đảo Sơn Trà, Đà Nẵng)
UPDATE golf_course_i18n SET address='Bán đảo Sơn Trà, Đà Nẵng' WHERE course_id=1 AND lang='vi';
UPDATE golf_course_i18n SET address='Son Tra Peninsula, Da Nang, Vietnam' WHERE course_id=1 AND lang='en';
UPDATE golf_course_i18n SET address='越南岘港市山茶半岛' WHERE course_id=1 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南峴港市山茶半島' WHERE course_id=1 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ダナン市 ソンチャ半島' WHERE course_id=1 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 다낭시 손짜반도' WHERE course_id=1 AND lang='ko';

-- course_id = 2 (Chi Linh Star – Thị xã Chí Linh, Hải Dương)
UPDATE golf_course_i18n SET address='Thị xã Chí Linh, Hải Dương' WHERE course_id=2 AND lang='vi';
UPDATE golf_course_i18n SET address='Chi Linh Town, Hai Duong, Vietnam' WHERE course_id=2 AND lang='en';
UPDATE golf_course_i18n SET address='越南海阳省芝林市' WHERE course_id=2 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南海陽省芝林市' WHERE course_id=2 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ハイズオン省 チーリン市' WHERE course_id=2 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 하이즈엉성 치링시' WHERE course_id=2 AND lang='ko';

-- course_id = 3 (Heron Lake – Xã Vân Trì, Đông Anh, Hà Nội)
UPDATE golf_course_i18n SET address='Xã Vân Trì, Huyện Đông Anh, Hà Nội' WHERE course_id=3 AND lang='vi';
UPDATE golf_course_i18n SET address='Van Tri Commune, Dong Anh District, Hanoi, Vietnam' WHERE course_id=3 AND lang='en';
UPDATE golf_course_i18n SET address='越南河内市东英县云止社' WHERE course_id=3 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南河內市東英縣雲止社' WHERE course_id=3 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ハノイ市 ドンアン区 ヴァンチー村' WHERE course_id=3 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 하노이시 동안구 반찌 마을' WHERE course_id=3 AND lang='ko';

-- course_id = 4 (Long Biên – Quận Long Biên, Hà Nội)
UPDATE golf_course_i18n SET address='Quận Long Biên, Hà Nội' WHERE course_id=4 AND lang='vi';
UPDATE golf_course_i18n SET address='Long Bien District, Hanoi, Vietnam' WHERE course_id=4 AND lang='en';
UPDATE golf_course_i18n SET address='越南河内市龙边区' WHERE course_id=4 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南河內市龍邊區' WHERE course_id=4 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ハノイ市 ロンビエン区' WHERE course_id=4 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 하노이시 롱비엔구' WHERE course_id=4 AND lang='ko';

-- course_id = 5 (Sky Lake – Đông Anh, Hà Nội)
UPDATE golf_course_i18n SET address='Huyện Đông Anh, Hà Nội' WHERE course_id=5 AND lang='vi';
UPDATE golf_course_i18n SET address='Dong Anh District, Hanoi, Vietnam' WHERE course_id=5 AND lang='en';
UPDATE golf_course_i18n SET address='越南河内市东英县' WHERE course_id=5 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南河內市東英縣' WHERE course_id=5 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ハノイ市 ドンアン区' WHERE course_id=5 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 하노이시 동안구' WHERE course_id=5 AND lang='ko';

-- course_id = 6 (FLC Hạ Long – TP. Hạ Long, Quảng Ninh)
UPDATE golf_course_i18n SET address='Thành phố Hạ Long, Quảng Ninh' WHERE course_id=6 AND lang='vi';
UPDATE golf_course_i18n SET address='Ha Long City, Quang Ninh, Vietnam' WHERE course_id=6 AND lang='en';
UPDATE golf_course_i18n SET address='越南广宁省下龙市' WHERE course_id=6 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南廣寧省下龍市' WHERE course_id=6 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム クアンニン省 ハロン市' WHERE course_id=6 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 꽝닌성 하롱시' WHERE course_id=6 AND lang='ko';

-- course_id = 7 (Tuần Châu – Đảo Tuần Châu, Hạ Long)
UPDATE golf_course_i18n SET address='Đảo Tuần Châu, Hạ Long, Quảng Ninh' WHERE course_id=7 AND lang='vi';
UPDATE golf_course_i18n SET address='Tuan Chau Island, Ha Long, Quang Ninh, Vietnam' WHERE course_id=7 AND lang='en';
UPDATE golf_course_i18n SET address='越南广宁省下龙市巡洲岛' WHERE course_id=7 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南廣寧省下龍市巡洲島' WHERE course_id=7 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム クアンニン省 ハロン市 トゥアンチャウ島' WHERE course_id=7 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 꽝닌성 하롱시 투안차우섬' WHERE course_id=7 AND lang='ko';

-- course_id = 8 (Van Tri Golf Club)
UPDATE golf_course_i18n SET address='Xã Vân Trì, Huyện Đông Anh, Hà Nội' WHERE course_id=8 AND lang='vi';
UPDATE golf_course_i18n SET address='Van Tri Commune, Dong Anh District, Hanoi, Vietnam' WHERE course_id=8 AND lang='en';
UPDATE golf_course_i18n SET address='越南河内市东英县云止社' WHERE course_id=8 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南河內市東英縣雲止社' WHERE course_id=8 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ハノイ市 ドンアン区 ヴァンチー村' WHERE course_id=8 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 하노이시 동안구 반찌 마을' WHERE course_id=8 AND lang='ko';

-- course_id = 9 (Tam Dao Golf Resort)
UPDATE golf_course_i18n SET address='Huyện Tam Đảo, Vĩnh Phúc' WHERE course_id=9 AND lang='vi';
UPDATE golf_course_i18n SET address='Tam Dao District, Vinh Phuc, Vietnam' WHERE course_id=9 AND lang='en';
UPDATE golf_course_i18n SET address='越南永福省潭岛县' WHERE course_id=9 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南永福省潭島縣' WHERE course_id=9 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ヴィンフック省 タムダオ県' WHERE course_id=9 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 빈푹성 탐다오현' WHERE course_id=9 AND lang='ko';

-- course_id = 10 (Montgomerie Links Vietnam)
UPDATE golf_course_i18n SET address='Phường Hòa Hải, Quận Ngũ Hành Sơn, Đà Nẵng' WHERE course_id=10 AND lang='vi';
UPDATE golf_course_i18n SET address='Hoa Hai Ward, Ngu Hanh Son District, Da Nang, Vietnam' WHERE course_id=10 AND lang='en';
UPDATE golf_course_i18n SET address='越南岘港市五行山区和海坊' WHERE course_id=10 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南峴港市五行山區和海坊' WHERE course_id=10 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ダナン市 グー・ハイン区 ホアハイ坊' WHERE course_id=10 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 다낭시 응우행손구 호아하이동' WHERE course_id=10 AND lang='ko';

-- course_id = 11 (Laguna Lang Co Golf Club)
UPDATE golf_course_i18n SET address='Xã Lộc Vinh, Huyện Phú Lộc, Thừa Thiên Huế' WHERE course_id=11 AND lang='vi';
UPDATE golf_course_i18n SET address='Loc Vinh Commune, Phu Loc District, Thua Thien Hue, Vietnam' WHERE course_id=11 AND lang='en';
UPDATE golf_course_i18n SET address='越南承天顺化省富乐县禄英社' WHERE course_id=11 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南承天順化省富樂縣祿英社' WHERE course_id=11 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム トゥアティエンフエ省 フーロック県 ロックヴィン村' WHERE course_id=11 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 튜아티엔후에성 푸록현 록빈사' WHERE course_id=11 AND lang='ko';

-- course_id = 12 (Ba Na Hills GC Light Course)
UPDATE golf_course_i18n SET address='Huyện Hòa Vang, Đà Nẵng' WHERE course_id=12 AND lang='vi';
UPDATE golf_course_i18n SET address='Hoa Vang District, Da Nang, Vietnam' WHERE course_id=12 AND lang='en';
UPDATE golf_course_i18n SET address='越南岘港市和枫县' WHERE course_id=12 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南峴港市和楓縣' WHERE course_id=12 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ダナン市 ホアヴァン区' WHERE course_id=12 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 다낭시 호아방구' WHERE course_id=12 AND lang='ko';

-- course_id = 13 (Vietnam Golf & Country Club)
UPDATE golf_course_i18n SET address='Khu đô thị Ciputra, Quận Nam Từ Liêm, Hà Nội' WHERE course_id=13 AND lang='vi';
UPDATE golf_course_i18n SET address='Ciputra Urban Area, Nam Tu Liem District, Hanoi, Vietnam' WHERE course_id=13 AND lang='en';
UPDATE golf_course_i18n SET address='越南河内市南慈廉区西浦特拉都市区' WHERE course_id=13 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南河內市南慈廉區西浦特拉都市區' WHERE course_id=13 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ハノイ市 ナムトゥリエム区 シプトラ都市区' WHERE course_id=13 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 하노이시 남뚜리엠구 시푸트라 도시지역' WHERE course_id=13 AND lang='ko';

-- course_id = 14 (Twin Doves Golf Club)
UPDATE golf_course_i18n SET address='Xã Lê Minh Xuân, Huyện Bình Chánh, TP. Hồ Chí Minh' WHERE course_id=14 AND lang='vi';
UPDATE golf_course_i18n SET address='Le Minh Xuan Commune, Binh Chanh District, Ho Chi Minh City, Vietnam' WHERE course_id=14 AND lang='en';
UPDATE golf_course_i18n SET address='越南胡志明市平政县黎明轩社' WHERE course_id=14 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南胡志明市平政縣黎明軒社' WHERE course_id=14 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ホーチミン市 ビンチャン区 レミンシュアン村' WHERE course_id=14 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 호치민시 빈찬구 레민쉬안사' WHERE course_id=14 AND lang='ko';

-- course_id = 15 (Sanctuary Ho Tram Golf)
UPDATE golf_course_i18n SET address='Huyện Xuyên Mộc, Bà Rịa-Vũng Tàu' WHERE course_id=15 AND lang='vi';
UPDATE golf_course_i18n SET address='Xuyen Moc District, Ba Ria - Vung Tau, Vietnam' WHERE course_id=15 AND lang='en';
UPDATE golf_course_i18n SET address='越南巴地头顿省穿木县' WHERE course_id=15 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南巴地頭頓省穿木縣' WHERE course_id=15 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム バリア・ブンタウ省 シュエンモック県' WHERE course_id=15 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 바리아붕따우성 쑤언목현' WHERE course_id=15 AND lang='ko';

-- course_id = 16 (Vinpearl Golf Phu Quoc)
UPDATE golf_course_i18n SET address='Xã Gành Dầu, Huyện Phú Quốc, Kiên Giang' WHERE course_id=16 AND lang='vi';
UPDATE golf_course_i18n SET address='Ganh Dau Commune, Phu Quoc District, Kien Giang, Vietnam' WHERE course_id=16 AND lang='en';
UPDATE golf_course_i18n SET address='越南坚江省富国县番渡社' WHERE course_id=16 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南堅江省富國縣番渡社' WHERE course_id=16 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム キエンザン省 フークォック県 ガインダウ社' WHERE course_id=16 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 껀장성 푸꾸옥현 간따우사' WHERE course_id=16 AND lang='ko';

-- course_id = 17 (The Dalat 1200 Golf Club)
UPDATE golf_course_i18n SET address='Phường 12, TP. Đà Lạt, Lâm Đồng' WHERE course_id=17 AND lang='vi';
UPDATE golf_course_i18n SET address='Ward 12, Da Lat City, Lam Dong, Vietnam' WHERE course_id=17 AND lang='en';
UPDATE golf_course_i18n SET address='越南林同省大叻市第12坊' WHERE course_id=17 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南林同省大叻市第12坊' WHERE course_id=17 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ラムドン省 ダラット市 第12区画' WHERE course_id=17 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 람동성 다랏시 제12구' WHERE course_id=17 AND lang='ko';

"""
cur.executescript(sql)
conn.commit()
conn.close()
print("Đã cập nhật xong address.")
