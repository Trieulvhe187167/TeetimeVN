import sqlite3
conn = sqlite3.connect('data/teetimevn_dev.db')
cur = conn.cursor()

sql = """

UPDATE golf_course_i18n SET address='Xã Kỳ Phú, Huyện Nho Quan, Tỉnh Ninh Bình' WHERE course_id=44 AND lang='vi';
UPDATE golf_course_i18n SET address='Ky Phu Commune, Nho Quan District, Ninh Binh Province, Vietnam' WHERE course_id=44 AND lang='en';
UPDATE golf_course_i18n SET address='越南宁平省儒关县基富乡' WHERE course_id=44 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南寧平省儒關縣基富鄉' WHERE course_id=44 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ニンビン省 ニョクアン郡 キーフー村' WHERE course_id=44 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 닌빈성 노관현 기푸 코뮌' WHERE course_id=44 AND lang='ko';


UPDATE golf_course_i18n SET address='Thôn 4B, Xã Đông Sơn, Thành phố Tam Điệp, Tỉnh Ninh Bình' WHERE course_id=45 AND lang='vi';
UPDATE golf_course_i18n SET address='Hamlet 4B, Dong Son Commune, Tam Diep City, Ninh Binh Province, Vietnam' WHERE course_id=45 AND lang='en';
UPDATE golf_course_i18n SET address='越南宁平省三叠市东山县4B村' WHERE course_id=45 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南寧平省三疊市東山鄉4B村' WHERE course_id=45 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ニンビン省 タムディエップ市 ドンソン村 4B' WHERE course_id=45 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 닌빈성 탐디엡시 동선 코뮌 4B 마을' WHERE course_id=45 AND lang='ko';

UPDATE golf_course_i18n SET address='Khu du lịch quốc tế Đồ Sơn, Phường Vạn Hương, Quận Đồ Sơn, Thành phố Hải Phòng' WHERE course_id=46 AND lang='vi';
UPDATE golf_course_i18n SET address='Dragon Ocean International Tourist Complex, Van Huong Ward, Do Son District, Hai Phong City, Vietnam' WHERE course_id=46 AND lang='en';
UPDATE golf_course_i18n SET address='越南海防市多山区万香坊龙洋国际旅游区' WHERE course_id=46 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南海防市多山區萬香坊龍洋國際旅遊區' WHERE course_id=46 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ハイフォン市 ドーソン区 ヴァンフオン坊 ドラゴンオーシャン国際観光コンプレックス' WHERE course_id=46 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 하이퐁시 도선구 반흐엉동 드래곤 오션 국제 관광 단지' WHERE course_id=46 AND lang='ko';


UPDATE golf_course_i18n SET address='Đảo Vũ Yên, Quận Hải An, Thành phố Hải Phòng' WHERE course_id=47 AND lang='vi';
UPDATE golf_course_i18n SET address='Vu Yen Island, Hai An District, Hai Phong City, Vietnam' WHERE course_id=47 AND lang='en';
UPDATE golf_course_i18n SET address='越南海防市海安区武燕岛' WHERE course_id=47 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南海防市海安區武燕島' WHERE course_id=47 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ハイフォン市 ハイアン区 ヴーイエン島' WHERE course_id=47 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 하이퐁시 하이안구 부옌 섬' WHERE course_id=47 AND lang='ko';

UPDATE golf_course_i18n SET address='Thị trấn Lưu Kiếm, Huyện Thủy Nguyên, Thành phố Hải Phòng' WHERE course_id=48 AND lang='vi';
UPDATE golf_course_i18n SET address='Luu Kiem Town, Thuy Nguyen District, Hai Phong City, Vietnam' WHERE course_id=48 AND lang='en';
UPDATE golf_course_i18n SET address='越南海防市水原县留检镇' WHERE course_id=48 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南海防市水原縣留檢鎮' WHERE course_id=48 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ハイフォン市 トゥイグエン郡 ルーキエム町' WHERE course_id=48 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 하이퐁시 투이응우옌현 루키엠 타운' WHERE course_id=48 AND lang='ko';

UPDATE golf_course_i18n SET address='Phường Ngọc Xuyên, Quận Đồ Sơn, Thành phố Hải Phòng' WHERE course_id=49 AND lang='vi';
UPDATE golf_course_i18n SET address='Ngoc Xuyen Ward, Do Son District, Hai Phong City, Vietnam' WHERE course_id=49 AND lang='en';
UPDATE golf_course_i18n SET address='越南海防市多山区玉川坊' WHERE course_id=49 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南海防市多山區玉川坊' WHERE course_id=49 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ハイフォン市 ドーソン区 ゴックシュエン坊' WHERE course_id=49 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 하이퐁시 도선구 응옥쑤옌동' WHERE course_id=49 AND lang='ko';

UPDATE golf_course_i18n SET address='Tràng Vĩ, Phường Trà Cổ, Thành phố Móng Cái, Tỉnh Quảng Ninh' WHERE course_id=50 AND lang='vi';
UPDATE golf_course_i18n SET address='Trang Vi, Tra Co Ward, Mong Cai City, Quang Ninh Province, Vietnam' WHERE course_id=50 AND lang='en';
UPDATE golf_course_i18n SET address='越南广宁省芒街市茶古坊长尾' WHERE course_id=50 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南廣寧省芒街市茶古坊長尾' WHERE course_id=50 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム クアンニン省 モンカイ市 チャコー坊 チャンヴィ' WHERE course_id=50 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 꽝닌성 몽카이시 짜코동 짱비' WHERE course_id=50 AND lang='ko';

UPDATE golf_course_i18n SET address='Xã Tiền Phong, Huyện Yên Dũng, Tỉnh Bắc Giang' WHERE course_id=51 AND lang='vi';
UPDATE golf_course_i18n SET address='Tien Phong Commune, Yen Dung District, Bac Giang Province, Vietnam' WHERE course_id=51 AND lang='en';
UPDATE golf_course_i18n SET address='越南北江省安勇县前锋乡' WHERE course_id=51 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南北江省安勇縣前鋒鄉' WHERE course_id=51 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム バクザン省 イエンドゥン郡 ティエンフォン村' WHERE course_id=51 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 박장성 옌증현 띠엔퐁 코뮌' WHERE course_id=51 AND lang='ko';

UPDATE golf_course_i18n SET address='Xã Cổ Lũng, Huyện Kim Bảng, Tỉnh Hà Nam' WHERE course_id=52 AND lang='vi';
UPDATE golf_course_i18n SET address='Co Lung Commune, Kim Bang District, Ha Nam Province, Vietnam' WHERE course_id=52 AND lang='en';
UPDATE golf_course_i18n SET address='越南河南省金榜县古隆乡' WHERE course_id=52 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南河南省金榜縣古隆鄉' WHERE course_id=52 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ハナム省 キムバン郡 コルン村' WHERE course_id=52 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 하남성 김방현 꼬룽 코뮌' WHERE course_id=52 AND lang='ko';

UPDATE golf_course_i18n SET address='Xã Minh Quân, Huyện Trấn Yên, Tỉnh Yên Bái' WHERE course_id=53 AND lang='vi';
UPDATE golf_course_i18n SET address='Minh Quan Commune, Tran Yen District, Yen Bai Province, Vietnam' WHERE course_id=53 AND lang='en';
UPDATE golf_course_i18n SET address='越南安沛省镇安县明军乡' WHERE course_id=53 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南安沛省鎮安縣明軍鄉' WHERE course_id=53 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム イエンバイ省 チャンイエン郡 ミンクアン村' WHERE course_id=53 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 옌바이성 쩐옌현 민꾸언 코뮌' WHERE course_id=53 AND lang='ko';

UPDATE golf_course_i18n SET address='Xã Ngũ Chỉ Sơn, Thị xã Sa Pa, Tỉnh Lào Cai' WHERE course_id=54 AND lang='vi';
UPDATE golf_course_i18n SET address='Ngu Chi Son Commune, Sa Pa Town, Lao Cai Province, Vietnam' WHERE course_id=54 AND lang='en';
UPDATE golf_course_i18n SET address='越南老街省沙垻市五指山乡' WHERE course_id=54 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南老街省沙壩市五指山鄉' WHERE course_id=54 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム ラオカイ省 サパ町 ゴチーソン村' WHERE course_id=54 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 라오까이성 사파시 응우찌선 코뮌' WHERE course_id=54 AND lang='ko';

UPDATE golf_course_i18n SET address='Xã Yên Sơn, Huyện Lục Nam, Tỉnh Bắc Giang' WHERE course_id=55 AND lang='vi';
UPDATE golf_course_i18n SET address='Yen Son Commune, Luc Nam District, Bac Giang Province, Vietnam' WHERE course_id=55 AND lang='en';
UPDATE golf_course_i18n SET address='越南北江省禄南县安山乡' WHERE course_id=55 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南北江省祿南縣安山鄉' WHERE course_id=55 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム バクザン省 ルックナム郡 イエンソン村' WHERE course_id=55 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 박장성 룩남현 옌선 코뮌' WHERE course_id=55 AND lang='ko';

UPDATE golf_course_i18n SET address='Xã Minh Tân, Huyện Cẩm Khê, Tỉnh Phú Thọ' WHERE course_id=56 AND lang='vi';
UPDATE golf_course_i18n SET address='Minh Tan Commune, Cam Khe District, Phu Tho Province, Vietnam' WHERE course_id=56 AND lang='en';
UPDATE golf_course_i18n SET address='越南富寿省锦溪县明新乡' WHERE course_id=56 AND lang='zh-CN';
UPDATE golf_course_i18n SET address='越南富壽省錦溪縣明新鄉' WHERE course_id=56 AND lang='zh-TW';
UPDATE golf_course_i18n SET address='ベトナム フート省 カムケ郡 ミンタイン村' WHERE course_id=56 AND lang='ja';
UPDATE golf_course_i18n SET address='베트남 푸토성 깜케현 민떤 코뮌' WHERE course_id=56 AND lang='ko';


"""
cur.executescript(sql)
conn.commit()
conn.close()
print("Đã cập nhật xong address.")
