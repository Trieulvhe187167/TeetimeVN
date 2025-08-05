#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
# Mở kết nối
conn = sqlite3.connect('data/teetimevn_dev.db')
cur = conn.cursor()

# Block cập nhật address cho course_id = 1
sql = """
UPDATE golf_course_i18n
SET overview = '
Tràng An Golf & Country Club tọa lạc tại xã Kỳ Phú, huyện Nho Quan, tỉnh Ninh Bình, cách Hà Nội khoảng 100 km. Sân golf này được thiết kế bởi Golf East (Thái Lan) và chính thức đi vào hoạt động từ tháng 10/2016. Với tổng chiều dài 7.074 yard, sân bao gồm 18 hố par 72 tiêu chuẩn quốc tế, được bao quanh bởi rừng thông và hồ Đồng Chương thơ mộng.

1. Tổng quan & Lịch sử
Sân golf Tràng An được mệnh danh là "Đà Lạt thứ hai" của Việt Nam nhờ vào cảnh quan thiên nhiên hùng vĩ và khí hậu mát mẻ quanh năm. Nơi đây không chỉ là điểm đến lý tưởng cho các golfer mà còn là địa điểm tổ chức các giải đấu và sự kiện golf lớn trong nước.

2. Thiết kế & Cảnh quan
Sân golf được thiết kế hài hòa với thiên nhiên, tận dụng tối đa địa hình tự nhiên với 2 hồ nước, 5 dòng suối và 98 bẫy cát. Các hố golf được bố trí xen kẽ giữa rừng thông, tạo nên thử thách đa dạng cho người chơi ở mọi trình độ.

3. Chất lượng cỏ & Bảo dưỡng
Sân sử dụng hai loại cỏ cao cấp là Champion và Zeon, được chăm sóc theo tiêu chuẩn quốc tế, đảm bảo mặt sân luôn trong tình trạng tốt nhất. Đặc biệt, sân không sử dụng hóa chất trong quá trình bảo dưỡng, góp phần bảo vệ môi trường sinh thái.

4. Cơ sở vật chất & Dịch vụ
Tràng An Golf & Country Club sở hữu nhà câu lạc bộ hiện đại với đầy đủ tiện nghi như phòng thay đồ, nhà hàng Á - Âu, pro-shop, sân tập, và khu vực nghỉ dưỡng. Ngoài ra, sân còn cung cấp các dịch vụ như caddie chuyên nghiệp, cho thuê gậy và xe điện, đáp ứng mọi nhu cầu của golfer.

5. Trải nghiệm & Gợi ý
Đến với Tràng An Golf & Country Club, golfer sẽ được trải nghiệm cảm giác chơi golf giữa thiên nhiên hoang sơ, tận hưởng không khí trong lành và khung cảnh hữu tình. Đặc biệt, sân còn có hệ thống đèn chiếu sáng hiện đại, cho phép chơi golf vào ban đêm.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 44 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = '
Tràng An Golf & Country Club is located in Ky Phu Commune, Nho Quan District, Ninh Binh Province, about 100 km from Hanoi. Designed by Golf East (Thailand), it officially opened in October 2016. With a total length of 7,074 yards, the course comprises 18 international-standard par-72 holes, set amidst pine forests and the picturesque Dong Chuong Lake.

1. Overview & History
Dubbed the “Second Da Lat” of Vietnam for its majestic natural scenery and year-round cool climate, Tràng An Golf Course is not only an ideal destination for golfers but also a venue for major domestic tournaments and events.

2. Design & Scenery
The course is harmoniously integrated with nature, making full use of the terrain with 2 lakes, 5 streams, and 98 sand bunkers. Holes are interspersed among pine groves, offering diverse challenges for players of all skill levels.

3. Turf Quality & Maintenance
Featuring two premium grass types—Champion and Zeon—maintained to international standards, the course always remains in top condition. Notably, no chemicals are used in upkeep, helping to preserve the local ecosystem.

4. Facilities & Services
Tràng An Golf & Country Club boasts a modern clubhouse with amenities such as locker rooms, an Asian-European restaurant, a pro shop, a driving range, and relaxation areas. Additional services include professional caddies, club rentals, and electric carts to meet every golfer''s need.

5. Experience & Recommendations
At Tràng An, golfers can enjoy playing amid pristine nature, breathe in fresh air, and take in the enchanting scenery. A state-of-the-art lighting system even allows for night golf.

6. Reservations
Call (+84) 0123456789 or book your tee time online at TeetimeVn.com for the best offers.
'
WHERE course_id = 44 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
Tràng An 高尔夫乡村俱乐部位于宁平省儒泉县旗富社，距河内约100 公里。该球场由 Golf East（泰国）设计，于2016年10月正式投入运营。场地全长7074码，设有18个国际标准72杆球洞，周围环绕松林和风景如画的同庄湖。

1. 概况与历史
Tràng An 球场因其壮丽的自然景观和全年凉爽的气候，被誉为越南的“第二大叻”。这里不仅是高尔夫爱好者的理想之地，也是国内大型赛事和活动的举办场所。

2. 设计与景观
球场设计与自然和谐共融，充分利用地形特色，拥有2个湖泊、5条溪流和98个沙坑。球洞分布于松林之间，为不同水平的球员提供多样化挑战。

3. 草坪质量与维护
球场采用 Champion 和 Zeon 两种高品质草种，按照国际标准精心维护，确保场地始终处于最佳状态。特别是在维护过程中不使用化学药剂，有助于保护生态环境。

4. 设施与服务
Tràng An 高尔夫乡村俱乐部拥有现代化会所，配备更衣室、亚欧餐厅、专业球具店、练习场及休息区。此外，还提供专业球童、高尔夫球具和电瓶车租赁等服务，满足球员的各项需求。

5. 体验与建议
在 Tràng An，球员可在原生态的自然环境中挥杆，尽享新鲜空气与迷人景致。先进的照明系统更让夜间打球成为可能。

6. 预订
请致电 (+84) 0123456789 或访问 TeetimeVn.com 在线预订发球时段，以获取最佳优惠。
'
WHERE course_id = 44 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
Tràng An 高爾夫鄉村俱樂部位於寧平省儒泉縣旗富社，距河內約100 公里。由 Golf East（泰國）設計，於2016年10月正式開放營運。場地全長7074碼，設有18個國際標準72桿球洞，環繞松林與如畫的同莊湖。

1. 概況與歷史
Tràng An 球場以其壯麗的自然景觀和全年涼爽的氣候被譽為越南的「第二大叻」。這裡不僅是高爾夫愛好者的理想之地，也是國內大型賽事和活動的熱門場地。

2. 設計與景觀
球場設計與自然完美契合，充分發揮地形特色，擁有2個湖泊、5條溪流和98個沙坑。球洞分佈於松林之間，為不同水平的球員帶來多元挑戰。

3. 草皮品質與維護
球場採用 Champion 與 Zeon 兩種頂級草種，依國際標準維護，確保球場始終維持最佳狀態。維護過程中不使用化學藥劑，更加保護當地生態。

4. 設施與服務
Tràng An 高爾夫鄉村俱樂部擁有現代化會所，設有更衣室、亞歐餐廳、專業球具店、打擊場及休憩區。此外，還提供專業球童、高爾夫球具及電動球車借用等貼心服務。

5. 體驗與建議
在 Tràng An，球員可在原始自然中盡情揮桿，享受清新空氣與美景。先進的燈光系統亦可支持夜間高爾夫。

6. 預訂
請撥打 (+84) 0123456789 或前往 TeetimeVn.com 線上預訂，享受最優惠方案。
'
WHERE course_id = 44 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
Tràng An ゴルフ＆カントリークラブは、ニンビン省ニョクアン県キー・フー村に位置し、ハノイから約100 kmの距離にあります。タイの Golf East 社が設計し、2016年10月に正式オープンしました。全長7,074ヤードのコースは、国際基準のパー72×18ホールで構成されており、松林と風光明媚なドンチュオン湖に囲まれています。

1. 概要と歴史
壮大な自然景観と年間を通じた涼しい気候から「ベトナムの第二のダラット」と呼ばれています。ゴルファーの理想的なスポットであると同時に、国内主要大会やイベントの開催地としても有名です。

2. 設計と景観
コースは自然との調和を重視し、2つの池、5本の小川、98のバンカーを巧みに配置。松林の中にホールが点在し、あらゆるレベルのプレーヤーに多彩なチャレンジを提供します。

3. 芝質とメンテナンス
Champion種と Zeon種という高品質の芝を国際基準で管理し、常にベストコンディションを維持。化学薬品を使用しないメンテナンスで環境保護にも配慮しています。

4. 施設とサービス
ロッカールーム、アジアン・ヨーロピアンレストラン、プロショップ、練習場、リラクゼーションエリアなどを備えたモダンなクラブハウスを完備。プロキャディやクラブ・カートのレンタルサービスも充実しています。

5. 体験とおすすめ
手つかずの大自然の中でプレーし、澄んだ空気と美しい風景を満喫できます。最新の照明システムによりナイトゴルフも可能です。

6. 予約
(+84) 0123456789 までお電話いただくか、TeetimeVn.com でオンライン予約をご利用ください。
'
WHERE course_id = 44 AND lang = 'ja';

UPDATE golf_course_i18n
SET overview = '
Tràng An 골프 & 컨트리 클럽은 닌빈성 녀오꽝현 기푸 지역에 위치하며, 하노이에서 약 100 km 거리에 있습니다. 태국의 Golf East 사가 설계했으며, 2016년 10월에 공식 개장했습니다. 총 길이 7,074야드의 코스는 국제 표준 파72 18홀로 구성되며, 소나무 숲과 경치 좋은 동쭝 호수에 둘러싸여 있습니다。

1. 개요 및 역사
장엄한 자연 경관과 연중 시원한 기후 덕분에 ‘베트남의 두 번째 달랏''으로 불립니다. 골프 애호가들에게 이상적인 장소일 뿐만 아니라 국내 주요 대회 및 이벤트의 개최지로도 유명합니다。

2. 설계 및 경관
코스는 자연과의 조화를 이루도록 설계되었으며, 2개의 호수、5개의 개울、98개의 벙커를 활용해 지형을 최대한 살렸습니다。홀들은 소나무 숲 사이에 배치되어 다양한 실력의 플레이어에게 도전 과제를 제공합니다。

3. 잔디 품질 및 유지 관리
Champion과 Zeon 두 가지 고급 잔디를 국제 기준에 따라 관리하여 항상 최상의 상태를 유지합니다。특히 유지 관리 과정에서 화학 물질을 사용하지 않아 환경 보호에도 기여합니다。

4. 시설 및 서비스
라커룸、아시아-유럽 레스토랑、프로숍、연습장、휴식 공간 등을 갖춘 현대적인 클럽하우스를 보유하고 있습니다。전문 캐디、클럽 및 전기 카ート 대여 서비스도 제공하여 골퍼들의 모든 요구를 충족합니다。

5. 체험 및 추천
순수 자연 속에서 골프를 즐기며 상쾌한 공기와 아름다운 경치를 만끽할 수 있습니다。최신 조명 시스템으로 야간 골프도 가능합니다。

6. 예약
(+84) 0123456789로 전화하시거나 TeetimeVn.com에서 온라인 티타임을 예약하여 최상의 혜택을 누리세요。
'
WHERE course_id = 44 AND lang = 'ko';


UPDATE golf_course_i18n
SET overview = '
Sân Golf Hoàng Gia (Royal Golf Club) nằm tại xã Yên Thắng, huyện Yên Mô, tỉnh Ninh Bình, cách Hà Nội khoảng 100 km. Với tổng diện tích 670 ha, sân bao gồm ba sân 18 hố: King''s Hill, Queen''s Course và Prince''s Course. Được thiết kế bởi Nicklaus Design và P&Z Development, sân chính thức khai trương vào năm 2010 và nhanh chóng trở thành điểm đến hàng đầu cho golfer trong và ngoài nước.

1. Tổng quan & Lịch sử
Sân Golf Hoàng Gia là sân golf 54 hố đầu tiên tại miền Bắc Việt Nam, tọa lạc gần các danh thắng nổi tiếng như Tràng An, Tam Cốc – Bích Động và chùa Bái Đính. Với cảnh quan thiên nhiên hùng vĩ và thiết kế đẳng cấp quốc tế, sân đã tổ chức nhiều giải đấu chuyên nghiệp và là điểm đến yêu thích của cộng đồng golfer.

2. Thiết kế & Cảnh quan
– King''s Hill: Sân đầu tiên, dài 7.267 yard, nổi bật với hố số 2 – par 3, green nằm trên đảo giữa hồ, tạo thử thách độc đáo.  
– Queen''s Course: Thiết kế bởi Jack Nicklaus, dài 7.265 yard, nổi bật với hố số 4 – par 4, tee đặt trên đồi nhỏ, fairway hẹp với hai bên là dãy đá vôi.  
– Prince''s Course: Đang trong quá trình hoàn thiện, hứa hẹn mang đến trải nghiệm mới lạ cho golfer.

3. Chất lượng sân cỏ & Bảo dưỡng
Sân sử dụng cỏ Zeon Zoysia cho fairway và Primo Zoysia cho green, nhập khẩu từ Thái Lan, đảm bảo bề mặt chơi mượt mà và ổn định. Hệ thống tưới tiêu hiện đại và đội ngũ bảo dưỡng chuyên nghiệp giúp duy trì chất lượng sân theo tiêu chuẩn quốc tế.

4. Cơ sở vật chất & Dịch vụ
Nhà câu lạc bộ rộng 10.000 m², tọa lạc trên đỉnh núi đá, cung cấp đầy đủ tiện nghi: phòng thay đồ, pro-shop, nhà hàng Á – Âu, khu giải trí, spa, phòng tập gym và khách sạn 12 phòng sang trọng. Khu resort "Công chúa" với các biệt thự cao cấp, thiết kế hài hòa với thiên nhiên, mang đến trải nghiệm nghỉ dưỡng đẳng cấp.

5. Trải nghiệm & Gợi ý
Chơi golf tại Sân Golf Hoàng Gia, golfer sẽ được hòa mình vào thiên nhiên với khung cảnh núi đá vôi triệu năm tuổi, hồ Yên Thắng rộng 185 ha và không khí trong lành. Đặc biệt, sân có hệ thống đèn chiếu sáng hiện đại, cho phép chơi golf vào ban đêm.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất. 
'
WHERE course_id = 45 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = '
Royal Golf Club is located in Yen Thang Commune, Yen Mo District, Ninh Binh Province, about 100 km from Hanoi. Covering an area of 670 ha, the facility comprises three 18-hole courses: King''s Hill, Queen''s Course, and Prince''s Course. Designed by Nicklaus Design and P&Z Development, it officially opened in 2010 and quickly became a top destination for both domestic and international golfers.

1. Overview & History  
Royal Golf Club is the first 54-hole golf facility in northern Vietnam, situated near famous attractions such as Trang An, Tam Coc – Bich Dong, and Bai Dinh Pagoda. With its majestic natural landscape and world-class design, the club has hosted numerous professional tournaments and is a favorite among the golfing community.

2. Design & Scenery  
– King''s Hill: The first course, 7,267 yards long, highlighted by hole No. 2 – a par-3 with the green on an island in the lake, creating a unique challenge.  
– Queen''s Course: Designed by Jack Nicklaus, 7,265 yards long, notable for hole No. 4 – a par-4 with the tee on a small hill and a narrow fairway flanked by limestone formations.  
– Prince''s Course: Currently under completion, promising a fresh experience for golfers.

3. Turf Quality & Maintenance  
Fairways use Zeon Zoysia grass and greens use Primo Zoysia, both imported from Thailand, ensuring a smooth and consistent playing surface. A modern irrigation system and professional maintenance team keep conditions to international standards.

4. Facilities & Services  
The 10,000 m² clubhouse sits atop a limestone hill and offers full amenities: locker rooms, a pro shop, an Asian-European restaurant, entertainment areas, a spa, a gym, and 12 luxury hotel rooms. The “Princess” resort area features high-end villas harmonized with nature for a premium stay.

5. Experience & Recommendations  
Golfers at Royal Golf Club immerse themselves in million-year-old limestone scenery, the 185-ha Yen Thang Lake, and fresh air. Advanced lighting even allows night golf.

6. Reservations  
Call (+84) 0123456789 or book online at TeetimeVn.com for the best offers.
'
WHERE course_id = 45 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
皇家高尔夫俱乐部位于宁平省应胜社、应谋县，距河内约100公里。球场占地670公顷，由三座18洞球场组成：王丘球场、女王球场和王子球场。由Nicklaus Design和P&Z Development设计，2010年正式开业，迅速成为国内外高尔夫爱好者的首选目的地。

1. 概况与历史  
皇家高尔夫俱乐部是越南北部首个54洞高尔夫设施，毗邻长安、三谷碧洞和白顶寺等著名景点。凭借壮丽自然风光和国际级设计，球场举办了众多职业赛事，深受高尔夫社区喜爱。

2. 设计与景观  
– 王丘球场：首座球场，全长7,267码，以第2洞著称——果岭位于湖中小岛，挑战独特。  
– 女王球场：由杰克·尼克劳斯设计，全长7,265码，第4洞为一4杆洞，发球台设于小丘，窄长球道两侧为石灰岩。  
– 王子球场：正在建设中，承诺带来全新体验。

3. 草坪质量与维护  
球道采用Zeon Zoysia，果岭采用Primo Zoysia，均自泰国进口，确保平滑稳定的球面。现代灌溉系统和专业维护团队将球场维护至国际标准。

4. 设施与服务  
会所面积10,000平方米，坐落于石灰岩丘顶，提供更衣室、专业球具店、亚欧餐厅、娱乐区、水疗中心、健身房和12间豪华客房。“公主”度假区拥有高端别墅，与自然和谐融合，带来尊贵体验。

5. 体验与建议  
在皇家高尔夫俱乐部，可感受千万年石灰岩地貌、185公顷应胜湖和清新空气。先进灯光系统亦可支持夜间高尔夫。

6. 预订  
请致电 (+84) 0123456789 或访问 TeetimeVn.com 在线预订，以获取最佳优惠。
'
WHERE course_id = 45 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
皇家高爾夫俱樂部位於寧平省應勝社、應謀縣，距河內約100公里。球場佔地670公頃，由三座18洞球場組成：王丘球場、女王球場和王子球場。由Nicklaus Design與P&Z Development設計，於2010年正式開幕，迅速成為國內外高爾夫愛好者的首選。

1. 概況與歷史  
皇家高爾夫俱樂部是越南北部首座54洞高爾夫設施，鄰近長安、三谷碧洞及拜頂寺等著名景點。憑藉壯麗自然景觀與國際級設計，承辦多場職業賽事，深受球手青睞。

2. 設計與景觀  
– 王丘球場：首座球場，全長7,267碼，以第2洞聞名——果嶺位於湖中小島，挑戰獨特。  
– 女王球場：由傑克·尼克勞斯設計，全長7,265碼，第4洞為一4桿洞，發球台設於小丘，球道兩側為石灰岩。  
– 王子球場：正在建設中，承諾帶來全新體驗。

3. 草皮品質與維護  
球道採用Zeon Zoysia，果嶺採Primo Zoysia，皆自泰國進口，確保平滑穩定球面。現代灌溉系統與專業養護團隊將球場維護至國際標準。

4. 設施與服務  
會所面積10,000平方米，位於石灰岩丘頂，設有更衣室、專業球具店、亞歐餐廳、娛樂區、SPA、水療、健身房及12間豪華客房。公主度假區高端別墅與自然融合，締造尊貴度假體驗。

5. 體驗與建議  
在皇家高爾夫俱樂部，球手可沉浸於千萬年石灰岩地貌、185公頃應勝湖與清新空氣中。先進燈光系統亦支持夜間高爾夫。

6. 預訂  
請撥打 (+84) 0123456789 或前往 TeetimeVn.com 線上預訂，以獲取最佳優惠。
'
WHERE course_id = 45 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
ロイヤルゴルフクラブ（Royal Golf Club）は、ニンビン省イェンモー県イェンタイン村に位置し、ハノイから約100km離れています。敷地面積670haで、キングスヒル、クイーンズコース、プリンセスコースの3つの18ホールコースで構成されています。Nicklaus DesignとP&Z Developmentが設計し、2010年に正式オープン、国内外のゴルファーにとって有数の目的地となりました。

1. 概要と歴史  
北部ベトナム初の54ホール施設で、チャンアン、タムコック-ビックドン、バイディン寺院などの名所近くにあります。壮大な自然景観と国際基準の設計により、数多くのプロトーナメントを開催し、愛好者に人気です。

2. 設計と景観  
– キングスヒル：全長7,267ヤード。第2ホール（パー3）は湖上の島グリーンが特徴で、ユニークな挑戦を提供します。  
– クイーンズコース：ジャック・ニクラウス設計、全長7,265ヤード。第4ホール（パー4）は小丘のティーイングエリアと両側の石灰岩地形が特徴です。  
– プリンセスコース：現在建設中で、新たな体験を約束します。

3. 芝質とメンテナンス  
フェアウェイはZeon Zoysia、グリーンはPrimo Zoysiaを使用し、タイから輸入。最新の灌漑システムとプロのメンテナンスで国際基準を維持します。

4. 施設とサービス  
1万㎡のクラブハウスにはロッカールーム、プロショップ、アジアン・ヨーロピアンレストラン、エンターテインメントエリア、スパ、ジム、12室の豪華ホテルルームが揃っています。「プリンセス」リゾートエリアには高級ヴィラが点在し、自然と調和した滞在を提供。

5. 体験とおすすめ  
千万年の石灰岩地形と185haのイェンタイン湖、澄んだ空気に包まれてプレー可能。最新照明でナイトゴルフも楽しめます。

6. 予約  
(+84) 0123456789までお電話、またはTeetimeVn.comでオンライン予約をどうぞ。
'
WHERE course_id = 45 AND lang = 'ja';

UPDATE golf_course_i18n
SET overview = '
로열 골프 클럽(Royal Golf Club)은 닌빈성 옌모현 옌탱 마을에 위치하며, 하노이에서 약 100km 떨어져 있습니다. 총 면적 670ha에 킹스힐(King''s Hill), 퀸스코스(Queen''s Course), 프린스코스(Prince''s Course)의 3개 18홀 코스로 구성되어 있습니다. Nicklaus Design과 P&Z Development가 설계했으며, 2010년 공식 개장 후 국내외 골퍼들의 최고 명소로 자리 잡았습니다.

1. 개요 및 역사  
이 클럽은 북부 베트남 최초의 54홀 골프 시설로, 짱안(Trang An), 탐콕–빅동(Tam Coc–Bich Dong), 바이딩 사원(Bai Dinh Pagoda) 등 유명 관광지 인근에 위치합니다. 웅장한 자연 경관과 국제 수준의 설계로 수많은 프로 토너먼트를 개최하였고, 골퍼들의 사랑을 받고 있습니다.

2. 코스 설계 및 경관  
– 킹스힐: 첫 번째 코스로 전체 길이 7,267야드. 2번 홀(파3)은 호수 중앙의 섬 그린이 특징으로 독특한 도전을 제공합니다.  
– 퀸스코스: 잭 니클라우스(Jack Nicklaus) 설계, 길이 7,265야드. 4번 홀(파4)은 작은 언덕 위의 티잉 구역과 양측의 석회암 지형이 특징입니다.  
– 프린스코스: 현재 공사 중이며 골퍼들에게 새로운 경험을 약속합니다.

3. 잔디 품질 및 유지 관리  
페어웨이는 Zeon Zoysia, 그린은 Primo Zoysia를 사용하며 모두 태국에서 수입된 고품질 잔디입니다. 최첨단 관개 시스템과 전문 유지 관리 팀이 국제 기준의 코스 컨디션을 유지합니다.

4. 시설 및 서비스  
클럽하우스는 10,000㎡ 규모로 라커룸, 프로숍, 아시안-유러피언 레스토랑, 엔터테인먼트 구역, 스파, 헬스장, 12개의 고급 객실을 갖추고 있습니다. “프린세스” 리조트 구역에는 고급 빌라가 조성되어 자연과 어우러진 럭셔리한 휴양을 제공합니다.

5. 경험 및 추천  
수백만 년 된 석회암 지형과 185ha 규모의 옌탱 호수, 맑은 공기 속에서 라운드를 즐길 수 있습니다. 최첨단 조명 시스템으로 야간 골프도 가능합니다.

6. 예약  
(+84) 0123456789로 전화하시거나 TeetimeVn.com에서 온라인 티타임을 예약하여 최상의 혜택을 누리세요.
'
WHERE course_id = 45 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = '
Dragon Golf Links tọa lạc tại Khu du lịch Quốc tế Đồi Rồng, phường Vạn Hương, quận Đồ Sơn, Hải Phòng – cách trung tâm thành phố khoảng 25 phút lái xe và sân bay Cát Bi khoảng 20 phút. Sân golf ven biển 27 hố này được thiết kế bởi Greg Norman và chính thức khai trương vào tháng 3 năm 2023, mang đến trải nghiệm golf độc đáo giữa khung cảnh biển cả và núi rừng.

1. Tổng quan & Lịch sử  
Dragon Golf Links là sân golf ven biển đầu tiên tại Việt Nam, được đầu tư hơn 2.000 tỷ đồng, nhanh chóng trở thành điểm đến ưa chuộng của golfer trong và ngoài nước nhờ thiết kế đẳng cấp và cảnh quan ngoạn mục.

2. Thiết kế & Cảnh quan  
– Sân gồm ba cụm 9 hố với fairway dài, bunker cát trắng mịn và đường bóng ven biển.  
– Các hố 6, 7, 8, 12, 13, 14 nằm song song và vuông góc với biển, mang đến tầm nhìn panorama 360° và thử thách gió biển.  
– Thảm cỏ xanh mướt hòa quyện cùng biển cả, tạo nên bản sắc links độc đáo.

3. Chất lượng sân cỏ & Bảo dưỡng  
Cỏ fairway và green được chọn lọc chất lượng cao, được bảo dưỡng theo tiêu chuẩn quốc tế với hệ thống tưới tiêu tự động và đội ngũ chăm sóc chuyên nghiệp, đảm bảo mặt sân luôn mượt mà và ổn định.

4. Cơ sở vật chất & Dịch vụ  
– Nhà câu lạc bộ rộng gần 5.000 m², thiết kế hiện đại lấy cảm hứng hình rồng, với locker cao cấp, phòng tắm, khu xông hơi khô/ướt và pro-shop đa dạng.  
– Khu sân tập rộng 8 ha với 25 làn tập, thảm cỏ tự nhiên và tầm nhìn biển mở rộng, mang đến trải nghiệm luyện tập chuyên nghiệp.

5. Trải nghiệm & Gợi ý  
– Sáng sớm: tận hưởng không khí trong lành và bình minh rực rỡ trên biển.  
– Chiều muộn: ngắm hoàng hôn từ tee box ven biển.  
– Sau vòng golf: thư giãn tại nhà hàng hoặc spa trong khu nghỉ dưỡng Dream Dragon.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 46 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = '
Dragon Golf Links is located in the Dragon Hill International Tourism Area, Van Huong Ward, Do Son District, Hai Phong—about a 25-minute drive from the city center and 20 minutes from Cat Bi Airport. This 27-hole seaside course was designed by Greg Norman and officially opened in March 2023, offering a unique golfing experience amid ocean and mountain scenery.

1. Overview & History  
Dragon Golf Links is Vietnam''s first seaside golf course, with over VND 2,000 billion in investment, quickly becoming a preferred destination for domestic and international golfers thanks to its world-class design and spectacular landscape.

2. Design & Scenery  
– The course comprises three 9-hole loops with long fairways, fine white sand bunkers, and seaside tee lines.  
– Holes 6, 7, 8, 12, 13, and 14 run parallel or perpendicular to the sea, offering 360° panoramic ocean views and wind challenges.  
– Lush green turf blending with the sea creates a distinct links identity.

3. Turf Quality & Maintenance  
Fairway and greens use high-quality turf, maintained to international standards with automatic irrigation and a professional care team, ensuring a smooth, consistent playing surface.

4. Facilities & Services  
– The clubhouse spans nearly 5,000 m² with a modern dragon-inspired design, premium lockers, showers, dry/wet saunas, and a well-stocked pro shop.  
– The 8-ha driving range with 25 bays features natural turf and expansive sea views for professional practice.

5. Experience & Recommendations  
– Early morning: enjoy fresh air and a stunning sunrise over the sea.  
– Late afternoon: watch the sunset from the seaside tee.  
– After your round: relax at the on-site restaurant or spa within the Dream Dragon resort.

6. Reservations  
Call (+84) 0123456789 or book your tee time online at TeetimeVn.com for the best offers.
'
WHERE course_id = 46 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
Dragon Golf Links位于海防市多山区万香街道龙山国际旅游区，距市中心约25分钟车程，距Cat Bi机场约20分钟。该27洞海滨球场由Greg Norman设计，于2023年3月正式开业，提供海洋与山岳相映成趣的独特高尔夫体验。

1. 概况与历史  
Dragon Golf Links是越南首个海滨高尔夫球场，投资逾20亿越盾，凭借世界级设计与壮观景观迅速成为国内外球手的首选目的地。

2. 设计与景观  
– 球场由三段9洞环组成，配有长球道、细白沙坑和海边发球区。  
– 第6、7、8、12、13、14号洞沿海平行或垂直布局，360°全海景与海风挑战并存。  
– 翠绿草坪与大海交融，打造独特links风格。

3. 草坪品质与维护  
球道和果岭采用高品质草种，配备自动灌溉系统和专业养护团队，按国际标准维护，确保球面平顺稳定。

4. 设施与服务  
– 近5,000 m²的会所以现代龙形设计为特色，设有高级储物柜、淋浴、干/湿桑拿及齐全的pro-shop。  
– 占地8 ha、拥有25个练习位的练习场，天然草皮与开阔海景为专业练习提供最佳环境。

5. 体验与建议  
– 清晨：感受海风拂面与壮丽日出。  
– 傍晚：在海边发球台观赏迷人落日。  
– 球局结束后：在Dream Dragon度假区的餐厅或SPA放松身心。

6. 预订  
请致电(+84)0123456789或登录TeetimeVn.com在线预订，尊享最佳优惠。
'
WHERE course_id = 46 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
Dragon Golf Links位於海防市多山區萬香街道龍山國際旅遊區，距市中心約25分鐘車程，距Cat Bi機場約20分鐘。此27洞海濱球場由Greg Norman設計，於2023年3月正式開幕，帶來海洋與山嶺交織的獨特高爾夫體驗。

1. 概況與歷史  
Dragon Golf Links是越南首座海濱高爾夫球場，投資逾20億越盾，憑藉世界級設計及壯觀景致迅速成為國內外球手的首選。

2. 設計與景觀  
– 球場由三段9洞環組成，配備長球道、細白沙坑及海邊開球區。  
– 第6、7、8、12、13、14號洞與海岸平行或垂直佈局，可360°欣賞海景並迎戰海風。  
– 翠綠草坪與大海融合，塑造獨特links風格。

3. 草皮品質與維護  
球道與果嶺採用高品質草種，引進自國際，配合自動灌溉系統與專業維護團隊，保證球面平順穩定。

4. 設施與服務  
– 近5,000 m²的新古典龍形會所，設有高檔儲物櫃、淋浴、乾/濕蒸氣室及專業球具店。  
– 占地8 ha的練習場擁有25個練習位，天然草皮與寬闊海景相得益彰，為專業練習提供理想場地。

5. 體驗與建議  
– 清晨：迎接清新海風與壯麗日出。  
– 黃昏：在海邊發球台觀賞落日餘暉。  
– 球局結束後：於Dream Dragon度假區內餐廳或SPA放鬆身心。

6. 預訂  
請撥打(+84)0123456789或訪問TeetimeVn.com線上預訂，享受尊貴優惠。
'
WHERE course_id = 46 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
Dragon Golf Linksはハイフォン市ドーソン区バンフーン坊のドラゴンヒル国際リゾートエリアに位置し、市中心部から車で約25分、カットビ空港から約20分です。この27ホールのシーサイドコースはGreg Normanが設計し、2023年3月に正式オープン、海と山の絶景を望むユニークなゴルフ体験を提供します。

1. 概要と歴史  
Dragon Golf Linksはベトナム初のシーサイドゴルフコースで、20億ドン以上の投資を受け、世界クラスの設計と壮大な景観により国内外のゴルファーから高い評価を得ています。

2. 設計と景観  
– 3つの9ホールループで構成され、長いフェアウェイ、細かい白砂のバンカー、シーサイドのティーイングエリアが特色です。  
– 6、7、8、12、13、14番ホールは海岸線に平行または直角に配置され、360°のパノラマビューと海風チャレンジを楽しめます。  
– 青々とした芝と海が調和し、独特のリンクスコースらしさを演出します。

3. 芝質とメンテナンス  
フェアウェイとグリーンには高品質芝を使用し、自動灌漑システムとプロのメンテナンスチームにより国際基準で管理します。

4. 施設とサービス  
– 約5,000㎡のクラブハウスはドラゴンをモチーフにしたモダンなデザインで、プレミアムロッカー、シャワー、ドライ／ウェットサウナ、充実のプロショップを完備。  
– 8ヘクタールのドライビングレンジには25打席があり、天然芝と広大な海景がプロ練習に最適です。

5. 体験とおすすめ  
– 早朝：新鮮な海風と美しい日の出を堪能。  
– 夕方：シーサイドティーからのサンセットビュー。  
– ラウンド後：Dream Dragonリゾート内のレストランやスパでリラックス。

6. 予約  
(+84)0123456789までお電話、またはTeetimeVn.comでオンライン予約をどうぞ。
'
WHERE course_id = 46 AND lang = 'ja';

UPDATE golf_course_i18n
SET overview = '
Dragon Golf Links는 하이퐁시 도손구 반훙동 드래곤힐 국제관광지구에 위치하며, 시내에서 차로 약 25분, 캇비 공항에서 약 20분 거리에 있습니다. 이 27홀 시사이드 코스는 Greg Norman이 설계했으며, 2023년 3월 정식 개장하여 바다와 산의 장관 속에서 특별한 골프 경험을 제공합니다.

1. 개요 및 역사  
Dragon Golf Links는 베트남 최초의 시사이드 골프 코스로, 20억 동 이상의 투자가 이루어졌으며, 세계적 수준의 설계와 웅장한 경관으로 국내외 골퍼들에게 빠르게 사랑받았습니다.

2. 설계 및 경관  
– 3개의 9홀 루프로 구성되어 있으며, 긴 페어웨이, 고운 백사장 벙커, 시사이드 티잉 구역이 특징입니다.  
– 6, 7, 8, 12, 13, 14번 홀은 해안선과 평행 또는 직각으로 배치되어 360° 파노라마 바다 뷰와 해풍 도전을 제공합니다.  
– 푸른 잔디와 바다가 어우러져 독특한 링크스 코스 매력을 자아냅니다.

3. 잔디 품질 및 유지 관리  
페어웨이와 그린에는 고품질 잔디를 사용하며, 자동 관개 시스템과 전문 관리 팀이 국제 표준에 맞춰 유지 관리합니다.

4. 시설 및 서비스  
– 약 5,000㎡ 규모의 클럽하우스는 드래곤에서 영감을 받은 모던한 디자인으로 고급 락커, 샤워실, 드라이/웻 사우나 및 프로숍을 갖추고 있습니다.  
– 8헥타르 규모의 드라이빙 레인지에는 25개의 타석이 있으며, 천연 잔디와 탁 트인 바다 경관이 더해져 전문적인 연습 환경을 제공합니다.

5. 경험 및 추천  
– 이른 아침: 신선한 바닷바람과 황홀한 일출 감상.  
– 늦은 오후: 시사이드 티에서 감상하는 석양.  
– 라운드 후: Dream Dragon 리조트 내 레스토랑이나 스파에서 휴식.

6. 예약  
(+84)0123456789로 전화하거나 TeetimeVn.com에서 온라인 예약하세요.
'
WHERE course_id = 46 AND lang = 'ko';


UPDATE golf_course_i18n
SET overview = '
Vinpearl Golf Hải Phòng tọa lạc trên Đảo Vũ Yên, quận Hải An, TP. Hải Phòng – cách trung tâm thành phố khoảng 15 km và sân bay Cát Bi 10 km. Khu resort bao gồm hai sân 18 hố par-72 (Lakeside và Marshland) do IMG Worldwide thiết kế và chính thức khai trương năm 2019, mang đến trải nghiệm golf nghỉ dưỡng đẳng cấp bên bờ vịnh.

1. Tổng quan & Lịch sử  
Vinpearl Golf Hải Phòng là một phần của hệ sinh thái nghỉ dưỡng Vinpearl, nhanh chóng thu hút golfer nhờ cảnh quan hồ nước mênh mông, không gian xanh mát và dịch vụ chuyên nghiệp.

2. Thiết kế & Cảnh quan  
– Lakeside: fairway uốn quanh hồ nước rộng lớn, điểm nhấn là các bunker trắng và đảo cát ấn tượng.  
– Marshland: fairway chạy qua đầm lầy tự nhiên, tạo cảm giác hoang sơ và thử thách với đường bóng thay đổi độ cao.

3. Chất lượng sân cỏ & Bảo dưỡng  
Fairway cỏ Platinum Paspalum, green cỏ TifEagle Bermuda được chăm sóc theo tiêu chuẩn USGA, hệ thống tưới tự động và đội ngũ greenskeeping chuyên nghiệp duy trì mặt sân luôn mượt mà.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại với locker cao cấp, pro-shop, nhà hàng Á-Âu, khu vực training (driving range, putting green), spa và hồ bơi. Bên cạnh đó, dịch vụ caddie chuyên nghiệp và khoá học golf với huấn luyện viên PGA đáp ứng mọi nhu cầu.

5. Trải nghiệm & Gợi ý  
– Khi bình minh vừa ló rạng: tận hưởng không khí trong lành và cảnh hồ yên ả.  
– Lúc hoàng hôn: ngắm những tia nắng cuối ngày chiếu rọi lên mặt nước và fairway.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 47 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = '
Vinpearl Golf Hai Phong is located on Vu Yen Island, Hai An District, Hai Phong City—about 15 km from the city center and 10 km from Cat Bi Airport. The resort features two 18-hole par-72 courses (Lakeside and Marshland) designed by IMG Worldwide and officially opened in 2019, offering a premium bay-side golf experience.

1. Overview & History
Vinpearl Golf Hai Phong is part of the Vinpearl resort ecosystem, quickly attracting golfers with its expansive water vistas, lush green spaces, and professional service.

2. Design & Scenery
– Lakeside: fairways that wind around a large lake, highlighted by white sand bunkers and dramatic island greens.  
– Marshland: fairways that traverse natural marshes, creating a wild atmosphere and challenge with varied elevations.

3. Turf Quality & Maintenance
Fairways use Platinum Paspalum grass and greens use TifEagle Bermuda, maintained to USGA standards with automatic irrigation and a dedicated greenskeeping team to ensure consistently smooth playing surfaces.

4. Facilities & Services
A modern clubhouse of nearly 5,000 m² with premium lockers, a pro shop, an Asian-European restaurant, training facilities (driving range, putting green), a spa, and a swimming pool. Professional caddie services and PGA-coach lessons are also available to meet every golfer''s needs.

5. Experience & Recommendations
– At dawn: enjoy fresh air and the tranquil morning light over the lake.  
– At sunset: watch the last golden rays reflect off the water and fairways.

6. Reservations
Call (+84) 0123456789 or book online at TeetimeVn.com for the best offers.
'
WHERE course_id = 47 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
Vinpearl Golf Hải Phòng位于海防市海安区Vũ Yên岛，距市中心约15公里，距Cat Bi机场10公里。度假区包括两座18洞72杆球场（Lakeside与Marshland），由IMG Worldwide设计，2019年正式开业，为海湾边带来高端高尔夫度假体验。

1. 概况与历史  
Vinpearl Golf Hải Phòng是Vinpearl度假生态圈的一部分，以广阔水景、清凉绿色空间及专业服务迅速吸引了众多球手。

2. 设计与景观  
– Lakeside：球道环绕湖泊，白色沙坑与岛式果岭相映成趣。  
– Marshland：球道穿越天然沼泽，地形起伏带来原始挑战。

3. 草坪质量与维护  
球道采用Platinum Paspalum草，果岭采用TifEagle Bermuda草，按USGA标准维护，自动灌溉系统与专业维护团队确保球面始终平滑。

4. 设施与服务  
近5,000平方米现代会所，配备高级储物柜、专业球具店、亚欧餐厅、练习场（球道练习区、推杆练习区）、SPA与泳池。专业球童及PGA教练课程完美满足球手需求。

5. 体验与建议  
– 拂晓：呼吸清新空气，欣赏宁静湖畔晨光。  
– 黄昏：观赏余晖映照下的水面与球道。

6. 预订  
请致电(+84) 0123456789或访问TeetimeVn.com在线预订，尊享优惠。
'
WHERE course_id = 47 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
Vinpearl Golf Hải Phòng位於海防市海安區Vũ Yên島，距市中心約15公里，距Cat Bi機場10公里。度假區包括兩座18洞72桿球場（Lakeside與Marshland），由IMG Worldwide設計，2019年正式開幕，為海灣邊帶來高端高爾夫度假體驗。

1. 概況與歷史  
Vinpearl Golf Hải Phòng是Vinpearl度假生態圈的一部分，以廣闊水景、清涼綠地及專業服務迅速吸引眾多球手。

2. 設計與景觀  
– Lakeside：球道環繞湖泊，白色沙坑與島式果嶺相映成趣。  
– Marshland：球道穿越天然沼澤，地形起伏帶來原始挑戰。

3. 草皮品質與維護  
球道採用Platinum Paspalum草，果嶺採用TifEagle Bermuda草，按USGA標準維護，自動灌溉系統與專業養護團隊確保球面始終平滑。

4. 設施與服務  
近5,000平方米現代會所，配備高檔儲物櫃、專業球具店、亞歐餐廳、練習場（遠距練習區、推桿練習區）、SPA及泳池。專業球童與PGA教練課程完美滿足球手需求。

5. 體驗與建議  
– 曙光：呼吸清新空氣，欣賞寧靜湖畔晨光。  
– 黃昏：觀賞餘暉映照下的水面與球道。

6. 預訂  
請撥打(+84) 0123456789或訪問TeetimeVn.com線上預訂，尊享優惠。
'
WHERE course_id = 47 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
Vinpearl Golf Hải Phòngはハイフォン市ハイアン区のVu Yen島に位置し、市中心部から約15km、カットビ空港から約10kmの距離です。リゾートにはIMG Worldwideが設計した18ホール・パー72コースが2つ（LakesideとMarshland）あり、2019年に正式オープン。湾岸でのラグジュアリーなゴルフリゾート体験を提供します。

1. 概要と歴史  
Vinpearl Golf Hải PhòngはVinpearlリゾートの一部であり、広大な水景、涼やかな緑地、プロフェッショナルなサービスで多くのゴルファーを魅了しています。

2. 設計と景観  
– Lakeside：大きな湖を取り囲むフェアウェイと白いバンカー、そして島グリーンが特徴。  
– Marshland：天然の湿地を貫くフェアウェイで、起伏のある地形が野趣あふれるチャレンジを演出。

3. 芝質とメンテナンス  
フェアウェイはPlatinum Paspalum、グリーンはTifEagle Bermudaを使用し、USGA基準の自動灌漑システムと専任チームで常に滑らかな状態を維持。

4. 施設とサービス  
約5,000㎡のモダンなクラブハウスには高級ロッカー、プロショップ、アジアン‐ヨーロピアンレストラン、ドライビングレンジ、パッティンググリーン、スパ、プールを完備。プロキャディやPGAコーチによるレッスンも提供。

5. 体験とおすすめ  
– 明け方：新鮮な空気と穏やかな湖面の朝焼けを満喫。  
– 夕暮れ：海辺のティーグラウンドから美しいサンセットを堪能。

6. 予約  
(+84) 0123456789までお電話、またはTeetimeVn.comでオンライン予約をどうぞ。
'
WHERE course_id = 47 AND lang = 'ja';

UPDATE golf_course_i18n
SET overview = '
Vinpearl Golf Hải Phòng은 하이퐁시 하이안구 Vu Yen 섬에 위치하며, 도심에서 약 15km, 캇비 공항에서 약 10km 거리에 있습니다. 이 리조트에는 IMG Worldwide가 설계한 파72 18홀 코스 두 개(Lakeside 및 Marshland)가 있으며, 2019년에 공식 개장하여 만찬 같은 만경을 자랑합니다.

1. 개요 및 역사  
Vinpearl Golf Hải Phòng은 Vinpearl 리조트 생태계의 일부로, 드넓은 수경, 시원한 녹지, 전문 서비스로 빠르게 골퍼들의 주목을 받았습니다.

2. 설계 및 경관  
– Lakeside: 넓은 호수를 감싸는 페어웨이와 백사장 벙커, 섬 그린이 특징입니다.  
– Marshland: 자연 습지를 가로지르는 페어웨이로, 변화무쌍한 지형이 원시적 도전을 제공합니다.

3. 잔디 품질 및 유지 관리  
페어웨이는 Platinum Paspalum, 그린은 TifEagle Bermuda를 사용하며, USGA 기준의 자동 관개 시스템과 전담 유지 관리 팀이 항상 부드러운 상태를 유지합니다.

4. 시설 및 서비스  
약 5,000㎡ 규모의 모던 클럽하우스에는 고급 라커, 프로숍, 아시안‐유러피언 레스토랑, 드라이빙 레인지, 퍼팅 그린, 스파, 수영장이 마련되어 있습니다. 전문 캐디 서비스와 PGA 코치 레슨도 제공합니다.

5. 경험 및 추천  
– 새벽: 신선한 공기와 호수의 고요한 아침을 즐겨보세요.  
– 해질녘: 해변 티 박스에서 황홀한 석양을 감상하세요.

6. 예약  
(+84) 0123456789로 전화하시거나 TeetimeVn.com에서 온라인 예약하세요.
'
WHERE course_id = 47 AND lang = 'ko';


UPDATE golf_course_i18n
SET overview = '
Sono Felice Country Club Hải Phòng tọa lạc tại thôn Lưu Kiểm, huyện Thủy Nguyên, thành phố Hải Phòng, cách Hà Nội khoảng 120 km và cách sân bay Cát Bi 25 km.
Trên diện tích bao quanh bởi sông Gia và sông Mộc, sân gồm 18 hố par 71, dài 7123 yards (6513 m), được thiết kế bởi Pacific Coast Design và khai trương năm 2011.

1. Tổng quan & Lịch sử  
Được phát triển từ dự án Sono Belle – Song Gia Golf Resort, Sono Felice mở cửa năm 2011 và nhanh chóng trở thành điểm đến yêu thích của golfer trong nước và quốc tế.

2. Thiết kế & Cảnh quan  
Sân gồm hai vòng River Nine và Ocean Nine, tận dụng cảnh quan sông nước và đồi gò, gió sông mang đến thử thách bất ngờ.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens sử dụng Bentgrass, fairway dùng Paspalum, được duy trì theo tiêu chuẩn USGA với hệ thống tưới tự động và đội ngũ chăm sóc chuyên nghiệp.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại, driving range, resort tại chỗ, nhà hàng Á-Âu, spa, phòng gym và dịch vụ caddie, HLV PGA luôn sẵn sàng phục vụ.

5. Trải nghiệm & Gợi ý  
– Giờ lý tưởng: sáng sớm ngắm sương mù bên sông.  
– Hole River 9: kết thúc ngoạn mục với green cao và bunker hiểm hóc.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 48 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = '
Sono Felice Country Club Hai Phong is located in Luu Kiem Village, Thuy Nguyen District, Hai Phong City—about 120 km from Hanoi and 25 km from Cat Bi Airport. Set on land surrounded by the Gia and Moc rivers, the course features 18 par-71 holes over 7,123 yards (6,513 m), designed by Pacific Coast Design and opened in 2011.

1. Overview & History  
Developed from the Sono Belle – Song Gia Golf Resort project, Sono Felice opened in 2011 and quickly became a favorite destination for both domestic and international golfers.

2. Design & Scenery  
The course consists of two loops, River Nine and Ocean Nine, taking full advantage of riverside and rolling-hill landscapes, with river breezes adding unexpected challenges.

3. Turf Quality & Maintenance  
Greens use Bentgrass and fairways use Paspalum, maintained to USGA standards with an automatic irrigation system and a professional care team.

4. Facilities & Services  
A modern clubhouse, driving range, on-site resort accommodation, an Asian-European restaurant, spa, gym, caddie service, and PGA coach lessons are all available.

5. Experience & Recommendations  
– Ideal time: early morning to enjoy the mist over the river.  
– River Nine finishing hole: a dramatic end with an elevated green and challenging bunkers.

6. Reservations  
Call (+84) 0123456789 or book your tee time online at TeetimeVn.com for the best offers.
'
WHERE course_id = 48 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
Sono Felice 海防乡村俱乐部位于海防市水原区留检村，距河内约120公里，距Cat Bi机场25公里。球场被嘉河与木河环绕，占地7,123码（6,513米），共18个标准71杆球洞，由Pacific Coast Design设计，2011年开业。

1. 概况与历史  
由Sono Belle – Song Gia高尔夫度假区项目开发，Sono Felice于2011年开放，迅速成为国内外球手的热门目的地。

2. 设计与景观  
球场由River Nine和Ocean Nine两段9洞循环组成，充分利用河畔与丘陵地形，河风带来意想不到的挑战。

3. 草坪质量与维护  
果岭采用Bentgrass，球道采用Paspalum，按USGA标准维护，配备自动灌溉系统和专业养护团队。

4. 设施与服务  
现代会所、练习场、度假住宿、亚欧餐厅、水疗、健身房、球童服务及PGA教练课程一应俱全。

5. 体验与建议  
– 理想时段：清晨欣赏河雾。  
– River Nine收官洞：高架果岭与险峻沙坑带来戏剧性高潮。

6. 预订  
请致电(+84)0123456789或访问TeetimeVn.com在线预订，享受最佳优惠。
'
WHERE course_id = 48 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
Sono Felice 海防鄉村俱樂部位於海防市水原區留檢村，距河內約120公里，距Cat Bi機場25公里。球場被嘉河與木河環繞，總長7,123碼（6,513米），共18個標準71桿球洞，由Pacific Coast Design設計，2011年開幕。

1. 概況與歷史  
由Sono Belle – Song Gia高爾夫度假區項目開發，Sono Felice於2011年營運，迅速成為國內外球手的最愛。

2. 設計與景觀  
球場由River Nine和Ocean Nine兩個9洞循環組成，善用河畔與丘陵地形，河風帶來意想不到的挑戰。

3. 草皮品質與維護  
果嶺採用Bentgrass，球道採用Paspalum，按USGA標準維護，配備自動灌溉系統與專業養護團隊。

4. 設施與服務  
現代會所、練習場、內設度假村住宿、亞歐餐廳、水療中心、健身房、專業球童服務及PGA教練課程一應俱全。

5. 體驗與建議  
– 理想時段：清晨欣賞河畔霧景。  
– River Nine收官洞：高架果嶺與險峻沙坑締造戲劇性結局。

6. 預訂  
請撥打(+84)0123456789或訪問TeetimeVn.com線上預訂，尊享優惠。
'
WHERE course_id = 48 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
Sono Felice カントリークラブ（Hai Phong）は、ハイフォン市トゥイグエン区リュウキム村に位置し、ハノイから約120km、カットビ空港から25kmです。嘉川と木川に囲まれた敷地に全長7,123ヤード（6,513m）のパー71×18ホールがあり、Pacific Coast Designが設計、2011年に開場しました。

1. 概要と歴史  
Sono Belle – Song Giaゴルフリゾートプロジェクトから開発され、2011年に開場後、国内外のゴルファーに人気のスポットとなりました。

2. 設計と景観  
River NineとOcean Nineの2つの9ホールループで構成され、河畔と丘陵の景観を活かし、川風が意外な挑戦をもたらします。

3. 芝質とメンテナンス  
グリーンはベントグラス、フェアウェイはパスパラムを採用し、USGA基準の自動灌漑システムと専門チームで管理しています。

4. 施設とサービス  
モダンなクラブハウス、ドライビングレンジ、オンサイトリゾート、アジアン・ヨーロピアンレストラン、スパ、ジム、キャディサービス、PGAコーチレッスンを完備。

5. 体験とおすすめ  
– 理想的な時間：早朝の川霧を楽しむ。  
– River Nineの最終ホール：高台グリーンと戦略的バンカーがドラマチックな締めくくりを演出。

6. 予約  
(+84)0123456789までお電話、またはTeetimeVn.comでオンライン予約をどうぞ。
'
WHERE course_id = 48 AND lang = 'ja';

UPDATE golf_course_i18n
SET overview = '
Sono Felice 컨트리 클럽(Hai Phong)은 하이퐁시 트이응웬구 류킴 마을에 위치하며, 하노이에서 약 120km, 캇비 공항에서 25km 떨어져 있습니다. 자강과목강으로 둘러싸인 부지에 총 길이 7,123야드(6,513m), 파71×18홀 코스가 있으며, Pacific Coast Design이 설계하고 2011년 개장했습니다.

1. 개요 및 역사  
Sono Belle – Song Gia 골프 리조트 프로젝트에서 개발되어 2011년 개장 후 국내외 골퍼들에게 사랑받는 명소가 되었습니다.

2. 설계 및 경관  
River Nine과 Ocean Nine 두 개의 9홀 루프로 구성되어 강변과 구릉 지형을 활용하며 강바람이 예상치 못한 도전을 제공합니다.

3. 잔디 품질 및 유지 관리  
그린은 벤트그래스, 페어웨이는 파스파럼을 사용하며 USGA 기준의 자동 관개 시스템과 전문 팀이 관리합니다.

4. 시설 및 서비스  
모던 클럽하우스, 드라이빙 레인지, 리조트 숙박, 아시안-유러피언 레스토랑, 스파, 헬스장, 캐디 서비스 및 PGA 코치 레슨을 제공합니다.

5. 경험 및 추천  
– 이상적인 시간: 이른 아침 강안의 안개를 감상하세요.  
– River Nine 마지막 홀: 높은 그린과 전략적 벙커가 드라마틱한 마무리를 선사합니다.

6. 예약  
(+84)0123456789로 전화하거나 TeetimeVn.com에서 온라인 예약하세요.
'
WHERE course_id = 48 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = '
Ruby Tree Golf Resort Hải Phòng tọa lạc tại Ngọc Xuyên, Đồ Sơn, TP. Hải Phòng.
Cách trung tâm thành phố khoảng 15 phút lái xe và sân bay Cát Bi khoảng 25 km.

1. Tổng quan & Lịch sử  
Sân golf 18 hố par-72, dài 6.317 m (6.908 yards), do Pacific Coast Design thiết kế và chính thức khai trương năm 2010 dưới tên Do Son Seaside Golf Resort.

2. Thiết kế & Cảnh quan  
Course có bốn tee khác nhau, fairway uốn lượn quanh các hồ nước và bunker cát trắng tạo nên thử thách nghệ thuật.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens sử dụng Paspalum, fairway bằng Paspalum được chăm sóc theo tiêu chuẩn USGA với hệ thống tưới tự động và đội ngũ bảo trì chuyên nghiệp.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại bao gồm locker cao cấp, pro-shop, driving range và dịch vụ cho thuê golf cart (USD 37).  
Caddie chuyên nghiệp luôn sẵn sàng hỗ trợ golfer.

5. Trải nghiệm & Gợi ý  
– Sáng sớm: tận hưởng gió biển mát rượi và bình minh trên fairway.  
– Chiều muộn: ngắm hoàng hôn khi ánh nắng phản chiếu lên mặt nước.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 49 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = '
Ruby Tree Golf Resort Hai Phong is located in Ngoc Xuyen, Do Son District, Hai Phong City—about a 15-minute drive from the city center and 25 km from Cat Bi Airport.

1. Overview & History  
The 18-hole, par-72 course spans 6,317 m (6,908 yards), designed by Pacific Coast Design and officially opened in 2010 as Do Son Seaside Golf Resort.

2. Design & Scenery  
The course features four different tee boxes, with fairways winding around water hazards and white sand bunkers, creating artistic challenges.

3. Turf Quality & Maintenance  
Greens and fairways both use Paspalum, maintained to USGA standards with an automatic irrigation system and a professional maintenance team.

4. Facilities & Services  
The modern clubhouse includes premium lockers, a pro shop, a driving range, and golf cart rental service (USD 37). Professional caddies are always on hand to assist golfers.

5. Experience & Recommendations  
– Early morning: enjoy the cool sea breeze and sunrise over the fairway.  
– Late afternoon: watch the sunset as its rays dance on the water.

6. Reservations  
Call (+84) 0123456789 or book your tee time online at TeetimeVn.com for the best offers.
'
WHERE course_id = 49 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
Ruby Tree 高尔夫度假村（海防）位于海防市多山区玉宣，距离市中心约15分钟车程，距Cat Bi机场约25公里。

1. 概况与历史  
这座18洞、标准72杆的球场全长6,317米（6,908码），由Pacific Coast Design设计，2010年以Do Son Seaside Golf Resort之名正式开业。

2. 设计与景观  
球场设有四个不同发球台，球道环绕水障碍和白色沙坑，营造艺术化的挑战。

3. 草坪质量与维护  
果岭和球道均采用Paspalum草，按USGA标准维护，配备自动灌溉系统和专业维护团队。

4. 设施与服务  
现代化会所包括高档储物柜、专业球具店、练习场和高尔夫球车租赁服务（37美元）。专业球童随时为球手提供协助。

5. 体验与建议  
– 清晨：感受凉爽海风和球道上的日出美景。  
– 傍晚：欣赏夕阳余晖在水面上的映照。

6. 预订  
请致电(+84) 0123456789或访问TeetimeVn.com在线预订，享受最佳优惠。
'
WHERE course_id = 49 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
Ruby Tree 高爾夫渡假村（海防）位於海防市多山區玉宣，距市中心約15分鐘車程，距Cat Bi機場約25公里。

1. 概況與歷史  
這座18洞、標準72桿的球場全長6,317米（6,908碼），由Pacific Coast Design設計，2010年以Do Son Seaside Golf Resort之名正式開幕。

2. 設計與景觀  
球場設有四個不同發球台，球道環繞水障礙和白色沙坑，營造藝術化挑戰。

3. 草皮品質與維護  
果嶺和球道均採用Paspalum草，依USGA標準維護，配備自動灌溉系統和專業維護團隊。

4. 設施與服務  
現代化會所包括高檔儲物櫃、專業球具店、練習場及高爾夫球車租賃服務（37美元）。專業球童隨時為球手提供協助。

5. 體驗與建議  
– 清晨：享受涼爽海風與球道上的日出美景。  
– 傍晚：觀賞夕陽餘暉映照水面之美。

6. 預訂  
請撥打(+84) 0123456789或訪問TeetimeVn.com線上預訂，尊享優惠。
'
WHERE course_id = 49 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
Ruby Treeゴルフリゾート（ハイフォン）は、ハイフォン市ドーソン区ゴックシュエンに位置し、市中心部から車で約15分、カットビ空港から約25kmです。

1. 概要と歴史  
全長6,317m（6,908ヤード）、パー72の18ホールコースはPacific Coast Designが設計し、2010年にDo Son Seaside Golf Resortとして正式オープンしました。

2. 設計と景観  
コースには4つの異なるティーがあり、フェアウェイは水域や白砂のバンカーに沿って曲線を描き、芸術的な挑戦を提供します。

3. 芝質とメンテナンス  
グリーンとフェアウェイにはPaspalumを使用し、USGA基準の自動灌漑システムと専門チームによるメンテナンスで常に良好な状態を保っています。

4. 施設とサービス  
モダンなクラブハウスには高級ロッカー、プロショップ、ドライビングレンジがあり、ゴルフカートレンタル（37米ドル）サービスを提供。プロキャディが常にサポートします。

5. 体験とおすすめ  
– 早朝：涼しい海風とフェアウェイに昇る朝日を楽しむ。  
– 夕方：水面に映る夕陽をフェアウェイから眺める。

6. 予約  
(+84) 0123456789までお電話、またはTeetimeVn.comでオンライン予約を。
'
WHERE course_id = 49 AND lang = 'ja';

UPDATE golf_course_i18n
SET overview = '
Ruby Tree 골프 리조트 하이퐁은 하이퐁시 도손구 옥선에 위치하며, 도심에서 차로 약 15분, 캇비 공항에서 약 25km 떨어져 있습니다.

1. 개요 및 역사  
전장 6,317m(6,908야드), 파72 18홀 코스는 Pacific Coast Design이 설계했으며, 2010년 Do Son Seaside Golf Resort라는 이름으로 공식 개장했습니다.

2. 설계 및 경관  
코스에는 4개의 서로 다른 티가 있으며, 페어웨이는 수역과 흰 모래 벙커를 따라 굽이치며 예술적 도전을 제공합니다.

3. 잔디 품질 및 유지 관리  
그린과 페어웨이는 Paspalum을 사용하며, USGA 기준의 자동 관개 시스템과 전문 유지 관리 팀이 항상 관리합니다.

4. 시설 및 서비스  
모던한 클럽하우스에는 고급 라커, 프로숍, 드라이빙 레인지가 있으며, 골프 카트 대여 서비스(37달러)를 제공합니다. 전문 캐디가 항상 골퍼를 지원합니다.

5. 경험 및 추천  
– 이른 아침: 시원한 바닷바람과 페어웨이에 떠오르는 일출을 즐기세요.  
– 늦은 오후: 물에 반사된 석양을 페어웨이에서 감상하세요.

6. 예약  
(+84) 0123456789로 전화하시거나 TeetimeVn.com에서 온라인 예약하세요.
'
WHERE course_id = 49 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = '
Câu lạc bộ Golf Quốc tế Móng Cái tọa lạc tại Tràng Vĩ, phường Trà Cổ, thành phố Móng Cái, tỉnh Quảng Ninh, ngay sát biên giới Việt - Trung. Sân được khai trương năm 2008, do Pacific Coast Design thiết kế, với 18 hố par 72 trải dài 7.204 yards (tương đương 6.587 m) dọc bờ biển Tra Cổ. Các fairway uốn lượn giữa cồn cát và bunker dựng đứng, mang đậm phong cách Links cổ điển.

1. Tổng quan & Lịch sử  
Là sân gôn tiêu chuẩn quốc tế duy nhất giáp biển và biên giới, Móng Cái nhanh chóng thu hút golfer trong và ngoài nước nhờ quang cảnh hoang sơ và không khí mát mẻ quanh năm.

2. Thiết kế & Cảnh quan  
– 18 hố Links nằm dọc 3 km bờ biển Tra Cổ.  
– Bunker cát dựng đứng, fairway ôm sát bãi biển, chướng ngại nước tự nhiên.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens Bentgrass và fairway Paspalum được chăm sóc theo tiêu chuẩn USGA với hệ thống tưới tự động và đội ngũ greenkeeper chuyên nghiệp.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại với locker cao cấp, pro-shop, driving range, putting green, nhà hàng Á-Âu và spa. Caddie chuyên nghiệp, huấn luyện viên PGA và xe điện luôn sẵn sàng phục vụ.

5. Trải nghiệm & Gợi ý  
– Sáng sớm: biển lặng, không khí mát mẻ.  
– Chiều tối: hoàng hôn in bóng lên mặt nước và cồn cát.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 50
  AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = '
International Golf Club Móng Cái is located in Tràng Vĩ, Trà Cổ Ward, Móng Cái City, Quang Ninh Province, right on the Vietnam–China border. The course opened in 2008, designed by Pacific Coast Design, featuring 18 par-72 holes stretching 7,204 yards (6,587 meters) along the Trà Cổ coastline. Fairways wind through sand dunes and sheer bunkers, reflecting a classic links style.

1. Overview & History  
As the only international-standard golf course bordering both the sea and the border, Móng Cái quickly attracted domestic and international golfers with its pristine scenery and year-round cool climate.

2. Design & Scenery  
– The 18-hole links course runs along 3 km of the Trà Cổ coastline.  
– Sheer sand bunkers and fairways hugging the beach, with natural water hazards.

3. Turf Quality & Maintenance  
Greens use Bentgrass and fairways use Paspalum, maintained to USGA standards with automatic irrigation and a professional greenkeeping team.

4. Facilities & Services  
A modern clubhouse with premium lockers, a pro shop, driving range, putting green, an Asian-European restaurant, and a spa. Professional caddies, PGA coaches, and electric carts are always available.

5. Experience & Recommendations  
– Early morning: calm sea and cool air.  
– Late afternoon: watch the sunset reflected on the water and dunes.

6. Reservations  
Call (+84) 0123456789 or book your tee time online at TeetimeVn.com for the best offers.
'
WHERE course_id = 50 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
国际蒙凯高尔夫俱乐部位于广宁省蒙凯市茶古坊章威，紧邻越中边境。球场于2008年开幕，由 Pacific Coast Design 设计，拥有18个标准72杆球洞，沿茶古海岸线延伸7,204码（6,587米）。球道在沙丘和直立沙坑间蜿蜒，呈现经典 links 风格。

1. 概况与历史  
作为唯一一座既临海又接壤边境的国际标准高尔夫球场，蒙凯凭借原始景观和全年宜人的凉爽气候迅速吸引了国内外球手。

2. 设计与景观  
– 18洞 links 球场沿茶古海岸线延伸3公里。  
– 直立沙坑，球道紧贴海滩，自然水障碍。

3. 草坪质量与维护  
果岭采用 Bentgrass，球道采用 Paspalum，按 USGA 标准维护，配备自动灌溉系统和专业绿化团队。

4. 设施与服务  
现代会所设有高档储物柜、专业球具店、练习场、推杆练习区、亚欧餐厅和 SPA。专业球童、PGA 教练和电动车随时待命。

5. 体验与建议  
– 清晨：海面平静，空气清凉。  
– 傍晚：观赏夕阳映在海面和沙丘上的美景。

6. 预订  
请致电 (+84) 0123456789 或访问 TeetimeVn.com 在线预订，获取最佳优惠。
'
WHERE course_id = 50 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
國際蒙凱高爾夫俱樂部位於廣寧省蒙凱市茶古坊章威，緊鄰越中邊境。球場於2008年開幕，由 Pacific Coast Design 設計，擁有18個標準72桿球洞，沿茶古海岸線延伸7,204碼（6,587米）。球道在沙丘和直立沙坑間蜿蜒，呈現經典 links 風格。

1. 概況與歷史  
作為唯一一座既臨海又接壤邊境的國際標準高爾夫球場，蒙凱憑藉原始景觀和全年宜人的涼爽氣候迅速吸引了國內外球手。

2. 設計與景觀  
– 18洞 links 球場沿茶古海岸線延伸3公里。  
– 直立沙坑，球道緊貼海灘，自然水障礙。

3. 草皮品質與維護  
果嶺採用 Bentgrass，球道採用 Paspalum，依 USGA 標準維護，配備自動灌溉系統和專業綠化團隊。

4. 設施與服務  
現代會所設有高檔儲物櫃、專業球具店、練習場、推桿練習區、亞歐餐廳和 SPA。專業球童、PGA 教練和電動車隨時待命。

5. 體驗與建議  
– 清晨：海面平靜，空氣清涼。  
– 傍晚：觀賞夕陽映在海面和沙丘上的美景。

6. 預訂  
請撥打 (+84) 0123456789 或訪問 TeetimeVn.com 線上預訂，獲取最佳優惠。
'
WHERE course_id = 50 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
モンカイ国際ゴルフクラブは広寧省モンカイ市チャコ坊トランヴィ地区に位置し、ベトナムと中国の国境に隣接しています。2008年に開場したコースは Pacific Coast Design が設計した18ホール、パー72、全長7,204ヤード（6,587m）で、チャコ海岸線に沿って広がります。フェアウェイは砂丘と垂直に切り立つバンカーの間を縫うように配置され、クラシックなリンクススタイルを体現しています。

1. 概要と歴史  
海と国境の両方に接する唯一の国際基準ゴルフコースとして、モンカイは手つかずの景観と一年中涼しい気候で国内外のゴルファーを惹きつけています。

2. 設計と景観  
– 18ホールのリンクスコースはチャコ海岸線に沿って3kmにわたって展開。  
– 垂直の砂バンカーとビーチに沿ったフェアウェイ、自然のウォーターハザード。

3. 芝質とメンテナンス  
グリーンはベントグラス、フェアウェイはパスパラムを使用し、自動灌漑システムとプロのグリーンキーピングチームによって USGA 基準で管理されています。

4. 施設とサービス  
モダンなクラブハウスには高級ロッカー、プロショップ、ドライビングレンジ、パッティンググリーン、アジアン・ヨーロピアンレストラン、スパを完備。プロキャディ、PGAコーチ、電動カートが常時利用可能です。

5. 体験とおすすめ  
– 早朝：穏やかな海と涼しい空気を満喫。  
– 夕方：水面と砂丘に映るサンセットを観賞。

6. 予約  
(+84) 0123456789までお電話いただくか、TeetimeVn.comでオンライン予約をどうぞ。
'
WHERE course_id = 50 AND lang = 'ja';

UPDATE golf_course_i18n
SET overview = '
몽카이 인터내셔널 골프 클럽은 꽝닌성 몽카이시 트라코사 트랑비 지구에 위치하며 베트남-중국 국경 바로 옆에 있습니다. 2008년에 개장한 이 코스는 Pacific Coast Design이 설계했으며, 파72 18홀, 전장 7,204야드(6,587m)로 차코 해안선을 따라 펼쳐집니다. 페어웨이는 사구와 수직 벙커 사이를 굽이치며 클래식 링크스 스타일을 띠고 있습니다.

1. 개요 및 역사  
바다와 국경을 모두 인접한 유일한 국제 기준 골프 코스로서 몽카이는 원시 그대로의 경관과 연중 시원한 기후로 국내외 골퍼들의 관심을 끌고 있습니다.

2. 설계 및 경관  
– 18홀 링크스 코스는 차코 해안선을 따라 3km에 걸쳐 펼쳐집니다.  
– 수직 사구 벙커와 해변을 따라 이어진 페어웨이, 자연 워터 해저드.

3. 잔디 품질 및 유지 관리  
그린은 벤트그래스, 페어웨이는 파스파럼을 사용하며 자동 관개 시스템과 전문 그린키핑 팀이 USGA 기준으로 관리합니다.

4. 시설 및 서비스  
모던한 클럽하우스에는 고급 라커, 프로숍, 드라이빙 레인지, 퍼팅 그린, 아시안-유러피언 레스토랑, 스파가 갖춰져 있으며 프로 캐디, PGA 코치, 전동 카트가 상시 대기합니다.

5. 체험 및 추천  
– 이른 아침: 고요한 바다와 시원한 공기를 만끽하세요.  
– 저녁: 물과 사구에 반사된 석양을 감상하세요.

6. 예약  
(+84) 0123456789로 전화하거나 TeetimeVn.com에서 온라인 예약하세요.
'
WHERE course_id = 50 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = '
Amber Hills Golf Resort tọa lạc tại thôn Bình An, xã Tiền Phong, huyện Yên Dũng, tỉnh Bắc Giang, cách trung tâm Hà Nội khoảng 50 km. Sân bao gồm 36 hố par 72, do Albanese & Lutzke thiết kế; giai đoạn 1 (Hillside Course) 18 hố dài 6.162 m khai trương tháng 8 2017, giai đoạn 2 (Rock Valley Course) 18 hố dài 6.575 m khai trương năm 2022.

1. Tổng quan & Lịch sử  
Được xây dựng nhằm tận dụng địa hình đồi núi Nham Biền, Amber Hills nhanh chóng được công nhận là “sân golf thử thách nhất Việt Nam” với vốn đầu tư 1.600 tỷ đồng, thu hút cả golfer trong nước và quốc tế.

2. Thiết kế & Cảnh quan  
– Hillside Course: fairway xuyên qua rừng thông và đồi dốc;  
– Rock Valley Course: phong cách links với bunker cát trắng và hồ nước tự nhiên.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens Bentgrass và fairway Paspalum được chăm sóc theo tiêu chuẩn USGA, với hệ thống tưới tự động và đội ngũ greenkeeper vận hành 24/7.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse sang trọng với locker cao cấp, pro-shop, driving range, putting green, nhà hàng Á-Âu, spa và biệt thự nghỉ dưỡng. Xe điện và caddie chuyên nghiệp luôn sẵn sàng phục vụ.

5. Trải nghiệm & Gợi ý  
– Sáng sớm: sương mù giăng giữa rừng thông;  
– Chiều muộn: hoàng hôn rực rỡ khung núi Nham Biền.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 51
  AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = '
Amber Hills Golf Resort is located in Binh An Hamlet, Tien Phong Commune, Yen Dung District, Bac Giang Province—about 50 km from central Hanoi. The resort comprises 36 par-72 holes, designed by Albanese & Lutzke; Phase 1 (Hillside Course) 18 holes over 6,162 m opened in August 2017, and Phase 2 (Rock Valley Course) 18 holes over 6,575 m opened in 2022.

1. Overview & History  
Built to take advantage of the Nam Bien mountain terrain, Amber Hills was quickly recognized as “Vietnam''s most challenging golf course” with an investment of VND 1,600 billion, attracting both domestic and international golfers.

2. Design & Scenery  
– Hillside Course: fairways cutting through pine forests and steep hills;  
– Rock Valley Course: links-style with white sand bunkers and natural water hazards.

3. Turf Quality & Maintenance  
Bentgrass greens and Paspalum fairways are maintained to USGA standards, with an automatic irrigation system and a greenkeeping team operating 24/7.

4. Facilities & Services  
A luxurious clubhouse with premium lockers, a pro shop, driving range, putting green, an Asian-European restaurant, spa, and resort villas. Electric carts and professional caddies are always available.

5. Experience & Recommendations  
– Early morning: mist drifting through pine forests;  
– Late afternoon: a spectacular sunset over the Nam Bien mountains.

6. Reservations  
Call (+84) 0123456789 or book your tee time online at TeetimeVn.com for the best offers.
'
WHERE course_id = 51 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
Amber Hills 高尔夫度假村位于北江省延勇县前丰社平安村，距河内市中心约50 公里。球场包括36洞标准72杆，由Albanese & Lutzke设计；第一期（Hillside Course）18洞全长6,162 米，2017年8月开幕；第二期（Rock Valley Course）18洞全长6,575 米，2022年开幕。

1. 概况与历史  
Amber Hills建于南边山地形之上，凭借独特地形被誉为“越南最具挑战性的高尔夫球场”，投资16,000亿越盾，吸引国内外众多球手。

2. 设计与景观  
– Hillside Course：球道穿越松林和陡坡；  
– Rock Valley Course：links风格，白色沙坑和天然水障碍。

3. 草坪质量与维护  
果岭采用Bentgrass，球道采用Paspalum，按USGA标准维护，配备自动灌溉系统和24/7运营的绿化团队。

4. 设施与服务  
奢华会所配备高级储物柜、专业球具店、练习场、推杆果岭、亚欧餐厅、水疗中心和度假别墅。电动车和专业球童随时待命。

5. 体验与建议  
– 清晨：松林间薄雾缭绕；  
– 傍晚：南边山脉的壮丽日落。

6. 预订  
请致电(+84) 0123456789或访问TeetimeVn.com在线预订，获取最佳优惠。
'
WHERE course_id = 51 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
Amber Hills 高爾夫渡假村位於北江省延勇縣前豐社平安村，距河內市中心約50 公里。球場包括36洞標準72桿，由Albanese & Lutzke設計；第一期（Hillside Course）18洞全長6,162 米，2017年8月開幕；第二期（Rock Valley Course）18洞全長6,575 米，2022年開幕。

1. 概況與歷史  
Amber Hills建於南邊山地形之上，憑藉獨特地形被譽為「越南最具挑戰性的高爾夫球場」，投資16,000億越盾，吸引國內外眾多球手。

2. 設計與景觀  
– Hillside Course：球道穿越松林和陡坡；  
– Rock Valley Course：links風格，白色沙坑和天然水障礙。

3. 草皮品質與維護  
果嶺採用Bentgrass，球道採用Paspalum，依USGA標準維護，配備自動灌溉系統和24/7運營的綠化團隊。

4. 設施與服務  
奢華會所配備高級儲物櫃、專業球具店、練習場、推杆果嶺、亞歐餐廳、水療中心和度假別墅。電動車和專業球童隨時待命。

5. 體驗與建議  
– 清晨：松林間薄霧繚繞；  
– 傍晚：南邊山脈的壯麗日落。

6. 預訂  
請撥打(+84) 0123456789或訪問TeetimeVn.com線上預訂，尊享優惠。
'
WHERE course_id = 51 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
Amber Hillsゴルフリゾートは北江省イェンドゥン県ティエンフォン社ビンアン村に位置し、ハノイ中心部から約50 kmです。36ホール・パー72コースはAlbanese & Lutzkeが設計し、第1フェーズ（Hillside Course）18ホール、全長6,162 mが2017年8月にオープン、第2フェーズ（Rock Valley Course）18ホール、全長6,575 mが2022年にオープンしました。

1. 概要と歴史  
ナムビエンの山岳地形を活かして建設されたAmber Hillsは、16兆ドンの投資を受け「ベトナムで最も挑戦的なゴルフコース」として評価され、国内外のゴルファーを惹きつけています。

2. 設計と景観  
– Hillside Course：松林と急斜面を貫くフェアウェイ。  
– Rock Valley Course：リンクス風の白砂バンカーと天然のウォーターハザード。

3. 芝質とメンテナンス  
ベントグラスのグリーンとパスパラムのフェアウェイはUSGA基準で管理され、自動灌漑システムと24時間体制のグリーンキーピングチームを完備。

4. 施設とサービス  
高級ロッカー、プロショップ、ドライビングレンジ、パッティンググリーン、アジアン・ヨーロピアンレストラン、スパ、リゾートヴィラを備えた豪華なクラブハウス。電動カートとプロキャディが常に利用可能。

5. 体験とおすすめ  
– 早朝：松林に漂う霧。  
– 夕方：南ビエン山脈に沈む壮大な夕日。

6. 予約  
(+84) 0123456789までお電話いただくか、TeetimeVn.comでオンライン予約をどうぞ。
'
WHERE course_id = 51 AND lang = 'ja';

UPDATE golf_course_i18n
SET overview = '
Amber Hills 골프 리조트는 북징성 옌드엉현 티엔펑사 빈안촌에 위치하며 하노이 중심부에서 약 50 km 떨어져 있습니다. 36홀 파72 코스는 Albanese & Lutzke가 설계했으며, 1단계(Hillside Course) 18홀 6,162 m가 2017년 8월 개장, 2단계(Rock Valley Course) 18홀 6,575 m가 2022년에 개장했습니다.

1. 개요 및 역사  
남비엔 산악 지형을 활용해 건설된 Amber Hills는 1,600억 동의 투자로 “베트남에서 가장 도전적인 골프장”으로 인정받아 국내외 골퍼들의 관심을 모았습니다.

2. 설계 및 경관  
– Hillside Course: 소나무 숲과 가파른 언덕을 가로지르는 페어웨이.  
– Rock Valley Course: 링크스 스타일의 흰 모래 벙커와 천연 워터 해저드.

3. 잔디 품질 및 유지 관리  
그린은 벤트그래스, 페어웨이는 파스팔럼을 사용하며 USGA 기준으로 관리되고, 자동 관개 시스템과 24시간 운영되는 그린키핑 팀이 운영됩니다.

4. 시설 및 서비스  
고급 라커, 프로 숍, 드라이빙 레인지, 퍼팅 그린, 아시안-유러피언 레스토랑, 스파, 리조트 빌라를 갖춘 호화로운 클럽하우스. 전동 카트와 전문 캐디가 항상 대기 중입니다.

5. 경험 및 추천  
– 이른 아침: 소나무 숲 사이로 피어오르는 안개.  
– 늦은 오후: 남비엔 산맥 위로 지는 장엄한 일몰.

6. 예약  
(+84) 0123456789로 전화하시거나 TeetimeVn.com에서 온라인 예약하세요.
'
WHERE course_id = 51 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = '
Stone Highland Golf & Resort tọa lạc tại khu vực Việt Yên, tỉnh Bắc Giang, cách trung tâm Hà Nội khoảng 1,5 giờ lái xe (~90 km).

1. Tổng quan & Lịch sử  
Dự án do Truong An Golf Company phát triển, hướng đến trải nghiệm golf trên nền địa hình đồi núi với khí hậu mát mẻ quanh năm. Sau khi mở 18 hố đầu cuối năm 2023, sân đã nhanh chóng thu hút golfer trong nước và quốc tế.

2. Thiết kế & Cảnh quan  
Layout tận dụng sườn núi và ruộng lúa bao quanh, mang đến tầm nhìn bao quát thiên nhiên hùng vĩ. Các bunker và chướng ngại nước được bố trí chiến lược để thử thách kỹ thuật điều khiển bóng.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens được đánh giá là một trong những greens đẹp nhất miền Bắc Việt Nam. Fairway được chăm sóc tỉ mỉ theo tiêu chuẩn quốc tế với hệ thống tưới tự động và đội ngũ bảo dưỡng chuyên nghiệp.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại với khu locker, pro-shop, driving range và các nhà hàng Á – Âu đa dạng. Dịch vụ thuê golf cart và trang thiết bị (gậy, giày, dù) luôn sẵn sàng đáp ứng nhu cầu golfer.

5. Trải nghiệm & Gợi ý  
Sân phù hợp cho cả golfer mới và chuyên nghiệp nhờ layout linh hoạt và cảnh quan thay đổi liên tục.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 52 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = '
Stone Highland Golf & Resort is located in Viet Yen area, Bac Giang Province—about a 1.5-hour drive (approximately 90 km) from central Hanoi.

1. Overview & History  
Developed by Truong An Golf Company to deliver a mountain-terrain golfing experience with a cool year-round climate. Since the opening of its first 18 holes in late 2023, the resort has quickly attracted golfers both domestic and international.

2. Design & Scenery  
The layout takes advantage of hillside terrain and surrounding rice paddies, offering panoramic views of majestic nature. Bunkers and water hazards are strategically positioned to challenge players in controlling their shots.

3. Turf Quality & Maintenance  
The greens are regarded among the most beautiful in northern Vietnam. Fairways are meticulously maintained to international standards with an automatic irrigation system and a professional maintenance team.

4. Facilities & Services  
A modern clubhouse features locker rooms, a pro shop, a driving range, and a variety of Asian–European dining options. Golf cart rentals and equipment (clubs, shoes, umbrellas) are available to meet every golfer''s needs.

5. Experience & Recommendations  
The course suits both beginners and professionals thanks to its flexible layout and ever-changing scenery.

6. Reservations  
Call (+84) 0123456789 or book your tee time online at TeetimeVn.com for the best deals.
'
WHERE course_id = 52 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
Stone Highland 高尔夫度假村位于北江省越银地区，距河内市中心约1.5小时车程（约90 公里）。

1. 概况与历史  
由Truong An Golf Company开发，旨在提供山地地形的高尔夫体验和全年凉爽气候。自2023年底首个18洞开放以来，迅速吸引了国内外球手。

2. 设计与景观  
球场布局充分利用山坡地形和周边稻田，呈现壮丽的全景视野。沙坑和水障碍经过战略性布置，考验球员的击球控制能力。

3. 草坪品质与维护  
果岭被评为越南北部最美之一，球道按照国际标准精心维护，配备自动灌溉系统和专业养护团队。

4. 设施与服务  
现代化会所设有更衣室、专业球具店、练习场及多样的亚欧餐饮选择。提供高尔夫球车租赁及设备（球杆、球鞋、雨伞）服务，随时满足球手需求。

5. 体验与建议  
灵活的布局和不断变化的景观使球场既适合新手，也适合职业球员。

6. 预订  
请致电(+84) 0123456789或访问TeetimeVn.com在线预订，以获取最佳优惠。
'
WHERE course_id = 52 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
Stone Highland 高爾夫渡假村位於北江省越銀地區，距河內市中心約1.5小時車程（約90 公里）。

1. 概況與歷史  
由Truong An Golf Company開發，旨在提供山地地形的高爾夫體驗與全年涼爽氣候。自2023年底首個18洞開放以來，迅速吸引國內外球手。

2. 設計與景觀  
球場布局充分利用山坡與周邊稻田，呈現壯麗全景。沙坑與水障礙戰略性布置，考驗球員擊球控制能力。

3. 草皮品質與維護  
果嶺被評為北部越南最美之一，球道依國際標準精心維護，配備自動灌溉系統與專業養護團隊。

4. 設施與服務  
現代會所設有更衣室、專業球具店、練習場及多元亞歐餐飲選擇。提供高爾夫球車租賃及設備（球桿、球鞋、雨傘），隨時滿足球手需求。

5. 體驗與建議  
靈活布局與不斷變化景觀，適合新手與專業球員。

6. 預訂  
請撥打(+84) 0123456789或訪問TeetimeVn.com線上預訂，獲取最佳優惠。
'
WHERE course_id = 52 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
Stone Highland ゴルフ＆リゾートは、バックザン省ヴィエットイェン地区に位置し、ハノイ中心部から車で約1.5時間（約90 km）です。

1. 概要と歴史  
Truong An Golf Companyにより開発され、山岳地形でのゴルフ体験と年間を通じて涼しい気候を提供。2023年末に最初の18ホールが完成して以来、国内外のゴルファーを迅速に魅了しています。

2. 設計と景観  
レイアウトは山腹地形と周囲の水田を活かし、雄大なパノラマビューを提供。バンカーとウォーターハザードは戦略的に配置され、ショットコントロール技術を試されます。

3. 芝質とメンテナンス  
グリーンは北部ベトナムで最も美しいものの一つと評され、フェアウェイは自動灌漑システムと専任チームによって国際基準で丁寧に管理されています。

4. 施設とサービス  
モダンなクラブハウスにはロッカー、プロショップ、ドライビングレンジ、アジアン‐ヨーロピアンレストランを完備。ゴルフカートレンタルやクラブ、シューズ、傘のレンタルサービスも利用可能です。

5. 体験とおすすめ  
柔軟なレイアウトと変化に富んだ景観により、初心者からプロまで楽しめます。

6. 予約  
(+84) 0123456789までお電話いただくか、TeetimeVn.comでオンライン予約をどうぞ。
'
WHERE course_id = 52 AND lang = 'ja';

UPDATE golf_course_i18n
SET overview = '
Stone Highland 골프 앤 리조트는 박장성 비엣옌 지역에 위치하며, 하노이 중심부에서 차로 약 1시간 30분(약 90 km) 거리에 있습니다.

1. 개요 및 역사  
Truong An Golf Company가 개발했으며, 산악 지형에서의 골프 경험과 연중 시원한 기후를 제공하도록 설계되었습니다. 2023년 말 첫 18홀 개장 이후 국내외 골퍼들의 사랑을 받고 있습니다.

2. 설계 및 경관  
코스 레이아웃은 산자락 지형과 주변 논을 활용하여 장엄한 파노라마 뷰를 제공합니다. 벙커와 워터 해저드는 전략적으로 배치되어 샷 컨트롤 기술을 테스트합니다.

3. 잔디 품질 및 유지 관리  
그린은 북부 베트남에서 가장 아름다운 것으로 평가받으며, 페어웨이는 자동 관개 시스템과 전문 관리 팀에 의해 국제 기준으로 관리됩니다.

4. 시설 및 서비스  
모던 클럽하우스에는 라커룸, 프로숍, 드라이빙 레인지, 아시안-유러피언 레스토랑이 있으며, 골프 카트 및 클럽, 신발, 우산 대여 서비스도 제공합니다.

5. 체험 및 추천  
유연한 레이아웃과 풍부한 경관 변화를 통해 초보자와 전문가 모두에게 적합합니다.

6. 예약  
(+84) 0123456789로 전화하거나 TeetimeVn.com에서 온라인 예약하세요.
'
WHERE course_id = 52 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = '
Yên Bái Star Golf & Resort tọa lạc tại Đường Âu Cơ, Minh Quân, Trấn Yên, Yên Bái, được khai trương năm 2018 và thiết kế bởi Peter John Waddell. Sân gồm 27 hố par-72 trải dài 6.975 yards, ôm trọn mặt hồ Minh Quân và những dải đồi cây xanh mát.

1. Tổng quan & Lịch sử  
Được khởi công xây dựng trong dự án du lịch sinh thái Yên Bái, Yên Bái Star Golf & Resort nhanh chóng trở thành điểm đến yêu thích với khí hậu mát mẻ quanh năm và tầm nhìn hướng hồ.

2. Thiết kế & Cảnh quan  
Sân tận dụng địa hình đồi tự nhiên và đường viền hồ để tạo ra những fairway uốn lượn, bunker trắng tinh và những hố nước phản chiếu khung cảnh thơ mộng.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens Bentgrass và fairway Sea Isle Paspalum được chăm sóc theo tiêu chuẩn USGA, với hệ thống tưới tự động thông minh và đội ngũ bảo trì chuyên nghiệp 24/7.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại bao gồm locker cao cấp, pro-shop, driving range, putting green, nhà hàng buffet Á-Âu, lounge và spa. Dịch vụ caddie, xe điện và huấn luyện viên PGA luôn sẵn sàng phục vụ.

5. Trải nghiệm & Gợi ý  
– Sáng sớm: sương mù nhẹ phủ trên mặt hồ Minh Quân.  
– Chiều tà: hoàng hôn nhuộm đỏ fairway và đồi thông.

6. Đặt chỗ  
Liên hệ (+84) 0789 00 1313 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 53 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = '
Yen Bai Star Golf & Resort is located on Au Co Road, Minh Quan, Tran Yen District, Yen Bai. Opened in 2018 and designed by Peter John Waddell, the course features 27 par-72 holes stretching 6,975 yards, embracing the shores of Minh Quan Lake and the surrounding verdant hills.

1. Overview & History  
Built as part of the Yen Bai eco-tourism project, Yen Bai Star Golf & Resort quickly became a favorite destination thanks to its year-round cool climate and panoramic lake views.

2. Design & Scenery  
The course leverages natural hill terrain and the lakeshore to create winding fairways, pristine white bunkers, and water holes that reflect the poetic landscape.

3. Turf Quality & Maintenance  
The greens use Bentgrass and the fairways use Sea Isle Paspalum, maintained to USGA standards with an intelligent automatic irrigation system and a professional maintenance team available 24/7.

4. Facilities & Services  
The modern clubhouse includes premium lockers, a pro shop, a driving range, a putting green, an Asian-European buffet restaurant, a lounge, and a spa. Caddie services, golf cart rentals, and PGA coaching are all available.

5. Experience & Recommendations  
– Early morning: light mist drifts over Minh Quan Lake.  
– Late afternoon: sunsets paint the fairways and pine-covered hills red.

6. Reservations  
Call (+84) 0789 00 1313 or book your tee time online at TeetimeVn.com for the best offers.
'
WHERE course_id = 53 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
越白星高尔夫度假村位于越白省陈安县明全镇欧纪路，2018年开业，由Peter John Waddell设计。球场由27个标准72杆球洞组成，全长6,975码，环抱明全湖岸及青葱山丘。

1. 概况与历史  
作为越白省生态旅游项目的一部分，越白星度假村凭借全年凉爽气候和湖景视野迅速成为热门目的地。

2. 设计与景观  
球场利用自然山丘地形和湖岸线，营造蜿蜒的球道、洁白的沙坑和倒映诗意景色的水障碍。

3. 草坪品质与维护  
果岭采用Bentgrass，球道采用Sea Isle Paspalum，按USGA标准维护，配备智能自动灌溉系统和24/7专业维护团队。

4. 设施与服务  
现代会所设有高级储物柜、专业球具店、练习场、推杆果岭、亚欧自助餐厅、休息厅和水疗中心。球童服务、高尔夫球车租赁和PGA教练课程全天候提供。

5. 体验与建议  
– 清晨：淡雾飘渺于明全湖面。  
– 傍晚：落日余晖将球道和松树林染成红色。

6. 预订  
请致电(+84) 0789 00 1313或登录TeetimeVn.com在线预订，获取优惠。
'
WHERE course_id = 53 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
越白星高爾夫度假村位於越白省陳安縣明全鎮歐紀路，2018年開業，由Peter John Waddell設計。球場由27個標準72桿球洞組成，總長6,975碼，環抱明全湖岸及青蔥山丘。

1. 概況與歷史  
作為越白省生態旅遊項目的一部分，越白星度假村憑藉全年涼爽氣候和湖景視野迅速成為熱門目的地。

2. 設計與景觀  
球場利用自然山丘地形和湖岸線，營造蜿蜒的球道、潔白的沙坑和倒映詩意景色的水障礙。

3. 草坪品質與維護  
果嶺採用Bentgrass，球道採用Sea Isle Paspalum，依USGA標準維護，配備智能自動灌溉系統和24/7專業維護團隊。

4. 設施與服務  
現代會所設有高級儲物櫃、專業球具店、練習場、推杆果嶺、亞歐自助餐廳、休息廳和水療中心。球童服務、高爾夫球車租賃及PGA教練課程全天候提供。

5. 體驗與建議  
– 早晨：淡霧飄渺於明全湖面。  
– 傍晚：落日餘暉將球道和松樹林染成紅色。

6. 預訂  
請撥打(+84) 0789 00 1313或登入TeetimeVn.com線上預訂，獲取優惠。
'
WHERE course_id = 53 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
イエンバイスターゴルフ＆リゾートは、イエンバイ省チャンイエン県ミンクアン鎮オーコー通りに位置し、2018年に開業、ピーター・ジョン・ワデルが設計を手がけました。コースは27ホール・パー72、全長6,975ヤードで、ミンクアン湖と緑豊かな丘陵に囲まれています。

1. 概要と歴史  
イエンバイのエコツーリズムプロジェクトの一環として建設され、年間を通じた涼しい気候と湖望の景観で開業後すぐに人気を博しました。

2. 設計と景観  
自然の丘陵地形と湖岸線を活かし、うねるフェアウェイ、純白のバンカー、詩情溢れる風景を映すウォーターハザードを配しています。

3. 芝質とメンテナンス  
グリーンにはベントグラス、フェアウェイにはシーアイル・パスパラムを使用し、USGA基準のスマートな自動灌漑システムと24時間体制のプロチームが管理しています。

4. 施設とサービス  
モダンなクラブハウスには高級ロッカー、プロショップ、ドライビングレンジ、パッティンググリーン、アジアン・ヨーロピアンビュッフェレストラン、ラウンジ、スパを完備。キャディサービス、ゴルフカートレンタル、PGAコーチレッスンを常時提供しています。

5. 体験とおすすめ  
– 早朝：ミンクアン湖面に立ち込める淡い霧。  
– 夕暮れ：フェアウェイと松林が夕日に染まる情景。

6. 予約  
(+84) 0789 00 1313までお電話いただくか、TeetimeVn.comでオンライン予約をどうぞ。
'
WHERE course_id = 53 AND lang = 'ja';

UPDATE golf_course_i18n
SET overview = '
옌바이 스타 골프 앤 리조트는 옌바이성 찐옌현 민꽌읍 아우코 로드에 위치해 있으며 2018년에 개장, 피터 존 와델이 설계했습니다. 코스는 파72 27홀, 총 길이 6,975야드로 민꽌 호수와 푸른 언덕에 둘러싸여 있습니다.

1. 개요 및 역사  
옌바이 생태 관광 프로젝트의 일환으로 조성되어 연중 시원한 기후와 호수 전경으로 개장 직후부터 골퍼들의 사랑을 받았습니다.

2. 설계 및 경관  
자연 언덕 지형과 호숫가를 활용한 구불구불한 페어웨이, 순백의 벙커, 시적인 풍경을 반사하는 워터 해저드를 배치했습니다.

3. 잔디 품질 및 유지 관리  
그린은 벤트그래스, 페어웨이는 씨아일 파스팔럼을 사용하며 USGA 기준의 스마트 자동 관개 시스템과 24시간 운영 전문 유지 관리 팀이 관리합니다.

4. 시설 및 서비스  
모던한 클럽하우스에는 고급 라커, 프로숍, 드라이빙 레인지, 퍼팅 그린, 아시안-유러피언 뷔페 레스토랑, 라운지, 스파가 있으며 캐디 서비스, 골프 카트 대여, PGA 코치 레슨을 제공합니다.

5. 체험 및 추천  
– 이른 아침: 민꽌 호수 위로 드리운 옅은 안개.  
– 늦은 오후: 페어웨이와 소나무 언덕이 노을빛 붉게 물드는 풍경.

6. 예약  
(+84) 0789 00 1313으로 전화하거나 TeetimeVn.com에서 온라인 예약하세요.
'
WHERE course_id = 53 AND lang = 'ko';


UPDATE golf_course_i18n
SET overview = '
Sa Pa Grand Golf Course tọa lạc dọc theo bờ sông Hồng, tại xã Bản Vược, huyện Bát Xát, tỉnh Lào Cai, cách thị trấn Sa Pa khoảng 30 km. Được thiết kế bởi Pacific Coast Design và khai trương năm 2024, sân 18 hố par 71 dài 6.656 yards, nằm ở độ cao hơn 1.600 mét so với mực nước biển—sân golf có độ cao nhất Việt Nam.

1. Tổng quan & Lịch sử  
Khởi nguồn từ dự án phát triển du lịch cao nguyên Sa Pa, Sa Pa Grand Golf Course nhanh chóng thu hút golfer trong và ngoài nước nhờ khí hậu mát lạnh quanh năm và cảnh quan hoang sơ.

2. Thiết kế & Cảnh quan  
Sân tận dụng địa hình đồi núi với fairway uốn lượn qua đồi thông và thung lũng, xen kẽ bunker trắng và bẫy nước từ sông Hồng.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens Bentgrass và fairway Platinum Paspalum được chăm sóc theo tiêu chuẩn USGA với hệ thống tưới tự động và đội ngũ chăm sóc sân chuyên nghiệp.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại với pro-shop, driving range và putting green; dịch vụ caddie chuyên nghiệp, xe điện và các nhà hàng, quán café phục vụ ẩm thực quốc tế.

5. Trải nghiệm & Gợi ý  
– Buổi sáng sương mù bao phủ đỉnh Hoàng Liên Sơn.  
– Buổi chiều hoàng hôn buông trên dòng sông Hồng.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 54 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = '
Sa Pa Grand Golf Course is located along the Red River bank in Ban Vược Commune, Bát Xát District, Lào Cai Province—about 30 km from Sa Pa town. Designed by Pacific Coast Design and opened in 2024, this 18-hole, par-71 course stretches 6,656 yards and sits above 1,600 meters above sea level, making it the highest-altitude golf course in Vietnam.

1. Overview & History  
Born from the Sa Pa highland tourism development project, Sa Pa Grand Golf Course quickly drew domestic and international golfers with its year-round cool climate and pristine mountain scenery.

2. Design & Scenery  
The layout harnesses the hilly terrain, with fairways winding through pine forests and valleys, interspersed with white sand bunkers and natural water hazards fed by the Red River.

3. Turf Quality & Maintenance  
Greens use Bentgrass and fairways use Platinum Paspalum, all maintained to USGA standards with an automated irrigation system and a dedicated turf-care team.

4. Facilities & Services  
The modern clubhouse features a pro shop, driving range, and putting green. Professional caddies, electric carts, and on-site restaurants and cafés serving international cuisine are available to guests.

5. Experience & Recommendations  
– Morning: enjoy mist rolling over the Hoàng Liên Sơn peaks.  
– Afternoon: take in the sunset over the Red River.

6. Reservations  
Call (+84) 0123456789 or book your tee time online at TeetimeVn.com for the best deals.
'
WHERE course_id = 54 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
萨帕格兰德高尔夫球场位于老街省八斋县班越社红河沿岸，距离萨帕镇约30公里。由Pacific Coast Design设计，2024年开业。球场为18洞72杆，长6,656码，海拔超过1,600米，是越南海拔最高的高尔夫球场。

1. 概况与历史  
萨帕高原旅游发展项目的一部分，凭借全年凉爽气候和原始山地景观，很快吸引了国内外球手。

2. 设计与景观  
球场利用丘陵地形，球道穿行于松林和山谷之间，点缀白色沙坑和源自红河的天然水障碍。

3. 草坪质量与维护  
果岭采用Bentgrass，球道采用Platinum Paspalum，按USGA标准维护，配备自动灌溉系统和专业养护团队。

4. 设施与服务  
现代会所设有专业球具店、练习场和推杆果岭。提供专业球童、电动球车及供应国际美食的餐厅和咖啡厅。

5. 体验与建议  
– 清晨：欣赏雾气笼罩的Hoàng Liên Sơn山峰。  
– 下午：观赏红河上的日落。

6. 预订  
请致电(+84)0123456789或访问TeetimeVn.com在线预订，享受优惠。
'
WHERE course_id = 54 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
薩帕格蘭德高爾夫球場位於老街省八載縣班越社紅河沿岸，距薩帕鎮約30公里。由Pacific Coast Design設計，2024年開業。球場為18洞72桿，長6,656碼，海拔超過1,600米，是越南海拔最高的高爾夫球場。

1. 概況與歷史  
薩帕高原旅遊發展專案的一部分，憑藉全年涼爽氣候與原始山地景觀，迅速吸引國內外球手。

2. 設計與景觀  
球場利用丘陵地形，球道穿行於松林與山谷之間，點綴白色沙坑和源自紅河的天然水障礙。

3. 草坪品質與維護  
果嶺採用Bentgrass，球道採用Platinum Paspalum，依USGA標準維護，配備自動灌溉系統與專業養護團隊。

4. 設施與服務  
現代會所設有專業球具店、練習場及推桿果嶺。提供專業球童、電動球車及供應國際美食的餐廳與咖啡廳。

5. 體驗與建議  
– 清晨：欣賞霧氣籠罩的Hoàng Liên Sơn山峰。  
– 下午：觀賞紅河上的日落。

6. 預訂  
請撥打(+84)0123456789或訪問TeetimeVn.com線上預訂，享受優惠。
'
WHERE course_id = 54 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
サパグランドゴルフコースは、ラオカイ省バットサット県バンヴィエック村の紅河沿いに位置し、サパタウンから約30kmです。Pacific Coast Designによる設計で2024年に開場。18ホール、パー71、全長6,656ヤード、海抜1,600メートル超で、ベトナム最高峰のゴルフコースです。

1. 概要と歴史  
サパ高原ツーリズム開発プロジェクトの一環として誕生し、年間を通じた涼しい気候と手つかずの山岳景観で、国内外のゴルファーを魅了しています。

2. 設計と景観  
丘陵地形を活かし、フェアウェイは松林と谷間を縫うように走り、白砂のバンカーと紅河由来の天然ウォーターハザードが散りばめられています。

3. 芝質とメンテナンス  
ベントグラスグリーンとプラチナパスパラムフェアウェイをUSGA基準で管理し、自動灌漑システムと専門チームが常時メンテナンスします。

4. 施設とサービス  
モダンなクラブハウスにはプロショップ、ドライビングレンジ、パッティンググリーンを完備。プロキャディ、電動カート、国際料理を提供するレストランやカフェが利用可能です。

5. 体験とおすすめ  
– 早朝：霧に包まれたホアンリエン山の峰々を堪能。  
– 午後：紅河に沈む夕日を眺める。

6. 予約  
(+84) 0123456789までお電話、またはTeetimeVn.comでオンライン予約をどうぞ。
'
WHERE course_id = 54 AND lang = 'ja';

UPDATE golf_course_i18n
SET overview = '
사파 그랜드 골프 코스는 라오까이성 바트삿군 반뷱 마을 홍강 강변에 위치하며, 사파 타운에서 약 30km 거리에 있습니다. Pacific Coast Design이 설계하고 2024년에 개장한 이 코스는 18홀 파71, 전장 6,656야드, 해발 1,600m 이상으로 베트남에서 가장 높은 골프 코스입니다.

1. 개요 및 역사  
사파 고원 관광 개발 프로젝트의 일환으로 조성되어 연중 시원한 기후와 자연 그대로의 산악 경관으로 국내외 골퍼들의 관심을 모았습니다.

2. 설계 및 경관  
언덕 지형을 활용해 페어웨이는 소나무 숲과 계곡을 가로지르며, 흰 모래 벙커와 홍강에서 유입된 천연 워터 해저드를 배치했습니다.

3. 잔디 품질 및 유지 관리  
그린은 벤트그래스를, 페어웨이는 플래티넘 파스팔럼을 사용하며 USGA 기준의 자동 관개 시스템과 전문 유지 관리 팀이 24시간 관리합니다.

4. 시설 및 서비스  
모던한 클럽하우스에는 프로숍, 드라이빙 레인지, 퍼팅 그린이 있으며 전문 캐디, 전동 카트, 국제 요리를 제공하는 레스토랑과 카페를 이용할 수 있습니다.

5. 체험 및 추천  
– 이른 아침: 안개에 싸인 호앙리엔산의 봉우리를 감상하세요.  
– 오후: 홍강에 비치는 아름다운 일몰을 즐기세요.

6. 예약  
(+84) 0123456789로 전화하거나 TeetimeVn.com에서 온라인 예약하세요.
'
WHERE course_id = 54 AND lang = 'ko';

-- course_id = 55 (Corn Hill Golf & Resort), lang = vi
UPDATE golf_course_i18n
SET overview = '
Corn Hill Golf & Resort tọa lạc tại thôn An Phú, xã Khám Lạng, huyện Lục Nam, tỉnh Bắc Giang, cách trung tâm Hà Nội khoảng 70 km, trên diện tích 148 ha. Sân có 36 hố par 72, chiều dài 7.185 yards, do Brett Mogg (hợp tác với Nelson & Haworth) thiết kế và chính thức khai trương năm 2024.

1. Tổng quan & Lịch sử  
Dự án khởi công năm 2020, Corn Hill nhanh chóng trở thành điểm đến lý tưởng cho golfer trong và ngoài nước, với khí hậu mát mẻ quanh năm và khung cảnh thiên nhiên hùng vĩ.

2. Thiết kế & Cảnh quan  
Fairway uốn lượn trên đồi thoai thoải, xen kẽ các bunker cát trắng và hồ nước nhân tạo, tạo nên thử thách và khung cảnh nghệ thuật đầy ấn tượng.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens bentgrass và fairway Paspalum được chăm sóc theo tiêu chuẩn USGA, kết hợp hệ thống tưới tự động và đội ngũ bảo dưỡng chuyên nghiệp hoạt động 24/7.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại với locker cao cấp, pro-shop, driving range, putting green, nhà hàng ẩm thực Á—Âu, lounge và spa. Caddie chuyên nghiệp và huấn luyện viên PGA luôn sẵn sàng phục vụ.

5. Trải nghiệm & Gợi ý  
– Chơi sáng sớm để tận hưởng màn sương mỏng trên fairway.  
– Trải nghiệm hoàng hôn rực rỡ tại hố 9 với tầm nhìn toàn cảnh.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVN.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 55 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = '
Corn Hill Golf & Resort is located in An Phú Hamlet, Khám Lạng Commune, Lục Nam District, Bắc Giang Province—about 70 km from central Hanoi—on 148 ha. The resort features 36 par-72 holes over 7,185 yards, designed by Brett Mogg in collaboration with Nelson & Haworth, and officially opened in 2024.

1. Overview & History  
Ground broken in 2020, Corn Hill quickly became an ideal destination for domestic and international golfers, thanks to its year-round cool climate and majestic natural scenery.

2. Design & Scenery  
Fairways wind across gentle hills, interspersed with white sand bunkers and man-made lakes, creating impressive challenges and artistic vistas.

3. Turf Quality & Maintenance  
Bentgrass greens and Paspalum fairways are maintained to USGA standards with an automatic irrigation system and a professional maintenance team operating 24/7.

4. Facilities & Services  
The modern clubhouse features premium lockers, a pro shop, a driving range, a putting green, an Asian-European restaurant, a lounge, and a spa. Professional caddies and PGA coaches are always on hand.

5. Experience & Recommendations  
– Play early to enjoy the morning mist over the fairways.  
– Experience the spectacular sunset at hole 9 with panoramic views.

6. Reservations  
Call (+84) 0123456789 or book your tee time online at TeetimeVN.com for the best offers.
'
WHERE course_id = 55 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
Corn Hill 高尔夫度假村位于北江省陆南县检查社安富村，距河内市中心约70 公里，占地148 公顷。球场拥有36个标准72杆球洞，全长7,185 码，由Brett Mogg与Nelson & Haworth合作设计，2024年正式开业。

1. 概况与历史  
项目于2020年动工，Corn Hill凭借全年凉爽气候和壮丽自然风光迅速成为国内外球手的理想目的地。

2. 设计与景观  
球道在缓坡山丘上蜿蜒，间或分布白色沙坑和人工湖，营造出令人印象深刻的挑战和艺术化景观。

3. 草坪质量与维护  
果岭采用Bentgrass，球道采用Paspalum，按USGA标准维护，配备自动灌溉系统和24/7专业维护团队。

4. 设施与服务  
现代会所设有高级储物柜、专业球具店、练习场、推杆果岭、亚欧餐厅、休息室和水疗中心。专业球童与PGA教练随时待命。

5. 体验与建议  
– 清晨挥杆可欣赏球道上的薄雾。  
– 在9号洞体验全景日落的壮丽。

6. 预订  
请致电(+84) 0123456789或登录TeetimeVN.com在线预订，以获取最佳优惠。
'
WHERE course_id = 55 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
Corn Hill 高爾夫渡假村位於北江省陸南縣檢查社安富村，距河內市中心約70 公里，佔地148 公頃。球場擁有36個標準72桿球洞，總長7,185 碼，由Brett Mogg與Nelson & Haworth合作設計，於2024年正式開幕。

1. 概況與歷史  
專案於2020年動工，Corn Hill憑藉全年涼爽氣候與壯麗自然風光迅速成為國內外球手的理想之選。

2. 設計與景觀  
球道沿緩坡山丘蜿蜒，間或分布白色沙坑與人工湖，營造令人印象深刻的挑戰與藝術化景觀。

3. 草皮品質與維護  
果嶺採用Bentgrass，球道採用Paspalum，依USGA標準維護，配備自動灌溉系統與24/7專業維護團隊。

4. 施設與服務  
現代化會所設有高級儲物櫃、專業球具店、練習場、推桿果嶺、亞歐餐廳、休息室及水療中心。專業球童與PGA教練隨時待命。

5. 體驗與建議  
– 清晨揮桿可欣賞球道上的薄霧。  
– 在9號洞體驗全景日落的壯麗。

6. 預訂  
請撥打(+84) 0123456789或登入TeetimeVN.com線上預訂，獲取最佳優惠。
'
WHERE course_id = 55 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
Corn Hill Golf & Resortはバクザン省ルックナム県チェックラン社アンフ村に位置し、ハノイ中心部から約70 km、敷地面積148 haを誇ります。コースはパー72×36ホール、全長7,185 ヤードで、Brett MoggがNelson & Haworthと協力して設計し、2024年に開業しました。

1. 概要と歴史  
プロジェクトは2020年に着工。Corn Hillは年間を通じた涼しい気候と雄大な自然景観により、国内外のゴルファーにとって理想的な目的地となっています。

2. 設計と景観  
フェアウェイは緩やかな丘陵地を蛇行し、白砂のバンカーや人工池が点在して印象的なチャレンジと芸術的景観を演出します。

3. 芝質とメンテナンス  
ベントグラスのグリーンとパスパラムのフェアウェイはUSGA基準で管理され、自動灌漑システムと24時間体制の専門チームが維持します。

4. 施設とサービス  
モダンなクラブハウスには高級ロッカー、プロショップ、ドライビングレンジ、パッティンググリーン、アジアン・ヨーロピアンレストラン、ラウンジ、スパを完備。プロキャディとPGAコーチが常時サポートします。

5. 体験とおすすめ  
– 早朝プレーでフェアウェイに立ち込める霧を満喫。  
– 9番ホールでパノラマのサンセットを体験。

6. 予約  
(+84) 0123456789までお電話、またはTeetimeVN.comでオンライン予約をどうぞ。
'
WHERE course_id = 55 AND lang = 'ja';

UPDATE golf_course_i18n
SET overview = '
Corn Hill Golf & Resort는 박장성 룩남현 검사랑사 안푸촌에 위치하며, 하노이 중심부에서 약70 km, 148 ha 부지를 차지합니다. 파72 36홀, 전장7,185 야드로 구성되며, Brett Mogg이 Nelson & Haworth와 협력해 설계했으며 2024년 공식 개장했습니다.

1. 개요 및 역사  
프로젝트는 2020년에 착공되었으며, Corn Hill은 연중 시원한 기후와 웅장한 자연 경관으로 국내외 골퍼들에게 이상적인 목적지로 자리 잡았습니다.

2. 설계 및 경관  
페어웨이는 완만한 구릉 지형을 따라 구불구불 연결되며, 흰 모래 벙커와 인공 호수가 곳곳에 배치되어 인상적인 도전과 예술적 경관을 연출합니다.

3. 잔디 품질 및 유지 관리  
그린은 벤트그래스, 페어웨이는 파스팔럼을 사용하며 USGA 기준에 따라 자동 관개 시스템과 24시간 운영되는 전문 유지 관리 팀이 관리합니다.

4. 시설 및 서비스  
현대적인 클럽하우스에는 고급 라커룸, 프로숍, 드라이빙 레인지, 퍼팅 그린, 아시안-유러피언 레스토랑, 라운지, 스파가 갖추어져 있습니다. 전문 캐디와 PGA 코치가 항상 지원합니다.

5. 체험 및 추천  
– 이른 아침 라운드로 페어웨이에 드리운 안개를 만끽하세요.  
– 9번 홀에서 파노라마 일몰을 경험하세요.

6. 예약  
(+84) 0123456789로 전화하시거나 TeetimeVN.com에서 온라인 예약하세요.
'
WHERE course_id = 55 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = '
Văn Lang Empire Golf Club tọa lạc trong quần thể đô thị Tam Nông Legendary, xã Hương Nộn, huyện Tam Nông, tỉnh Phú Thọ, cách Hà Nội khoảng 120 km (khoảng 2 giờ lái xe). Sân trải dài trên diện tích 168 ha bên bờ hồ Ngòi Hoa, là dự án sân golf 36 hố đẳng cấp quốc tế đầu tiên tại khu vực Bắc Bộ do huyền thoại Greg Norman thiết kế, với giai đoạn đầu gồm 18 hố par-72, chiều dài 7.300 yards, khai trương tháng 10/2024 và dự kiến hoàn thiện toàn bộ 36 hố vào Q2/2025.

1. Tổng quan & Lịch sử  
Được phát triển bởi T&T Golf thuộc Tập đoàn T&T, Văn Lang Empire ra đời nhằm kết hợp giá trị lịch sử văn hóa Nhà nước Văn Lang với trải nghiệm golf hiện đại. Ngay khi giai đoạn 1 đi vào hoạt động, sân đã thu hút sự quan tâm của cộng đồng golfer trong nước và quốc tế.

2. Thiết kế & Cảnh quan  
Với cảm hứng từ truyền thuyết Sơn Tinh – Thủy Tinh, mỗi hố golf tái hiện dấu ấn văn hóa Việt Nam qua bunker trắng, hồ nước tự nhiên và tán rừng thông xanh mát. Fairway uốn lượn theo địa hình đồi núi và mực nước hồ thay đổi.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens sử dụng Bentgrass, fairway cỏ Paspalum pha Zoysia, được chăm sóc theo tiêu chuẩn USGA. Hệ thống tưới phun sương thông minh và đội ngũ chăm sóc sân 24/7 đảm bảo bề mặt chơi luôn mượt mà.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse sang trọng với locker cao cấp, pro-shop, driving range, putting green, nhà hàng buffet Á – Âu, lounge trên đồi và spa. Caddie chuyên nghiệp, HLV PGA và phòng Golf Simulator sẵn sàng phục vụ.

5. Trải nghiệm & Gợi ý  
– Sáng sớm: sương mù trên mặt hồ và rừng thông.  
– Chiều muộn: hoàng hôn nhuộm đỏ dãy núi Hùng Vương.  
– Đừng bỏ lỡ trải nghiệm chơi golf đêm với đèn LED hoành tráng.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 56 AND lang = 'vi';


UPDATE golf_course_i18n
SET overview = '
Văn Lang Empire Golf Club is located within the Tam Nong Legendary urban complex in Huong Non Commune, Tam Nong District, Phu Tho Province—about 120 km from Hanoi (a roughly 2-hour drive). The course spans 168 ha along the shore of Ngoi Hoa Lake and is the first 36-hole, international-standard golf project in Northern Vietnam designed by the legendary Greg Norman. Phase 1 features 18 par-72 holes over 7,300 yards, opened in October 2024, with full completion of all 36 holes expected in Q2 2025.

1. Overview & History  
Developed by T&T Golf of the T&T Group, Văn Lang Empire marries the historical and cultural heritage of the ancient Văn Lang State with a modern golf experience. From the moment Phase 1 launched, it captivated both domestic and international golfers.

2. Design & Scenery  
Inspired by the Sơn Tinh–Thủy Tinh legend, each hole evokes Vietnamese cultural motifs through white sand bunkers, natural water hazards, and verdant pine canopies. Fairways meander along rolling hills and changing lake levels.

3. Turf Quality & Maintenance  
Greens use Bentgrass and fairways a Paspalum–Zoysia blend, all maintained to USGA standards. An intelligent mist irrigation system and a 24/7 turf-care team ensure perfectly smooth surfaces.

4. Facilities & Services  
A luxurious clubhouse offers premium lockers, a pro shop, a driving range, a putting green, an Asian-European buffet restaurant, a hilltop lounge, and a spa. Professional caddies, PGA coaches, and a golf simulator are on standby.

5. Experience & Recommendations  
– Early morning: mist over the lake and pine forests.  
– Late afternoon: sunsets painting the Hùng Vương range red.  
– Don''t miss the spectacular LED-lit night golf experience.

6. Reservations  
Call (+84) 0123456789 or book your tee time online at TeetimeVn.com for the best offers.
'
WHERE course_id = 56 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
文朗帝国高尔夫俱乐部位于富寿省潭农县香农社潭农传奇城市综合体内，距离河内约120 公里（车程约2小时）。球场占地168 公顷，沿芽花湖湖岸延伸，是北部地区首个由传奇球手格雷格·诺曼设计的36洞国际标准高尔夫项目。第一期包括18个标准72杆球洞，总长7,300 码，于2024年10月开幕，预计2025年第二季度完成所有36洞。

1. 概况与历史  
由T&T集团旗下T&T高尔夫开发，文朗帝国旨在将古代文朗国的历史文化与现代高尔夫体验融合。第一期运营伊始，便吸引了国内外高尔夫球手的关注。

2. 设计与景观  
以“山精—水精”传说为灵感，每个球洞通过白色沙坑、天然水障和茂密松林呈现越南文化印记。球道沿丘陵地形和变化的湖面蜿蜒。

3. 草坪质量与维护  
果岭采用Bentgrass，球道采用Paspalum–Zoysia混合草种，按USGA标准精心维护。智能喷雾灌溉系统和24/7养护团队确保场地始终平滑。

4. 设施与服务  
豪华会所配备高级储物柜、专业球具店、练习场、推杆果岭、亚欧自助餐厅、山顶休息区和水疗中心。专业球童、PGA教练以及高尔夫模拟器随时待命。

5. 体验与建议  
– 清晨：湖面与松林上的薄雾。  
– 傍晚：夕阳将雄王山脉染成赤红。  
– 不要错过壮观的LED夜间高尔夫体验。

6. 预订  
请致电(+84) 0123456789或访问TeetimeVn.com在线预订，获取最佳优惠。
'
WHERE course_id = 56 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
文朗帝國高爾夫俱樂部位於富壽省潭農縣香農社潭農傳奇城市綜合體，距河內約120 公里（車程約2小時）。場地占地168 公頃，沿芽花湖湖岸展開，是北部首個由傳奇球手格雷格·諾曼設計的36洞國際標準高爾夫項目。第一期包括18個標準72桿球洞，全長7,300 碼，於2024年10月開幕，預計2025年第2季度完工所有36洞。

1. 概況與歷史  
由T&T集團旗下T&T高爾夫開發，文朗帝國旨在將古代文朗國歷史文化與現代高爾夫體驗結合。第一期運營後，立即吸引國內外愛好者矚目。

2. 設計與景觀  
以「山精—水精」傳說為靈感，每個球洞透過白色沙坑、天然水障和茂密松林重現越南文化韻味。球道沿山丘地形與變幻湖面蜿蜒。

3. 草皮品質與維護  
果嶺採用Bentgrass，球道採用Paspalum–Zoysia混合草種，依USGA標準細心維護。智慧噴霧灌溉系統與24/7養護團隊確保場地最佳狀態。

4. 施設與服務  
豪華會所配備高級儲物櫃、專業球具店、練習場、推杆果嶺、亞歐自助餐廳、山頂休息室和水療中心。專業球童、PGA教練及高爾夫模擬器隨時待命。

5. 體驗與建議  
– 清晨：湖面與松林上的薄霧。  
– 傍晚：夕陽染紅雄王山脈。  
– 別錯過壯觀的LED夜間高爾夫體驗。

6. 預訂  
請撥打(+84) 0123456789或訪問TeetimeVn.com線上預訂，尊享優惠。
'
WHERE course_id = 56 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
ヴァンラングエンパイアゴルフクラブは、フートー省タムノン県フオンノン社のタムノンレジェンダリー都市複合施設内に位置し、ハノイから約120 km（車で約2時間）です。168 haの敷地はゴンホア湖畔に広がり、伝説的ゴルファー グレッグ・ノーマンが設計した36ホール国際標準ゴルフプロジェクトとして、2024年10月に第1フェーズ（パー72×18ホール、全長7,300 ヤード）が開業。全36ホールは2025年第2四半期に完成予定です。

1. 概要と歴史  
T&Tグループ傘下のT&Tゴルフが開発し、古代文朗国家の歴史文化的価値と現代的ゴルフ体験を融合。第1フェーズ開業後、国内外のゴルファーコミュニティから注目を集めました。

2. 設計と景観  
山神・水神の伝説にインスパイアされ、各ホールには白砂バンカー、自然ウォーターハザード、青々とした松林を配してベトナム文化を表現。フェアウェイは丘陵地形と湖面の変化を生かして曲線的に配置。

3. 芝質とメンテナンス  
グリーンはベントグラス、フェアウェイはパスパラムとゾイシアの混合芝を敷設。USGA基準のスマートミスト灌漑システムと24時間稼働のターフケアチームが常時メンテナンス。

4. 施設とサービス  
高級ロッカールーム、プロショップ、ドライビングレンジ、パッティンググリーン、アジアン・ヨーロピアンビュッフェレストラン、ヒルトップラウンジ、スパを完備。プロキャディ、PGAコーチ、ゴルフシミュレーターも利用可能。

5. 体験とおすすめ  
– 早朝：湖面と松林に立ち込める霧を楽しむ。  
– 夕刻：雄王山脈を紅く染めるサンセットを堪能。  
– LED照明下の夜間ゴルフ体験もお見逃しなく。

6. 予約  
(+84) 0123456789までお電話いただくか、TeetimeVn.comでオンライン予約をどうぞ。
'
WHERE course_id = 56 AND lang = 'ja';

UPDATE golf_course_i18n
SET overview = '
반랑 엠파이어 골프 클럽은 푸토성 탐농현 흥년사 탐농 레전더리 도시 단지 내에 위치하며, 하노이에서 약120 km(차로 약2시간) 떨어져 있습니다. 168 ha 부지에 자리잡은 이 36홀 국제표준 코스는 전설적 골퍼 그렉 노먼이 설계했으며, 2024년10월 제1단계(파72×18홀, 전장7,300야드)가 개장했습니다. 전체36홀은2025년2분기 완공 예정입니다.

1. 개요 및 역사  
T&T 그룹 계열사 T&T 골프가 개발하여 고대 반랑 국가의 역사문화적 가치를 현대 골프 경험과 결합했습니다. 1단계 개장 후 국내외 골퍼 커뮤니티의 주목을 받았습니다.

2. 설계 및 경관  
산신·수신 전설에서 영감을 받아 각 홀에 흰 모래 벙커, 자연 워터 해저드, 울창한 소나무 숲을 배치, 베트남 문화의 정수를 표현합니다. 페어웨이는 구릉 지형 및 변화하는 호면을 따라 곡선으로 조성되었습니다.

3. 잔디 품질 및 유지 관리  
그린은 벤트그래스, 페어웨이는 파스팔럼–조이시아 혼합 잔디를 사용하며, USGA 기준의 스마트 미스트 관개 시스템과 24시간 운영 터프 케어 팀이 최상의 코스 컨디션을 유지합니다.

4. 시설 및 서비스  
고급 라커룸, 프로숍, 드라이빙 레인지, 퍼팅 그린, 아시안-유러피언 뷔페 레스토랑, 힐탑 라운지 및 스파를 갖춘 호화 클럽하우스. 프로 캐디, PGA 코치, 골프 시뮬레이터 서비스도 제공됩니다.

5. 체험 및 추천  
– 이른 아침: 호수와 소나무 숲에 드리운 안개를 감상하세요.  
– 늦은 오후: 웅왕산맥을 붉게 물들이는 일몰을 즐기세요.  
– LED 조명 속의 야간 골프 경험도 놓치지 마세요.

6. 예약  
(+84) 0123456789로 전화하거나 TeetimeVn.com에서 온라인 예약하세요.
'
WHERE course_id = 56 AND lang = 'ko';

"""

# Thực thi nhiều lệnh cùng lúc
cur.executescript(sql)

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("Đã cập nhật xong overview")
