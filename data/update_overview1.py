#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
# Mở kết nối
conn = sqlite3.connect('data/teetimevn_dev.db')
cur = conn.cursor()

# Block cập nhật address cho course_id = 1
sql = """-- course_id = 1 (BRG Kings Island Golf Resort), lang = vi
UPDATE golf_course_i18n
SET overview = '
BRG Kings Island Golf Resort tọa lạc tại Đồng Mô, thị xã Sơn Tây, Hà Nội, cách trung tâm Hà Nội khoảng 36 km và sân bay Nội Bài 45 km. Trên diện tích 350 ha bên hồ Đồng Mô, khu nghỉ dưỡng gồm ba sân 18 hố par 72: Lakeside (khai trương 1993), Mountainview (2004) và Kings Course (2018). Golfer có thể di chuyển bằng thuyền hoặc ô tô, trải nghiệm fairway uốn lượn giữa đồi cây và mặt nước, với 14/18 hố Lakeside có chướng ngại nước.

1. Tổng quan & Lịch sử  
Là tổ hợp gôn 54 hố đầu tiên miền Bắc, BRG Kings Island nhanh chóng khẳng định vị thế quốc tế từ năm 1993, liên tục tổ chức giải nghiệp dư quốc gia và là điểm tập luyện của nhiều golfer chuyên nghiệp.

2. Thiết kế & Cảnh quan  
– Lakeside: fairway dốc nhẹ, nước xuất hiện ở 14 hố.  
– Mountainview: tận dụng đường nét địa hình đồi tự nhiên.  
– Kings Course: kết hợp bunker phức hợp và fairway rộng mở.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens Bentgrass và fairway Paspalum–Zoysia được chăm sóc theo tiêu chuẩn USGA với hệ thống tưới tự động 24/7.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại bao gồm locker cao cấp, pro-shop, driving range, putting green, spa, hồ bơi và phòng Golf Simulator. Dịch vụ caddie chuyên nghiệp luôn sẵn sàng phục vụ.

5. Trải nghiệm & Gợi ý  
– Khởi đầu bằng chuyến thuyền qua hồ Đồng Mô.  
– Sáng sớm sương mù trên mặt nước, hoàng hôn rực rỡ phản chiếu lên fairway.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 1 AND lang = 'vi';

-- course_id = 1 (BRG Kings Island Golf Resort), lang = en
UPDATE golf_course_i18n
SET overview = '
BRG Kings Island Golf Resort is located in Dong Mo, Son Tay Town, Hanoi—36 km from central Hanoi and 45 km from Noi Bai Airport. Set on 350 ha beside Dong Mo Lake, the resort features three par-72, 18-hole courses: Lakeside (opened 1993), Mountainview (2004), and Kings Course (2018). Golfers access by boat or car and navigate fairways winding through rolling terrain and water hazards on 14 of 18 Lakeside holes.

1. Overview & History  
As Northern Vietnam’s first 54-hole facility, BRG Kings Island set the international standard in 1993 and has since hosted national amateur championships and trained professional players.

2. Course Design & Scenery  
– Lakeside: gentle slopes and water hazards on 14 holes.  
– Mountainview: natural hillside contours.  
– Kings Course: expansive fairways and complex bunker layouts.

3. Turf Quality & Maintenance  
Bentgrass greens and Paspalum–Zoysia fairways are maintained to USGA standards with 24/7 automated irrigation.

4. Facilities & Services  
The modern clubhouse offers premium lockers, a pro shop, driving range, putting greens, spa, swimming pool, and Golf Simulator. Professional caddies are always on hand.

5. Experience & Tips  
– Begin with a scenic boat transfer across Dong Mo Lake.  
– Enjoy morning mist on the water or golden sunsets across the fairways.

6. Booking  
Call (+84) 0123456789 or book online at TeetimeVn.com for best rates.
'
WHERE course_id = 1 AND lang = 'en';

-- course_id = 1 (BRG Kings Island Golf Resort), lang = zh-CN
UPDATE golf_course_i18n
SET overview = '
BRG Kings Island 高尔夫度假村位于河内市Sơn Tây区Đồng Mô湖畔，距市中心36公里，距Nội Bài机场45公里。度假区占地350公顷，拥有三座18洞标准杆72杆球场：Lakeside（1993年开业）、Mountainview（2004年）和Kings Course（2018年）。球手可乘船或驾车进入，14个Lakeside球洞均有水障碍。

1. 概览与历史  
作为北部越南首个54洞综合体，BRG Kings Island自1993年起确立国际标准，承办全国业余锦标赛并为职业球手提供训练场地。

2. 设计与景观  
– Lakeside：地形起伏，14洞穿水。  
– Mountainview：自然山坡轮廓。  
– Kings Course：宽阔球道与复杂沙坑布局。

3. 草坪品质与维护  
果岭采用Bentgrass，球道为Paspalum–Zoysia，依据USGA标准并配备24/7自动灌溉系统。

4. 配套设施与服务  
现代化会所设有高级储物柜、专业球具店、练习场、果岭练习区、SPA、泳池及高尔夫模拟器。

5. 体验与建议  
– 搭乘游船穿越Đồng Mô湖开启行程。  
– 清晨薄雾与黄昏余晖为理想球时。

6. 预订方式  
致电 (+84) 0123456789 或访问 TeetimeVn.com 在线预订，享受优惠。
'
WHERE course_id = 1 AND lang = 'zh-CN';

-- course_id = 1 (BRG Kings Island Golf Resort), lang = zh-TW
UPDATE golf_course_i18n
SET overview = '
BRG Kings Island 高爾夫度假村位於河內市Sơn Tây區Đồng Mô湖畔，距市中心36公里，距Nội Bài機場45公里。度假區占地350公頃，設有三座18洞標準桿72桿球場：Lakeside（1993年開幕）、Mountainview（2004年）、Kings Course（2018年）。球手可乘船或駕車前往，Lakeside的14洞均設水障礙。

1. 總覽與歷史  
作為北越第一座54洞綜合體，BRG Kings Island自1993年起樹立國際標準，承辦全國業餘錦標賽並為職業球手訓練。

2. 設計與景觀  
– Lakeside：地形起伏，14洞穿越水障礙。  
– Mountainview：自然山坡輪廓。  
– Kings Course：寬廣球道與複雜沙坑配置。

3. 草坪品質與維護  
果嶺採用Bentgrass，球道為Paspalum–Zoysia，依USGA標準並配備24/7自動灌溉系統。

4. 施設與服務  
現代化會所設有高級儲物櫃、專業球具店、練習場、果嶺練習區、SPA、泳池及高爾夫模擬器。

5. 體驗與建議  
– 乘坐遊船遊覽Đồng Mô湖開啟高爾夫之旅。  
– 清晨薄霧與黃昏霞光為理想球時。

6. 預訂方式  
請致電 (+84) 0123456789 或造訪 TeetimeVn.com 線上預訂，享受優惠。
'
WHERE course_id = 1 AND lang = 'zh-TW';

-- course_id = 1 (BRG Kings Island Golf Resort), lang = ja
UPDATE golf_course_i18n
SET overview = '
BRG Kings Island ゴルフリゾートは、ハノイ市Sơn Tây区Đồng Mô湖畔に位置し、市街中心部から約36km、Nội Bài空港から45kmです。350haの敷地に、18ホール・パー72コースが3つあります：Lakeside（1993年開業）、Mountainview（2004年）、Kings Course（2018年）。フェアウェイは起伏に富み、Lakesideの14ホールにはウォーターハザードが配されています。

1. 概要と歴史  
北部ベトナム初の54ホール施設として1993年に設立され、国内アマチュア選手権を開催し、プロ選手のトレーニング場としても高く評価されています。

2. コースデザイン＆景観  
– Lakeside：緩やかな起伏と14ホールの水障害。  
– Mountainview：自然の丘陵地形を活かしたレイアウト。  
– Kings Course：広々としたフェアウェイと複雑なバンカー配置。

3. 芝の品質＆メンテナンス  
ベントグラスのグリーンとパスパルム–ゾイシアのフェアウェイはUSGA基準で管理され、自動灌漑システムが24時間稼働。

4. 施設＆サービス  
モダンクラブハウスには高級ロッカー、プロショップ、ドライビングレンジ、パッティンググリーン、スパ、プール、ゴルフシミュレーターが揃い、プロキャディがサポートします。

5. 体験＆アドバイス  
– 湖上のボートトランスファーでスタートする特別体験。  
– 朝の霧と夕暮れのサンセットが美しいティータイム。

6. 予約方法  
電話 (+84) 0123456789 または TeetimeVn.com からオンライン予約を。
'
WHERE course_id = 1 AND lang = 'ja';

-- course_id = 1 (BRG Kings Island Golf Resort), lang = ko
UPDATE golf_course_i18n
SET overview = '
BRG Kings Island 골프 리조트는 하노이시 Sơn Tây구 Đồng Mô 호숫가에 위치하며, 도심에서 약36km, Nội Bài 공항에서45km 떨어져 있습니다. 350ha 부지에 18홀 파72 코스가 세 개 조성되어 있으며, Lakeside(1993년 개장) 14개 홀에는 워터 해저드가 배치되어 있습니다.

1. 개요 및 역사  
1993년 북부 베트남 최초의 54홀 시설로 오픈했으며, 이후 전국 아마추어 챔피언십 개최 및 프로 선수 훈련장으로 자리매김했습니다。

2. 코스 디자인 및 경관  
– Lakeside: 완만한 언덕과 14개 홀의 수역.  
– Mountainview: 자연 언덕 지형을 활용한 레이아웃.  
– Kings Course: 광활한 페어웨이와 정교한 벙커.

3. 잔디 품질 및 유지 관리  
Bentgrass 그린과 Paspalum–Zoysia 페어웨이는 USGA 기준에 맞춰 관리되며, 24시간 자동 관개 시스템을 가동합니다.

4. 시설 및 서비스  
프리미엄 라커룸, 프로샵, 드라이빙 레인지, 퍼팅 그린, 스파, 수영장, 골프 시뮬레이터 등 다양한 시설과 전문 캐디 서비스를 제공합니다。

5. 경험 및 팁  
– 호수를 건너는 보트 트랜스퍼로 시작하는 이색 경험。  
– 아침 안개와 황혼 노을이 어우러진 환상적인 라운드。

6. 예약 안내  
전화 (+84) 0123456789 또는 TeetimeVn.com 에서 온라인 예약하세요。
'
WHERE course_id = 1 AND lang = 'ko';

-- course_id = 2 (Chi Linh Star Golf & Country Club), lang = vi
UPDATE golf_course_i18n
SET overview = '
Chi Linh Star Golf & Country Club tọa lạc tại xã Núi Đối, thị xã Chí Linh, tỉnh Hải Dương, cách Hà Nội khoảng 60 km về phía đông. Khai trương năm 2010 và do IMG Links Associates thiết kế, sân sở hữu 27 hố gồm hai sân par-72 và par-71, với tổng chiều dài gần 8.500 yards. Địa hình đồi núi xen kẽ hồ nước tự nhiên và thảm cỏ Bentgrass tạo nên những fairway uốn lượn, thách thức kỹ năng đánh gậy và phân tích đường bóng của golfer.

1. Tổng quan & Lịch sử  
Ra đời từ dự án phát triển du lịch xanh miền Bắc, Chi Linh Star nhanh chóng thu hút cộng đồng golf thủ nhờ chất lượng sân đẳng cấp quốc tế và cảnh quan thơ mộng. Sân từng đăng cai nhiều giải nghiệp dư khu vực và là điểm tập luyện của các CLB golf Hà Nội.

2. Thiết kế & Cảnh quan  
Mỗi hố được bố trí để tận dụng độ dốc tự nhiên trên nền đồi, kết hợp bunker trắng và mặt hồ rộng tạo góc đánh đa dạng. Từ tee box 1, golfer có thể phóng tầm mắt đến rừng thông xanh mướt, trong khi fairway 18 men theo bờ hồ yên ả, mang trải nghiệm vừa thử thách vừa thư thái.

3. Chất lượng sân cỏ & Bảo dưỡng  
Sân sử dụng Bentgrass nhập khẩu, bảo dưỡng theo tiêu chuẩn USGA. Đội ngũ greenskeeper vận hành hệ thống tưới tự động và kiểm soát độ ẩm 24/7, giữ cho greens luôn phẳng mượt và fairway đạt độ bám bóng tối ưu.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại với locker cao cấp, pro-shop đa dạng, nhà hàng Á-Âu và khu lounge ngắm cảnh. Dịch vụ caddie chuyên nghiệp, huấn luyện viên PGA, phòng Golf Simulator và khu spa giúp golfer thư giãn sau vòng chơi.

5. Trải nghiệm & Gợi ý  
Thời điểm đẹp nhất là sáng sớm khi sương mù giăng lối trên fairway, hoặc buổi chiều khi ánh hoàng hôn nhuộm vàng mặt hồ. Đừng quên thử tee time kết hợp dùng buffet trong clubhouse để cảm nhận trọn vẹn không gian.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt trực tuyến qua TeetimeVn.com để nhận ưu đãi giá tốt và hỗ trợ 24/7.
'
WHERE course_id = 2 AND lang = 'vi';

-- course_id = 2 (Chi Linh Star Golf & Country Club), lang = en
UPDATE golf_course_i18n
SET overview = '
Chi Linh Star Golf & Country Club is located in Nui Doi Commune, Chi Linh Town, Hai Duong Province, approximately 60 km east of Hanoi. Opened in 2010 and designed by IMG Links Associates, the resort features 27 holes across two courses (par-72 and par-71), totaling nearly 8,500 yards. Rolling fairways weave through natural hills, lakes, and imported Bentgrass, challenging golfers’ shot selection and strategic play.

1. Overview & History  
Born from a green tourism initiative in northern Vietnam, Chi Linh Star quickly gained acclaim for its world-class course quality and serene landscape. The club has hosted numerous regional amateur tournaments and serves as a training ground for Hanoi golf clubs.

2. Course Design & Scenery  
Each hole capitalizes on natural hillside contours, integrating white-sand bunkers and expansive water hazards. From tee box 1, players overlook verdant pine forests; on the 18th fairway, a lakeside approach provides a tranquil yet testing finish.

3. Turf Quality & Maintenance  
The course uses imported Bentgrass maintained to USGA standards. A dedicated greenskeeping team operates automated irrigation and moisture-control systems around the clock, ensuring perfectly smooth greens and optimal fairway conditions.

4. Facilities & Services  
The modern clubhouse offers premium lockers, a well-stocked pro shop, an Asian-Western restaurant, and a scenic lounge. Professional caddies, PGA-certified coaches, a Golf Simulator room, and a spa round out the full-service experience.

5. Experience & Tips  
Ideal tee times are early morning when mist drifts across fairways or late afternoon as golden light kisses the lake. Don’t miss the post-round buffet in the clubhouse to fully savor the atmosphere.

6. Booking  
Call (+84) 0123456789 or book online at TeetimeVn.com for the best rates and 24/7 support.
'
WHERE course_id = 2 AND lang = 'en';

-- course_id = 2 (Chi Linh Star Golf & Country Club), lang = zh-CN
UPDATE golf_course_i18n
SET overview = '
Chi Linh Star 高尔夫乡村俱乐部位于海阳省Chí Linh市Núi Đối乡，距河内约60公里。俱乐部于2010年开业，由IMG Links Associates设计，拥有27洞（两个标准杆72杆和71杆球场），总长度近8500码。起伏的球道穿越丘陵、湖泊和进口Bentgrass草坪，为球手提供精准击球和战术考验。

1. 概览与历史  
源自越北绿色旅游项目，Chi Linh Star因其国际级球场品质和宁静景观而备受推崇。球场曾承办多项区域业余赛事，并是河内多家高尔夫俱乐部的训练基地。

2. 设计与景观  
每个球洞都巧妙利用天然山坡地形，结合白沙沙坑与宽阔水障碍。从1号发球台眺望可见一片松林，而18号球道紧贴湖畔，既平和又具挑战性。

3. 草坪品质与维护  
球场使用进口Bentgrass，按USGA标准进行维护。专业养护团队24/7运行自动灌溉和湿度控制系统，确保球道和果岭始终完美。

4. 设施与服务  
现代化会所配备高级储物柜、专业球具店、中西餐厅和观景休息区。专业球童、PGA教练、高尔夫模拟室和水疗中心为您提供全方位服务。

5. 体验与建议  
最佳发球时间为清晨薄雾弥漫之时或傍晚余晖映照湖面之际。赛后别忘在会所享用自助餐，尽享美好时光。

6. 预订方式  
致电 (+84) 0123456789 或访问 TeetimeVn.com 在线预订，享受优惠并获得全天候支持。
'
WHERE course_id = 2 AND lang = 'zh-CN';

-- course_id = 2 (Chi Linh Star Golf & Country Club), lang = zh-TW
UPDATE golf_course_i18n
SET overview = '
Chi Linh Star 高爾夫鄉村俱樂部位於海陽省Chí Linh市Núi Đối鄉，距河內約60公里。於2010年開業，由IMG Links Associates設計，擁有27洞（標準桿72洞與71洞），總長近8500碼。球道穿越丘陵與湖泊，並鋪設進口Bentgrass草坪，為球手帶來精準擊球與策略挑戰。

1. 總覽與歷史  
源自越北綠色旅遊項目，Chi Linh Star以國際級品質和寧靜景觀著稱。球場曾承辦多項區域業餘賽事，並是河內高爾夫俱樂部的主要訓練場地。

2. 設計與景觀  
每個球洞均充分利用天然山坡地形，融入白沙沙坑和廣闊水障礙。從1號發球台可俯瞰松林景色，18號球道緊貼湖畔，既寧靜又具挑戰。

3. 草坪品質與維護  
球場採用Bentgrass果嶺，Paspalum–Zoysia球道，並依照美國高協（USGA）標準進行日常養護，自動灌溉及濕度控制系統24/7運作。

4. 施設與服務  
現代化會所備有高級儲物櫃、專業球具店、中西餐廳及觀景休憩區。專業球童、PGA教練、模擬室與水療中心全面服務。

5. 體驗與建議  
最佳發球時段為清晨薄霧與傍晚餘暉交織之際。賽後可在會所享用自助餐，盡情放鬆。

6. 預訂方式  
請電洽 (+84) 0123456789 或造訪 TeetimeVn.com 線上預訂，享受優惠和全天候支持。
'
WHERE course_id = 2 AND lang = 'zh-TW';

-- course_id = 2 (Chi Linh Star Golf & Country Club), lang = ja
UPDATE golf_course_i18n
SET overview = '
Chi Linh Star Golf & Country Clubはベトナム・ハイズオン省Chí Linh市Núi Đối郡に位置し、ハノイ中心部から東へ約60kmです。2010年開業、IMG Links Associates設計の27ホール（パー72/パー71）コースは合計約8,500ヤード。丘陵、湖、輸入Bentgrassのフェアウェイが戦略的に配置されています。

1. 概要と歴史  
北部のグリーンツーリズム事業の一環として誕生し、国際基準のコース品質と美しい自然景観で評価を獲得。これまで複数の地域アマチュア大会を開催。

2. コースデザイン＆景観  
各ホールは自然の斜面を活かし、白砂バンカーと広大なウォーターハザードを配置。1番ティーからは松林、18番フェアウェイ沿いには湖畔の景色が広がります。

3. 芝の品質＆メンテナンス  
グリーンはBentgrass、フェアウェイはPaspalum–Zoysiaを使用し、USGA基準の自動灌漑・湿度管理システムで24時間体制メンテナンス。

4. 施設＆サービス  
モダンクラブハウスにはプレミアムロッカー、プロショップ、中西料理レストラン、ラウンジ、プロキャディ、PGAコーチ、ゴルフゼミュレーター、スパを完備。

5. 体験＆アドバイス  
朝の霧に包まれたフェアウェイや、夕方のサンセットラウンドが格別。クラブハウスでのビュッフェもお忘れなく。

6. 予約方法  
電話 (+84) 0123456789 へお問い合わせ、または TeetimeVn.com でオンライン予約を行ってください。
'
WHERE course_id = 2 AND lang = 'ja';

-- course_id = 2 (Chi Linh Star Golf & Country Club), lang = ko
UPDATE golf_course_i18n
SET overview = '
Chi Linh Star Golf & Country Club은 베트남 하이즈엉성 Chí Linh시 Núi Đối군에 위치하며, 하노이에서 동쪽으로 약 60km 거리에 있습니다. 2010년에 개장했으며 IMG Links Associates가 설계한 27홀(파72/파71) 코스는 총 약 8,500야드를 자랑합니다. 구릉과 호수, 수입 Bentgrass의 페어웨이가 조화를 이룹니다.

1. 개요 및 역사  
북부 녹색 관광 프로젝트의 일환으로 탄생하여, 국제 기준의 코스 품질과 아름다운 자연 경관으로 호평받았습니다. 여러 지역 아마추어 토너먼트를 개최했습니다.

2. 코스 디자인 및 경관  
각 홀은 자연 경사를 활용해 설계되었으며, 백사장 벙커와 광대한 워터 해저드가 배치되었습니다. 1번 티에서 소나무 숲을, 18번 페어웨이에서는 호숫가 전경을 감상할 수 있습니다.

3. 잔디 품질 및 유지관리  
그린은 Bentgrass, 페어웨이는 Paspalum–Zoysia를 사용하며, USGA 기준의 자동 관개 및 습도 제어 시스템으로 24시간 관리됩니다.

4. 시설 및 서비스  
모던 클럽하우스에는 프리미엄 라커, 프로샵, 아시안·웨스턴 레스토랑, 라운지, 프로 캐디, PGA 코치, 골프 시뮬레이터, 스파가 갖추어져 있습니다.

5. 경험 및 팁  
안개 낀 아침 라운드와 석양 라운드를 추천합니다. 클럽하우스 뷔페도 놓치지 마세요.

6. 예약 안내  
전화 (+84) 0123456789 또는 TeetimeVn.com 에서 온라인 예약하세요.
'
WHERE course_id = 2 AND lang = 'ko';

-- course_id = 3 (Heron Lake Golf Course), lang = vi
UPDATE golf_course_i18n
SET overview = '
Heron Lake Golf Course & Resort nằm tại Đường Dĩnh Ấm, Phường Khai Quang, thành phố Vĩnh Yên, tỉnh Vĩnh Phúc, cách Hà Nội khoảng 50 km về phía tây bắc. Khai trương năm 2010 và do Peter Rousseau (P+Z Designs) thiết kế, sân 18 hố par-72 dài 6.883 yards, đan xen giữa hồ nước tự nhiên và fairway uốn lượn trên nền đồi thấp.

1. Tổng quan & Lịch sử  
Heron Lake ra đời nhằm phát triển du lịch golf ven đô, nhanh chóng thu hút golfer trong và ngoài nước. Sân đã tổ chức nhiều giải nghiệp dư khu vực và là điểm luyện tập cho các CLB golf Hà Nội và Hải Phòng.

2. Thiết kế & Cảnh quan  
Mỗi hố tận dụng địa hình đồi mượt, các bunker trắng và chướng ngại nước bao quanh fairway. Tee box 1 cho tầm nhìn toàn cảnh hồ lớn, fairway 9 chạy dọc bờ hồ phẳng lặng.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens sử dụng Bentgrass nhập khẩu, fairway phối Paspalum–Zoysia, bảo dưỡng theo tiêu chuẩn USGA với hệ thống tưới tự động và đội ngũ greenskeeper 24/7.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse phong cách hiện đại bao gồm locker cao cấp, pro-shop, phòng Golf Simulator, driving range, putting green, nhà hàng Á-Âu và spa. Dịch vụ caddie và huấn luyện viên PGA luôn sẵn sàng hỗ trợ.

5. Trải nghiệm & Gợi ý  
– Sáng sớm sương mù nhẹ quấn quanh fairway, – Chiều hoàng hôn rực rỡ phản chiếu mặt hồ.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 3 AND lang = 'vi';

-- course_id = 3 (Heron Lake Golf Course), lang = en
UPDATE golf_course_i18n
SET overview = '
Heron Lake Golf Course & Resort is located on Dinh Am Street, Khai Quang Ward, Vinh Yen City, Vinh Phuc Province—about 50 km northwest of Hanoi. Opened in 2010 and designed by Peter Rousseau of P+Z Designs, this par-72, 18-hole layout measures 6,883 yards, weaving through gentle hills and natural lakes.

1. Overview & History  
Created to boost suburban golf tourism, Heron Lake quickly became a favorite for both domestic and international players. It has hosted numerous regional amateur tournaments and serves as a training ground for Hanoi and Hai Phong clubs.

2. Course Design & Scenery  
Each hole capitalizes on rolling terrain, with white-sand bunkers and water hazards framing the fairways. Tee box 1 offers panoramic lake views; fairway 9 runs alongside a tranquil reservoir.

3. Turf Quality & Maintenance  
Featuring imported Bentgrass greens and Paspalum–Zoysia fairways, the course is maintained to USGA standards with 24/7 automated irrigation and a dedicated greenskeeping team.

4. Facilities & Services  
The modern clubhouse includes premium lockers, a pro shop, a Golf Simulator room, driving range, putting green, an Asian-Western restaurant, and a spa. Professional caddies and PGA instructors are available.

5. Experience & Tips  
– Early-morning tee times reveal mist drifting over fairways.  
– Late-afternoon rounds showcase golden light on the lake.

6. Booking  
Call (+84) 0123456789 or book online at TeetimeVn.com for the best rates.
'
WHERE course_id = 3 AND lang = 'en';

-- course_id = 3 (Heron Lake Golf Course), lang = zh-CN
UPDATE golf_course_i18n
SET overview = '
Heron Lake 高尔夫球场及度假村位于 Vĩnh Phúc 省永安市 Khai Quang 区 Dinh Am 街，距河内西北约50公里。2010年开业，由 Peter Rousseau（P+Z Designs）设计，18洞标准杆72杆，全长6,883码，球道环绕自然湖泊与缓坡。

1. 概览与历史  
Heron Lake旨在促进郊区高尔夫旅游，很快成为国内外球手的热门选择。球场举办多项区域业余赛，也是河内和海防俱乐部的训练场地。

2. 设计与景观  
球道沿起伏地形蜿蜒，白沙沙坑与水障碍分布其间。1号发球台可俯瞰湖泊全景；9号球道沿宁静水库而行。

3. 草坪品质与维护  
果岭采用进口Bentgrass，球道铺设Paspalum–Zoysia，按USGA标准维护，拥有24/7自动灌溉和专业养护团队。

4. 设施与服务  
现代会所设有高级储物柜、专业球具店、高尔夫模拟室、练习场、推杆练习区、亚洲–西餐厅和水疗中心。提供专业球童和PGA教练服务。

5. 体验与建议  
– 清晨发球可见雾气在球道上飘荡。  
– 傍晚余晖映照湖面别具韵味。

6. 预订方式  
致电 (+84) 0123456789 或访问 TeetimeVn.com 在线预订，享受优惠。
'
WHERE course_id = 3 AND lang = 'zh-CN';

-- course_id = 3 (Heron Lake Golf Course), lang = zh-TW
UPDATE golf_course_i18n
SET overview = '
Heron Lake 高爾夫球場及度假村位於 Vĩnh Phúc 省永安市 Khai Quang 區 Dinh Am 街，距河內西北約50公里。2010年開業，由 Peter Rousseau（P+Z Designs）設計，18洞標準杆72杆，全長6,883碼，球道環繞自然湖泊與緩坡。

1. 總覽與歷史  
Heron Lake 旨在促進郊區高爾夫旅遊，很快成為國內外球手的熱門選擇。球場舉辦多項區域業餘賽，也是河內和海防俱樂部的訓練場地。

2. 設計與景觀  
球道沿起伏地形蜿蜒，白沙沙坑與水障礙分佈其間。1號發球台可俯瞰湖泊全景；9號球道沿寧靜水庫而行。

3. 草坪品質與維護  
果嶺採用進口Bentgrass，球道鋪設Paspalum–Zoysia，按USGA標準維護，配備24/7自動灌溉及專業養護團隊。

4. 施設與服務  
現代會所設有高級儲物櫃、專業球具店、高爾夫模擬室、練習場、果嶺練習區、亞洲–西餐廳及水療中心。提供專業球童和PGA教練服務。

5. 體驗與建議  
– 清晨發球可見霧氣在球道上飄蕩。  
– 傍晚餘暉映照湖面別具韻味。

6. 預訂方式  
請電洽 (+84) 0123456789 或造訪 TeetimeVn.com 線上預訂，享受優惠。
'
WHERE course_id = 3 AND lang = 'zh-TW';

-- course_id = 3 (Heron Lake Golf Course), lang = ja
UPDATE golf_course_i18n
SET overview = '
Heron Lake Golf Course & Resortは、Vĩnh Phúc省永安市Khai Quang区Dinh Am通りに位置し、ハノイ中心部から北西へ約50kmです。2010年開業、Peter Rousseau（P+Z Designs）設計のパー72・18ホール、全長6,883ヤードのコースで、自然湖と穏やかな丘陵地形が特徴です。

1. 概要と歴史  
郊外ゴルフ観光を促進するために設立され、国内外のプレーヤーに支持されました。地域アマチュアトーナメントの開催実績も豊富で、ハノイやハイフォンのクラブのトレーニング場として利用されています。

2. コースデザイン＆景観  
フェアウェイは起伏に富んだ地形に沿って配置され、ホワイトサンドバンカーとウォーターハザードが戦略的に設置されています。1番ティーからは湖の全景を望み、9番ホールは静かなリザーバー沿いに進みます。

3. 芝の品質＆メンテナンス  
ベントグラスグリーンとパスパルム–ゾイシアフェアウェイはUSGA基準で維持管理され、24時間稼働の自動灌漑システムと専門チームがコースをケアします。

4. 施設＆サービス  
モダンなクラブハウスにはプレミアムロッカー、プロショップ、ゴルフシミュレーター、ドライビングレンジ、パッティンググリーン、アジアン–ウェスタンレストラン、スパが揃い、プロキャディとPGAコーチがサポートします。

5. 体験＆アドバイス  
– 早朝の霧がフェアウェイを包む時間帯がおすすめ。  
– 夕方のサンセットは湖面を黄金色に染めます。

6. 予約方法  
電話 (+84) 0123456789 または TeetimeVn.com からオンライン予約を。
'
WHERE course_id = 3 AND lang = 'ja';

-- course_id = 3 (Heron Lake Golf Course), lang = ko
UPDATE golf_course_i18n
SET overview = '
Heron Lake Golf Course & Resort는 Vĩnh Phúc성 영안시 Khai Quang구 Dinh Am 거리 소재로, 하노이 중심부에서 북서쪽으로 약 50km 떨어져 있습니다. 2010년 개장, Peter Rousseau(P+Z Designs) 설계의 파72·18홀 코스로, 전장 6,883야드이며 자연 호수와 완만한 구릉이 특징입니다。

1. 개요 및 역사  
교외 골프 투어리즘을 촉진하기 위해 설립되어 국내외 골퍼들에게 인기입니다。지역 아마추어 대회도 다수 개최되었으며, 하노이와 하이퐁 클럽의 연습장으로도 활용됩니다。

2. 코스 디자인 및 경관  
페어웨이는 기복 있는 지형을 따라 배치되었으며, 화이트 샌드 벙커와 워터 해저드가 전략적으로 배치되어 있습니다。1번 티에서는 호수 전경을, 9번 홀에서는 고요한 저수지 풍경을 즐길 수 있습니다。

3. 잔디 품질 및 유지관리  
벤트그라스 그린과 파스팔럼–조이시아 페어웨이는 USGA 기준에 따라 관리되며, 24시간 자동 관개 시스템과 전문 팀이 코스를 유지합니다。

4. 시설 및 서비스  
모던 클럽하우스에는 프리미엄 라커룸、프로샵、골프 시뮬레이터、드라이빙 레인지、퍼팅 그린、아시안–웨스턴 레스토랑、스파가 구비돼 있으며、프로 캐디와 PGA 코치가 지원합니다。

5. 경험 및 팁  
– 이른 아침 안개 낀 티타임을 추천。  
– 석양 라운드는 호수를 황금빛으로 물들입니다。

6. 예약 안내  
전화 (+84) 0123456789 또는 TeetimeVn.com 에서 온라인 예약하세요。
'
WHERE course_id = 3 AND lang = 'ko';


-- course_id = 4 (Long Bien Golf Course), lang = vi
UPDATE golf_course_i18n
SET overview = '
Long Biên Golf Course tọa lạc tại Khu Trung Đoàn 918, phường Phúc Đồng, quận Long Biên, Hà Nội, cách trung tâm thành phố khoảng 15 phút lái xe. Thành lập năm 1997 và thiết kế bởi Nelson & Haworth, sân trải rộng trên 350 ha với 27 hố par-72, tổng chiều dài 7.201 yards, hài hòa giữa cảnh quan sông Hồng và mảng xanh rợp bóng.

1. Tổng quan & Lịch sử  
Ra đời nhằm thúc đẩy phong trào golf nội đô, Long Biên nhanh chóng trở thành điểm đến của golfer trong và ngoài nước, thường xuyên tổ chức các giải nghiệp dư và là nơi tập luyện của CLB Hà Nội.

2. Thiết kế & Cảnh quan  
Sân bao gồm ba sân 9 hố, uốn lượn qua đồi nhẹ và ven sông, với hàng dừa, bunker trắng và hồ nước rộng tạo điểm nhấn. Tee box 1 cho tầm nhìn toàn cảnh sông Hồng và cầu Long Biên.

3. Chất lượng sân cỏ & Bảo dưỡng  
Fairway lát Paspalum, greens sử dụng TifEagle Bermuda, được chăm sóc theo tiêu chuẩn USGA với hệ thống tưới tự động hoạt động 24/7:contentReference[oaicite:1]{index=1}.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại bao gồm locker cao cấp, pro-shop, driving range, putting green, nhà hàng Á-Âu và spa. Dịch vụ caddie chuyên nghiệp và PGA coach luôn sẵn sàng hỗ trợ.

5. Trải nghiệm & Gợi ý  
– Sáng sớm: sương mù bên sông tạo không gian thơ mộng.  
– Chiều muộn: hoàng hôn phản chiếu trên fairway.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi tốt nhất.
'
WHERE course_id = 4 AND lang = 'vi';

-- course_id = 4 (Long Bien Golf Course), lang = en
UPDATE golf_course_i18n
SET overview = '
Long Bien Golf Course is located at Khu Trung Doan 918, Phuc Dong Ward, Long Bien District, Hanoi—about a 15-minute drive from downtown:contentReference[oaicite:2]{index=2}. Established in 1997 and designed by Nelson & Haworth, this 350-ha facility features a 27-hole, par-72 layout stretching 7,201 yards, seamlessly blending Red River vistas with lush fairways.

1. Overview & History  
Created to foster urban golf, Long Bien quickly became a favorite for domestic and international players, hosting amateur championships and serving Hanoi clubs.

2. Course Design & Scenery  
Comprised of three 9-hole courses, holes meander through gentle hills and riverbanks, framed by palm rows, white-sand bunkers, and water hazards. Tee box 1 offers panoramic views of the Red River and Long Bien Bridge.

3. Turf Quality & Maintenance  
Paspalum fairways and TifEagle Bermuda greens are maintained to USGA standards with 24/7 automated irrigation:contentReference[oaicite:3]{index=3}.

4. Facilities & Services  
The modern clubhouse includes premium lockers, a pro shop, driving range, putting green, an Asian-Western restaurant, and a spa. Professional caddies and PGA coaches are on hand.

5. Experience & Tips  
– Early morning: mist over the river creates a serene ambiance.  
– Late afternoon: enjoy golden sunset hues across the fairways.

6. Booking  
Call (+84) 0123456789 or book online at TeetimeVn.com for the best rates.
'
WHERE course_id = 4 AND lang = 'en';

-- course_id = 4 (Long Bien Golf Course), lang = zh-CN
UPDATE golf_course_i18n
SET overview = '
龙边高尔夫球场位于河内市龙边区Phúc Đồng坊Khu Trung Đoàn 918，距市中心约15分钟车程:contentReference[oaicite:4]{index=4}。球场成立于1997年，由Nelson & Haworth设计，占地350公顷，拥有27洞标准杆72杆，总长7,201码，融红河景致与绿色球道于一体。

1. 概览与历史  
作为推动市内高尔夫的项目，龙边迅速成为国内外球手的热门场地，承办业余锦标赛并为河内俱乐部提供训练场地。

2. 设计与景观  
球道分为三组9洞，沿缓坡与河岸蜿蜒，棕榈林、白沙沙坑和水障碍错落其间。1号发球台可俯瞰红河及龙边桥风光。

3. 草坪品质与维护  
球道采用Paspalum，果岭使用TifEagle百慕大草，按USGA标准并配备24/7自动灌溉系统维护:contentReference[oaicite:5]{index=5}。

4. 设施与服务  
现代会所配有高级储物柜、专业球具店、练习场、推杆果岭、中西餐厅和SPA。专业球童与PGA教练全程支持。

5. 体验与建议  
– 清晨薄雾为球道增添诗意。  
– 傍晚落日染金球道，景色迷人。

6. 预订方式  
请致电 (+84) 0123456789 或访问 TeetimeVn.com 在线预订，享受最佳价格。
'
WHERE course_id = 4 AND lang = 'zh-CN';

-- course_id = 4 (Long Bien Golf Course), lang = zh-TW
UPDATE golf_course_i18n
SET overview = '
龍邊高爾夫球場位於河內市龍邊區Phúc Đồng坊Khu Trung Đoàn 918，距市中心約15分鐘車程:contentReference[oaicite:6]{index=6}。球場於1997年成立，由Nelson & Haworth設計，佔地350公頃，擁有27洞標準桿72桿，總長7,201碼，融合紅河美景與翠綠球道。

1. 總覽與歷史  
作為推動市內高爾夫的項目，龍邊迅速成為國內外球手的熱門之選，承辦業餘賽事並為河內球會提供訓練場地。

2. 設計與景觀  
球道分為三組9洞，沿緩坡與河岸蜿蜒，椰子樹、白沙沙坑和水障礙錯落其間。1號發球台可俯瞰紅河及龍邊橋風光。

3. 草坪品質與維護  
球道使用Paspalum，果嶺鋪設TifEagle百慕大草，按USGA標準並配備24/7自動灌溉系統維護:contentReference[oaicite:7]{index=7}。

4. 設施與服務  
現代化會所設有高級儲物櫃、專業球具店、練習場、推杆果嶺、中西餐廳和SPA。專業球童及PGA教練全程服務。

5. 體驗與建議  
– 清晨薄霧為球道增添詩意。  
– 傍晚落日映金球道，景色醉人。

6. 預訂方式  
請電洽 (+84) 0123456789 或造訪 TeetimeVn.com 線上預訂，享受最佳價格。
'
WHERE course_id = 4 AND lang = 'zh-TW';

-- course_id = 4 (Long Bien Golf Course), lang = ja
UPDATE golf_course_i18n
SET overview = '
ロンビエンゴルフコースはハノイ市ロンビエン区Phúc Đồng坊Khu Trung Đoàn 918に位置し、市中心部から車で約15分です:contentReference[oaicite:8]{index=8}。1997年に設立され、Nelson & Haworthが設計した350ヘクタールの敷地に27ホール・パー72、全長7,201ヤードのレイアウトを誇ります。

1. 概要と歴史  
市内ゴルフの普及を目的に開設され、国内外のプレーヤーに愛され、多くのアマチュア大会をホストし、ハノイのクラブ練習場としても利用されています。

2. コースデザイン＆景観  
3組9ホールのコースは緩やかな丘陵と河岸に沿って配置され、ヤシの並木、白砂バンカー、水辺が調和した美しい景観を提供。1番ティーからは紅河とロンビエン橋を一望。

3. 芝の品質＆メンテナンス  
フェアウェイはPaspalum、グリーンはTifEagleバミューダを使用。USGA基準の24/7自動灌漑システムと専門スタッフによる徹底管理で最高のコンディションを維持:contentReference[oaicite:9]{index=9}。

4. 施設＆サービス  
モダンクラブハウスにはプレミアムロッカー、プロショップ、ドライビングレンジ、パッティンググリーン、アジアン・ウェスタンレストラン、スパを完備。プロキャディとPGAコーチがサポート。

5. 体験＆アドバイス  
– 朝霧漂うティータイムは格別。  
– 夕暮れ時のサンセットラウンドでフェアウェイが金色に輝きます。

6. 予約方法  
電話 (+84) 0123456789 または TeetimeVn.com からオンライン予約をどうぞ。
'
WHERE course_id = 4 AND lang = 'ja';

-- course_id = 4 (Long Bien Golf Course), lang = ko
UPDATE golf_course_i18n
SET overview = '
롱비엔 골프 코스는 하노이 롱비엔구 Phúc Đồng坊 Khu Trung Đoàn 918에 위치하며, 시내 중심부에서 차로 약 15분 거리에 있습니다:contentReference[oaicite:10]{index=10}. 1997년에 개장하여 Nelson & Haworth가 설계한 350ha 부지에 27홀 파72, 전장 7,201야드 코스로 구성되어 있습니다。

1. 개요 및 역사  
도심 골프 활성화를 위해 설립되어 국내외 골퍼들에게 인기를 얻었으며, 다수의 아마추어 대회를 개최하고 하노이 골프 클럽들의 연습장으로 사용됩니다。

2. 코스 디자인 및 경관  
3개의 9홀 코스는 완만한 구릉과 강변을 따라 배치되어 있으며, 야자수, 흰 모래 벙커, 워터 해저드가 조화를 이룹니다。1번 티에서는 홍강과 롱비엔 다리를 조망할 수 있습니다。

3. 잔디 품질 및 유지관리  
페어웨이는 Paspalum, 그린은 TifEagle 버뮤다로 구성되며, USGA 기준의 24/7 자동 관개 시스템과 전문 그린키퍼 팀이 최상의 코스 상태를 유지합니다:contentReference[oaicite:11]{index=11}。

4. 시설 및 서비스  
모던 클럽하우스에는 프리미엄 라커룸、프로샵、드라이빙 레인지、퍼팅 그린、아시안-웨스턴 레스토랑、스파가 구비되어 있으며、프로 캐디 및 PGA 코치가 지원합니다。

5. 경험 및 팁  
– 이른 아침 안개 낀 라운드는 매우 낭만적입니다。  
– 해질녘 라운드는 황금빛 페어웨이가 환상적입니다。

6. 예약 안내  
전화 (+84) 0123456789 또는 TeetimeVn.com 에서 온라인 예약하세요。
'
WHERE course_id = 4 AND lang = 'ko';


-- course_id = 5 (Sky Lake Resort & Golf Club), lang = vi
UPDATE golf_course_i18n
SET overview = '
Sky Lake Resort & Golf Club nằm tại khu vực Hồ Văn Sơn, huyện Chương Mỹ, Hà Nội, cách trung tâm thành phố khoảng 45 phút lái xe:contentReference[oaicite:0]{index=0}. Khai trương năm 2012 và do Ahn Moon-Hwan (Bori Golf Design) thiết kế, sân bao gồm hai sân 18 hố chuẩn par-72, với tổng chiều dài lên tới 7.557 yards (Lake Course) và 7.311 yards (Sky Course):contentReference[oaicite:1]{index=1}.

1. Tổng quan & Lịch sử  
Thành lập nhằm phát triển du lịch gôn miền ven đô, Sky Lake nhanh chóng trở thành điểm đến ưa thích của golfer trong và ngoài nước, tổ chức nhiều giải nghiệp dư khu vực.

2. Thiết kế & Cảnh quan  
– Lake Course (7.557 yards): fairway uốn quanh hồ 50 ha, biến hóa độ cao và bunker trắng.  
– Sky Course (7.311 yards): chạy qua rừng tự nhiên, sử dụng địa hình đồi thấp, tạo thử thách cho mọi cấp độ.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens Bentgrass và fairway Paspalum–Zoysia được chăm sóc theo tiêu chuẩn USGA, với hệ thống tưới tự động và đội ngũ greenskeeper 24/7:contentReference[oaicite:2]{index=2}.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse sang trọng có locker cao cấp, pro-shop, driving range, putting green, nhà hàng Á-Âu và spa. Dịch vụ caddie, huấn luyện viên PGA và Golf Simulator luôn sẵn sàng.

5. Trải nghiệm & Gợi ý  
– Sáng sớm: sương mờ trên hồ Văn Sơn.  
– Chiều muộn: ánh hoàng hôn nhuộm vàng fairway.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi.
'
WHERE course_id = 5 AND lang = 'vi';

-- course_id = 5 (Sky Lake Resort & Golf Club), lang = en
UPDATE golf_course_i18n
SET overview = '
Sky Lake Resort & Golf Club is located in the Van Son Lake area, Chuong My District, Hanoi—about a 45-minute drive from downtown:contentReference[oaicite:3]{index=3}. Opened in 2012 and designed by Ahn Moon-Hwan of Bori Golf Design, the resort features two 18-hole par-72 courses: the Lake Course (7,557 yards) and the Sky Course (7,311 yards):contentReference[oaicite:4]{index=4}.

1. Overview & History  
Built to expand suburban golf tourism, Sky Lake quickly became a favorite for domestic and international players, hosting regional amateur events.

2. Course Design & Scenery  
– Lake Course: weaves around a 50-ha lake with elevation changes and white-sand bunkers.  
– Sky Course: meanders through natural woodlands and gentle hills, offering varied challenges.

3. Turf Quality & Maintenance  
Bentgrass greens and Paspalum–Zoysia fairways are maintained to USGA standards with automated irrigation and a 24/7 greenskeeping team:contentReference[oaicite:5]{index=5}.

4. Facilities & Services  
The upscale clubhouse includes premium lockers, a pro shop, a driving range, putting greens, an Asian-Western restaurant, and a spa. Professional caddies, PGA coaches, and a Golf Simulator are available.

5. Experience & Tips  
– Early mornings: mist rising over Van Son Lake.  
– Late afternoons: golden sunset light across fairways.

6. Booking  
Call (+84) 0123456789 or book online at TeetimeVn.com for the best rates.
'
WHERE course_id = 5 AND lang = 'en';

-- course_id = 5 (Sky Lake Resort & Golf Club), lang = zh-CN
UPDATE golf_course_i18n
SET overview = '
Sky Lake 度假及高尔夫俱乐部位于河内市Chuong My区Hồ Văn Sơn湖区，距市中心约45分钟车程:contentReference[oaicite:6]{index=6}。球场于2012年开业，由Ahn Moon-Hwan（Bori Golf Design）设计，包含两座18洞标准杆72杆球场：湖道（7,557码）和天空道（7,311码）:contentReference[oaicite:7]{index=7}。

1. 概览与历史  
旨在推动郊区高尔夫旅游，Sky Lake迅速成为国内外球手的热门目的地，并举办多场区域业余赛事。

2. 设计与景观  
– 湖道：环绕50公顷湖泊，地形起伏，白沙沙坑点缀。  
– 天空道：穿越原始林地与温和山丘，多样化挑战。

3. 草坪品质与维护  
果岭采用Bentgrass，球道为Paspalum–Zoysia，依照美国高协标准并配备自动灌溉和24/7养护团队:contentReference[oaicite:8]{index=8}。

4. 设施与服务  
高级会所设有储物柜、专业球具店、练习场、果岭练习区、中西餐厅和水疗中心。专业球童、PGA教练和高尔夫模拟器全天候服务。

5. 体验与建议  
– 清晨：湖面薄雾营造诗意。  
– 傍晚：夕阳金色洒满球道。

6. 预订方式  
致电 (+84) 0123456789 或访问 TeetimeVn.com 在线预订，享受优惠。
'
WHERE course_id = 5 AND lang = 'zh-CN';

-- course_id = 5 (Sky Lake Resort & Golf Club), lang = zh-TW
UPDATE golf_course_i18n
SET overview = '
Sky Lake 度假及高爾夫俱樂部位於河內市Chuong My區Hồ Văn Sơn湖區，距市中心約45分鐘車程:contentReference[oaicite:9]{index=9}。球場於2012年開業，由Ahn Moon-Hwan（Bori Golf Design）設計，擁有兩座18洞標準桿72桿球場：湖道（7,557碼）及天空道（7,311碼）:contentReference[oaicite:10]{index=10}。

1. 總覽與歷史  
旨在推動郊區高爾夫旅遊，Sky Lake迅速成為國內外球手的熱門之選，並承辦多場區域業餘比賽。

2. 設計與景觀  
– 湖道：環繞50公頃湖泊，起伏地形與白沙沙坑相映。  
– 天空道：穿越原始林地及緩坡山丘，挑戰多樣化擊球。

3. 草坪品質與維護  
果嶺採用Bentgrass，球道為Paspalum–Zoysia，依USGA標準並配備自動灌溉與24/7養護團隊:contentReference[oaicite:11]{index=11}。

4. 設施與服務  
高檔會所設有儲物櫃、專業球具店、練習場、果嶺練習區、中西餐廳和水療中心。專業球童、PGA教練及高爾夫模擬器全天候服務。

5. 體驗與建議  
– 清晨：湖畔薄霧增添詩意。  
– 傍晚：夕陽金色映照球道。

6. 預訂方式  
請電洽 (+84) 0123456789 或造訪 TeetimeVn.com 線上預訂，享受優惠。
'
WHERE course_id = 5 AND lang = 'zh-TW';

-- course_id = 5 (Sky Lake Resort & Golf Club), lang = ja
UPDATE golf_course_i18n
SET overview = '
Sky Lake Resort & Golf Clubはハノイ市Chuong My区のHồ Văn Sơn湖周辺に位置し、市中心部から車で約45分です:contentReference[oaicite:12]{index=12}。2012年開業、Ahn Moon-Hwan（Bori Golf Design）設計の18ホール×2コース、パー72、湖コース7,557ヤード、スカイコース7,311ヤードのレイアウトです:contentReference[oaicite:13]{index=13}。

1. 概要と歴史  
郊外ゴルフ観光を拡大する目的で設立され、国内外のプレーヤーに支持され、多数のアマチュア大会を開催。

2. コースデザイン＆景観  
– 湖コース：50ヘクタールの湖を巡る起伏あるフェアウェイとホワイトサンドバンカー。  
– スカイコース：自然林と穏やかな丘陵を活かしたレイアウトで多様な戦略を要求。

3. 芝の品質＆メンテナンス  
ベントグラスのグリーンとパスパルム–ゾイシアのフェアウェイはUSGA基準で管理され、自動灌漑と24/7メンテナンス体制で完璧に保たれます:contentReference[oaicite:14]{index=14}。

4. 施設＆サービス  
モダンクラブハウスにはプレミアムロッカー、プロショップ、ドライビングレンジ、パッティンググリーン、アジアン-ウェスタンレストラン、スパを完備。専属キャディとPGAコーチ、ゴルフシミュレーターがサポート。

5. 体験＆アドバイス  
– 早朝：湖上の霧が幻想的。  
– 夕方：夕陽がフェアウェイを黄金色に染める。

6. 予約方法  
電話 (+84) 0123456789 または TeetimeVn.com からオンライン予約をどうぞ。
'
WHERE course_id = 5 AND lang = 'ja';

-- course_id = 5 (Sky Lake Resort & Golf Club), lang = ko
UPDATE golf_course_i18n
SET overview = '
스카이 레이크 리조트 앤 골프 클럽은 하노이시 Chương Mỹ군 Hồ Văn Sơn 호숫가에 위치하며, 도심에서 차로 약 45분 거리입니다:contentReference[oaicite:15]{index=15}. 2012년 개장, Ahn Moon-Hwan(Bori Golf Design) 설계의 18홀 코스 두 개(파72)로, 레이크 코스 7,557야드·스카이 코스 7,311야드입니다:contentReference[oaicite:16]{index=16}.

1. 개요 및 역사  
교외 골프 관광 활성화를 위해 조성되어 국내외 골퍼에게 사랑받으며 다수의 아마추어 대회를 개최.

2. 코스 디자인 및 경관  
– 레이크 코스: 50헥타르 호수를 따라 펼쳐지는 기복 있는 페어웨이와 화이트 샌드 벙커.  
– 스카이 코스: 자연 숲과 완만한 언덕을 활용한 다채로운 레이아웃.

3. 잔디 품질 및 유지관리  
벤트그라스 그린과 파스팔럼–조이시아 페어웨이는 USGA 기준으로 관리되며, 자동 관개 및 24/7 유지 관리 체계가 가동:contentReference[oaicite:17]{index=17}.

4. 시설 및 서비스  
프리미엄 라커룸, 프로샵, 드라이빙 레인지, 퍼팅 그린, 아시안-웨스턴 레스토랑, 스파를 갖춘 모던 클럽하우스. 전담 캐디와 PGA 코치, 골프 시뮬레이터가 지원합니다.

5. 경험 및 팁  
– 이른 아침: 호수 위 안개가 환상적입니다.  
– 늦은 오후: 일몰이 페어웨이를 황금빛으로 물들입니다.

6. 예약 안내  
전화 (+84) 0123456789 또는 TeetimeVn.com 에서 온라인 예약하세요。
'
WHERE course_id = 5 AND lang = 'ko';

-- course_id = 6 (FLC Halong Bay Golf Club), lang = vi
UPDATE golf_course_i18n
SET overview = '
Sân golf FLC Hạ Long Bay Golf Club & Luxury Resort nằm trên đảo Rều, vịnh Hạ Long, trong quần thể FLC Luxury Resort, cách trung tâm thành phố Hạ Long khoảng 20 phút lái xe và 3 giờ từ Hà Nội:contentReference[oaicite:0]{index=0}. Khai trương tháng 8/2017 và do Schmidt-Curley thiết kế, sân 18 hố par-71 dài 6.092 yards, nổi bật với fairway uốn lượn qua các dãy đá vôi và mặt nước xanh biếc.

1. Tổng quan & Lịch sử  
Được hình thành để hoàn thiện tổ hợp du lịch – nghỉ dưỡng – giải trí FLC Hạ Long, sân nhanh chóng thu hút golfer trong và ngoài nước nhờ tầm nhìn tuyệt đẹp ra di sản thế giới Ha Long Bay:contentReference[oaicite:1]{index=1}.

2. Thiết kế & Cảnh quan  
Fairway khai thác địa hình đồi thấp và hồ nước tự nhiên, với bunker trắng chiến lược. Tee box 1 cho góc nhìn toàn cảnh biển, fairway 14 vòng quanh đảo nhỏ giữa hồ.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens sử dụng Bentgrass và fairway Paspalum, được chăm sóc theo tiêu chuẩn USGA với hệ thống tưới tự động và đội ngũ greenskeeper 24/7:contentReference[oaicite:2]{index=2}.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse sang trọng gồm locker cao cấp, pro-shop, nhà hàng Á-Âu, bay-view lounge, spa, driving range, putting green và phòng Golf Simulator. Dịch vụ caddie và huấn luyện viên PGA luôn sẵn sàng.

5. Trải nghiệm & Gợi ý  
– Sáng sớm: ngắm bình minh lên trên mặt nước.  
– Chiều muộn: tận hưởng hoàng hôn dát vàng vách đá vôi.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi.
'
WHERE course_id = 6 AND lang = 'vi';

-- course_id = 6 (FLC Halong Bay Golf Club), lang = en
UPDATE golf_course_i18n
SET overview = '
FLC Halong Bay Golf Club & Luxury Resort is located on Reu Island in Ha Long Bay, within the FLC Luxury Resort complex—about a 20-minute drive from Ha Long City and roughly 3 hours from Hanoi:contentReference[oaicite:3]{index=3}. Opened in August 2017 and designed by Schmidt-Curley, this 18-hole, par-71 course measures 6,092 yards and winds through dramatic limestone karsts and turquoise waters.

1. Overview & History  
Conceived as the centerpiece of FLC’s integrated resort, Halong Bay Golf Club quickly drew domestic and international golfers with its unrivaled bay views:contentReference[oaicite:4]{index=4}.

2. Course Design & Scenery  
Fairways follow rolling terrain and water features, punctuated by white-sand bunkers. Tee box 1 overlooks the bay; hole 14 loops around an island green amid the water.

3. Turf Quality & Maintenance  
Bentgrass greens and Paspalum fairways are maintained to USGA standards with automated irrigation and a 24/7 greenskeeping team:contentReference[oaicite:5]{index=5}.

4. Facilities & Services  
The upscale clubhouse offers premium lockers, a pro shop, an Asian-Western restaurant, bay-view lounge, spa, driving range, putting green, and Golf Simulator. Professional caddies and PGA coaches are available.

5. Experience & Tips  
– Early morning: sunrise over the misty bay.  
– Late afternoon: golden light on the limestone cliffs.

6. Booking  
Call (+84) 0123456789 or book online at TeetimeVn.com for the best rates.
'
WHERE course_id = 6 AND lang = 'en';

-- course_id = 6 (FLC Halong Bay Golf Club), lang = zh-CN
UPDATE golf_course_i18n
SET overview = '
FLC下龙湾高尔夫俱乐部及奢华度假区位于广宁省下龙湾Rều岛，距离下龙市中心约20分钟车程，距河内约3小时:contentReference[oaicite:6]{index=6}。球场于2017年8月开业，由Schmidt-Curley设计，18洞标准杆71杆，全长6,092码，球道穿梭于石灰岩峰林与碧绿海水之间。

1. 概览与历史  
作为FLC整合度假项目的核心，该球场凭借无与伦比的海湾景观迅速吸引国内外球手:contentReference[oaicite:7]{index=7}。

2. 设计与景观  
球道利用起伏地形和水障碍，配以白沙沙坑。1号发球台俯瞰下龙湾；14号球道环绕岛式果岭。

3. 草坪品质与维护  
果岭采用Bentgrass，球道使用Paspalum，按USGA标准并配备自动灌溉系统与全天候养护团队:contentReference[oaicite:8]{index=8}。

4. 设施与服务  
高端会所设有高级储物柜、专业球具店、中西餐厅、海湾景休息室、水疗中心、练习场、推杆区及高尔夫模拟室。专业球童与PGA教练全程服务。

5. 体验与建议  
– 清晨：雾气缭绕下的日出美景。  
– 傍晚：金色阳光映照石灰岩峭壁。

6. 预订方式  
请致电 (+84) 0123456789 或访问 TeetimeVn.com 在线预订，享受优惠。
'
WHERE course_id = 6 AND lang = 'zh-CN';

-- course_id = 6 (FLC Halong Bay Golf Club), lang = zh-TW
UPDATE golf_course_i18n
SET overview = '
FLC下龍灣高爾夫俱樂部及奢華度假區位於廣寧省下龍灣Rều島，距下龍市中心約20分鐘車程，距河內約3小時:contentReference[oaicite:9]{index=9}。球場於2017年8月開業，由Schmidt-Curley設計，18洞標準桿71桿，全長6,092碼，球道穿越石灰岩峰林與碧藍海水間。

1. 總覽與歷史  
作為FLC整合度假項目的核心，該球場憑藉絕佳海灣景觀迅速成為國內外球手首選:contentReference[oaicite:10]{index=10}。

2. 設計與景觀  
球道沿起伏地形與水障礙布局，搭配白沙沙坑。1號發球台俯瞰下龍灣；14號球道環繞島式果嶺。

3. 草坪品質與維護  
果嶺採用Bentgrass，球道鋪設Paspalum，按照USGA標準並配備自動灌溉系統與全天候養護團隊:contentReference[oaicite:11]{index=11}。

4. 施設與服務  
高端會所配備高級儲物櫃、專業球具店、中西餐廳、海灣景觀休息室、水療中心、練習場、推桿區及高爾夫模擬室。專業球童與PGA教練全程服務。

5. 體驗與建議  
– 清晨：霧氣中的日出美景。  
– 傍晚：夕陽染金石灰岩峭壁。

6. 預訂方式  
請電洽 (+84) 0123456789 或造訪 TeetimeVn.com 線上預訂，享受優惠。
'
WHERE course_id = 6 AND lang = 'zh-TW';

-- course_id = 6 (FLC Halong Bay Golf Club), lang = ja
UPDATE golf_course_i18n
SET overview = '
FLCハロンベイゴルフクラブ＆ラグジュアリーリゾートは、ベトナム広寧省ハロン湾のRều島に位置し、ハロン市中心部から車で約20分、ハノイから約3時間です:contentReference[oaicite:12]{index=12}。2017年8月オープン、Schmidt-Curley設計の18ホール・パー71、全長6,092ヤードのコースは、石灰岩カルストと紺碧の海に囲まれています。

1. 概要と歴史  
FLCの統合リゾート開発の中心として誕生し、世界遺産ハロン湾の絶景で国内外のゴルファーを魅了しました:contentReference[oaicite:13]{index=13}。

2. コースデザイン＆景観  
フェアウェイは起伏と水障害を組み合わせ、白砂バンカーがアクセント。1番ティー台からは湾を一望、14番ホールはアイランドグリーンを回り込みます。

3. 芝の品質＆メンテナンス  
ベントグラスグリーンとパスパルムフェアウェイはUSGA基準で管理され、自動灌漑システムと24時間体制のメンテナンスチームが完璧な状態を維持します:contentReference[oaicite:14]{index=14}。

4. 施設＆サービス  
プレミアムロッカー、プロショップ、アジアン-ウェスタンレストラン、ベイビューラウンジ、スパ、ドライビングレンジ、パッティンググリーン、ゴルフシミュレーターを備えたモダンクラブハウス。プロキャディとPGAコーチがサポート。

5. 体験＆アドバイス  
– 早朝：霧に包まれた湾の朝日を堪能。  
– 夕暮れ：黄金色に染まる崖の景観を楽しむ。

6. 予約方法  
電話 (+84) 0123456789 または TeetimeVn.com からオンライン予約をどうぞ。
'
WHERE course_id = 6 AND lang = 'ja';

-- course_id = 6 (FLC Halong Bay Golf Club), lang = ko
UPDATE golf_course_i18n
SET overview = '
FLC할롱베이 골프 클럽 & 럭셔리 리조트는 베트남 광닌성 할롱만 Rều섬에 위치하며, 할롱시 중심부에서 차로 약 20분, 하노이에서 약 3시간 거리입니다:contentReference[oaicite:15]{index=15}。2017년 8월 개장, Schmidt-Curley가 설계한 18홀 파71, 전장 6,092야드 코스는 석회암 절벽과 에메랄드빛 바다를 배경으로 펼쳐집니다。

1. 개요 및 역사  
FLC 종합 리조트 개발의 핵심으로 탄생하여, 세계유산 할롱만의 절경으로 국내외 골퍼를 매료했습니다:contentReference[oaicite:16]{index=16}。

2. 코스 디자인 및 경관  
페어웨이는 완만한 구릉과 워터 해저드가 조화롭게 배치되며, 화이트 샌드 벙커가 포인트. 1번 티에서는 만이 내려다보이고, 14번 홀은 섬 그린을 둘러싸고 있습니다。

3. 잔디 품질 및 유지관리  
벤트그라스 그린과 파스팔럼 페어웨이는 USGA 기준으로 관리되며, 자동 관개 시스템과 24/7 유지 관리 팀이 코스를 완벽하게 유지합니다:contentReference[oaicite:17]{index=17}。

4. 시설 및 서비스  
프리미엄 라커룸, 프로샵, 아시안-웨스턴 레스토랑, 만 전경 라운지, 스파, 드라이빙 레인지, 퍼팅 그린, 골프 시뮬레이터를 갖춘 모던 클럽하우스. 전담 캐디와 PGA 코치가 지원합니다。

5. 경험 및 팁  
– 이른 아침: 안개 낀 만의 일출 감상。  
– 늦은 오후: 석양이 절벽을 금빛으로 물들이는 장관。

6. 예약 안내  
전화 (+84) 0123456789 또는 TeetimeVn.com 에서 온라인 예약하세요。
'
WHERE course_id = 6 AND lang = 'ko';

-- course_id = 7 (Tuan Chau Resort Golf Course), lang = vi
UPDATE golf_course_i18n
SET overview = '
Sân golf Khu nghỉ dưỡng Tuần Châu nằm trên đảo Tuần Châu, phường Tuần Châu, thành phố Hạ Long, Quảng Ninh, cách trung tâm Hạ Long khoảng 5 km:contentReference[oaicite:0]{index=0}. Khai trương năm 2011 và do IMG London thiết kế, sân 18 hố par-72 trải dài 7.338 yards, tận dụng trọn vẹn cảnh quan kỳ vĩ của di sản thiên nhiên thế giới Ha Long Bay:contentReference[oaicite:1]{index=1}.

1. Tổng quan & Lịch sử  
Ra đời nhằm hoàn thiện quần thể du lịch – nghỉ dưỡng Tuần Châu, sân nhanh chóng thu hút golfer trong và ngoài nước nhờ tầm nhìn hướng vịnh và tiêu chuẩn quốc tế.

2. Thiết kế & Cảnh quan  
Hố golf uốn lượn qua địa hình đồi thấp, xen kẽ hồ nước ngọt và bunker trắng, với fairway hướng thẳng ra Vịnh Hạ Long. Hole 14 đặc biệt vòng quanh đảo nhỏ giữa hồ, đòi hỏi chiến lược chọn gậy chính xác.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens sử dụng Bentgrass và fairway trải Paspalum–Zoysia, được chăm sóc theo tiêu chuẩn USGA với hệ thống tưới tự động và đội ngũ greenskeeper chuyên nghiệp 24/7:contentReference[oaicite:2]{index=2}.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại với locker cao cấp, pro-shop, driving range, putting green, nhà hàng Á-Âu, lounge hướng vịnh, spa và phòng Golf Simulator. Dịch vụ caddie chuyên nghiệp và huấn luyện viên PGA hỗ trợ toàn diện.

5. Trải nghiệm & Gợi ý  
– Sáng sớm: ngắm bình minh trên biển mây.  
– Chiều muộn: hoàng hôn dát vàng kỳ vĩ trên vách đá vôi.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi.
'
WHERE course_id = 7 AND lang = 'vi';

-- course_id = 7 (Tuan Chau Resort Golf Course), lang = en
UPDATE golf_course_i18n
SET overview = '
Tuan Chau Resort Golf Course is located on Tuan Chau Island, Tuan Chau Ward, Ha Long City, Quang Ninh—about 5 km from downtown Ha Long:contentReference[oaicite:3]{index=3}. Opened in 2011 and designed by IMG London, this par-72, 18-hole course stretches 7,338 yards, making full use of the UNESCO World Heritage scenery of Ha Long Bay:contentReference[oaicite:4]{index=4}.

1. Overview & History  
Created to complement the Tuan Chau tourism and resort complex, the course quickly drew domestic and international golfers with its panoramic bay views and world-class standards.

2. Course Design & Scenery  
Fairways wind through gentle hills, freshwater lakes, and white-sand bunkers, with holes designed to maximize vistas of the bay. Hole 14 loops around a small island green, demanding precise strategy.

3. Turf Quality & Maintenance  
Bentgrass greens and Paspalum–Zoysia fairways are maintained to USGA standards with automated irrigation and a 24/7 greenskeeping team:contentReference[oaicite:5]{index=5}.

4. Facilities & Services  
The modern clubhouse offers premium lockers, a pro shop, a driving range, a putting green, an Asian-Western restaurant, a bay-view lounge, a spa, and a Golf Simulator room. Professional caddies and PGA coaches provide full support.

5. Experience & Tips  
– Early morning: enjoy sunrise over the misty bay.  
– Late afternoon: witness golden sunset light on limestone cliffs.

6. Booking  
Call (+84) 0123456789 or book online at TeetimeVn.com for the best rates.
'
WHERE course_id = 7 AND lang = 'en';

-- course_id = 7 (Tuan Chau Resort Golf Course), lang = zh-CN
UPDATE golf_course_i18n
SET overview = '
屯潮度假区高尔夫球场位于广宁省下龙市屯潮岛，距离市中心约5公里:contentReference[oaicite:6]{index=6}。球场于2011年开放，由IMG伦敦设计，18洞标准杆72杆，长度7,338码，充分利用下龙湾世界遗产的壮丽景观:contentReference[oaicite:7]{index=7}。

1. 概览与历史  
作为屯潮旅游度假区的核心项目，该球场凭借全景湾景和国际化标准迅速吸引了国内外球手。

2. 设计与景观  
球道蜿蜒于缓坡、淡水湖和白沙沙坑之间，每个球洞都强调海湾视野。14号洞环绕小岛果岭，挑战性十足。

3. 草坪品质与维护  
果岭使用Bentgrass，球道铺设Paspalum–Zoysia，按USGA标准由自动灌溉系统和24/7的养护团队维护:contentReference[oaicite:8]{index=8}。

4. 设施与服务  
现代会所配备高级储物柜、专业球具店、练习场、推杆场、中西餐厅、海湾休息区、水疗中心和高尔夫模拟室。专业球童及PGA教练提供全方位支持。

5. 体验与建议  
– 清晨：在薄雾中欣赏日出。  
– 傍晚：夕阳将石灰岩峭壁染成金色。

6. 预订方式  
请致电 (+84) 0123456789 或访问 TeetimeVn.com 在线预订，享受优惠。
'
WHERE course_id = 7 AND lang = 'zh-CN';

-- course_id = 7 (Tuan Chau Resort Golf Course), lang = zh-TW
UPDATE golf_course_i18n
SET overview = '
屯潮度假區高爾夫球場位於廣寧省下龍市屯潮島，距市中心約5公里:contentReference[oaicite:9]{index=9}。球場於2011年開幕，由IMG倫敦設計，18洞標準桿72桿，全長7,338碼，充分利用下龍灣世界遺產的壯麗景觀:contentReference[oaicite:10]{index=10}。

1. 總覽與歷史  
作為屯潮旅遊度假區的核心設施，該球場憑藉360°海灣全景與國際化標準迅速成為球手首選。

2. 設計與景觀  
球道沿緩坡、淡水湖及白沙沙坑蜿蜒，每一洞都最大化海灣視野。14號洞繞行島式果嶺，富有挑戰性。

3. 草坪品質與維護  
果嶺鋪設Bentgrass，球道為Paspalum–Zoysia，按USGA標準由自動灌溉系統和全天候養護團隊維護:contentReference[oaicite:11]{index=11}。

4. 施設與服務  
現代化會所設有高級儲物櫃、專業球具店、練習場、推桿場、中西餐廳、海灣休息室、水療中心及高爾夫模擬室。專業球童與PGA教練提供全方位支持。

5. 體驗與建議  
– 清晨：薄霧中的日出美景。  
– 傍晚：夕陽映照石灰岩峭壁，景色迷人。

6. 預訂方式  
請電洽 (+84) 0123456789 或前往 TeetimeVn.com 線上預訂，享受優惠。
'
WHERE course_id = 7 AND lang = 'zh-TW';

-- course_id = 7 (Tuan Chau Resort Golf Course), lang = ja
UPDATE golf_course_i18n
SET overview = '
トゥアンチャウリゾートゴルフコースは、ベトナム広寧省下龍市のトゥアンチャウ島に位置し、市中心部から約5kmです:contentReference[oaicite:12]{index=12}。2011年開業、IMG London設計の18ホール・パー72コースは7,338ヤードのレイアウトで、世界遺産ハロン湾の壮麗な景観を最大限に活かしています:contentReference[oaicite:13]{index=13}。

1. 概要と歴史  
トゥアンチャウ観光リゾートの中核として開発され、360度の湾ビューと国際基準の設備で国内外のゴルファーを魅了しました。

2. コースデザイン＆景観  
フェアウェイは緩やかな丘陵、淡水湖、白砂のバンカーを巡りながら湾を一望。14番ホールはアイランドグリーンを取り囲むデザインで挑戦的です。

3. 芝の品質＆メンテナンス  
ベントグラスグリーンとパスパルム–ゾイシアフェアウェイはUSGA基準で管理され、自動灌漑システムと24時間体制のメンテナンスチームが完璧な状態を維持します:contentReference[oaicite:14]{index=14}。

4. 施設＆サービス  
モダンクラブハウスにはプレミアムロッカー、プロショップ、ドライビングレンジ、パッティンググリーン、アジアン・ウェスタンレストラン、ベイビューラウンジ、スパ、高性能ゴルフシミュレーターを完備。プロキャディとPGAコーチがサポートします。

5. 体験＆アドバイス  
– 早朝：湾上に立ち込める霧の中で日の出を眺める贅沢。  
– 夕暮れ：石灰岩の断崖に染まるサンセットが幻想的。

6. 予約方法  
電話 (+84) 0123456789 または TeetimeVn.com からオンライン予約をどうぞ。
'
WHERE course_id = 7 AND lang = 'ja';

-- course_id = 7 (Tuan Chau Resort Golf Course), lang = ko
UPDATE golf_course_i18n
SET overview = '
투안차우 리조트 골프 코스는 베트남 광닌성 하롱시 투안차우섬에 위치하며, 시내 중심부에서 약 5km 거리입니다:contentReference[oaicite:15]{index=15}。2011년 개장, IMG London 설계의 18홀 파72 코스는 전장 7,338야드를 자랑하며, 유네스코 세계유산 하롱만의 절경을 최대한 활용합니다:contentReference[oaicite:16]{index=16}。

1. 개요 및 역사  
투안차우 관광 리조트의 핵심 시설로 개발되어, 360도 만 뷰와 국제 표준 시설로 국내외 골퍼를 사로잡았습니다。

2. 코스 디자인 및 경관  
페어웨이는 완만한 구릉, 담수 호수, 화이트 샌드 벙커를 지나며 만 전경을 조망합니다。14번 홀은 아일랜드 그린을 둘러싸는 레이아웃으로 도전적입니다。

3. 잔디 품질 및 유지관리  
그린은 벤트그라스, 페어웨이는 파스팔럼–조이시아로 구성되며, USGA 기준의 자동 관개 시스템과 24/7 유지 관리 팀이 코스를 최상으로 유지합니다:contentReference[oaicite:17]{index=17}。

4. 시설 및 서비스  
모던 클럽하우스에는 프리미엄 라커룸、프로샵、드라이빙 레인지、퍼팅 그린、아시안-웨스턴 레스토랑、베이뷰 라운지、스파、골프 시뮬레이터를 완비。전문 캐디와 PGA 코치가 지원합니다۔

5. 경험 및 팁  
– 이른 아침：만 위에 깔린 안개 속 일출을 감상。  
– 해질녘：석회암 절벽에 드리운 황금빛 석양을 즐기세요。

6. 예약 안내  
전화 (+84) 0123456789 또는 TeetimeVn.com 에서 온라인 예약하세요。
'
WHERE course_id = 7 AND lang = 'ko';

-- course_id = 8 (Van Tri Golf Club), lang = vi
UPDATE golf_course_i18n
SET overview = '
Sân golf Vân Trì Golf Club tọa lạc tại xã Kim Nỗ, huyện Đông Anh, Hà Nội, bên bờ sông Hồng, cách trung tâm thành phố khoảng 30 phút lái xe và sân bay Nội Bài 15 phút:contentReference[oaicite:0]{index=0}. Khai trương năm 2007 và do Peter Rousseau thiết kế, sân 18 hố par 72 trải dài 7.601 yards, kết hợp cồn cát ven sông, thảm lau sậy và hồ nước tự nhiên.

1. Tổng quan & Lịch sử  
Ra đời trong dự án phát triển du lịch golf ven đô Hà Nội, Vân Trì nhanh chóng ghi dấu nhờ thiết kế hiện đại và khung cảnh riverside:contentReference[oaicite:1]{index=1}.

2. Thiết kế & Cảnh quan  
Hố golf uốn lượn qua cồn cát, lau sậy và bunker trắng; tee box 1 có tầm nhìn thẳng ra sông, fairway 9 quanh co bên bờ cát, mang trải nghiệm vừa thử thách vừa phóng khoáng.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens Bentgrass và fairway Paspalum được chăm sóc theo tiêu chuẩn USGA với hệ thống tưới tự động và đội ngũ greenskeeper luân phiên 24/7:contentReference[oaicite:2]{index=2}.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse sang trọng với locker cao cấp, pro-shop, driving range, putting green, nhà hàng Á-Âu và lounge river-view; dịch vụ caddie, PGA coach và phòng Golf Simulator luôn sẵn sàng.

5. Trải nghiệm & Gợi ý  
– Sáng sớm: chạm sương mờ trên fairway.  
– Chiều muộn: hoàng hôn dát vàng cồn cát.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi.
'
WHERE course_id = 8 AND lang = 'vi';

-- course_id = 8 (Van Tri Golf Club), lang = en
UPDATE golf_course_i18n
SET overview = '
Van Tri Golf Club is located in Kim No Commune, Dong Anh District, Hanoi, on the banks of the Red River—about a 30-minute drive from downtown and 15 minutes from Noi Bai Airport:contentReference[oaicite:3]{index=3}. Opened in 2007 and designed by Peter Rousseau, the 18-hole, par 72 layout measures 7,601 yards and features riverside dunes, native grasses, and natural water hazards.

1. Overview & History  
Part of Hanoi’s suburban golf development, Van Tri quickly earned acclaim for its modern design and scenic riverside setting:contentReference[oaicite:4]{index=4}.

2. Course Design & Scenery  
Fairways weave through sandy dunes, native reeds, and white bunkers; tee box 1 offers panoramic river views, while hole 9 meanders along the dunes for a mix of challenge and freedom.

3. Turf Quality & Maintenance  
Bentgrass greens and Paspalum fairways are maintained to USGA standards with automated irrigation and a 24/7 greenskeeping team:contentReference[oaicite:5]{index=5}.

4. Facilities & Services  
The upscale clubhouse includes premium lockers, a pro shop, a driving range, a putting green, an Asian-Western restaurant, and a river-view lounge. Professional caddies, PGA coaches, and a Golf Simulator room are available.

5. Experience & Tips  
– Early morning: witness mist rising over the fairways.  
– Late afternoon: enjoy golden light cast across the dunes.

6. Booking  
Call (+84) 0123456789 or book online at TeetimeVn.com for the best rates.
'
WHERE course_id = 8 AND lang = 'en';

-- course_id = 8 (Van Tri Golf Club), lang = zh-CN
UPDATE golf_course_i18n
SET overview = '
Van Tri 高尔夫俱乐部位于河内市东英区 Kim No 社，毗邻红河，距市中心约30分钟车程，距内排机场15分钟:contentReference[oaicite:6]{index=6}。球场于2007年开业，由 Peter Rousseau 设计，18洞标准杆72杆，全长7,601码，融合河畔沙丘、原生芦苇与天然水障碍。

1. 概览与历史  
作为河内郊区高尔夫项目的一部分，Van Tri 凭借现代化设计和河畔景观迅速获得认可:contentReference[oaicite:7]{index=7}。

2. 设计与景观  
球道穿行于沙丘、芦苇和白沙沙坑；1号发球台可享河景全貌，9号球洞沿沙丘蜿蜒，兼具挑战与舒适。

3. 草坪品质与维护  
果岭采用 Bentgrass，球道为 Paspalum，按 USGA 标准并配备自动灌溉系统及全天候养护团队:contentReference[oaicite:8]{index=8}。

4. 设施与服务  
高端会所配备高级储物柜、专业球具店、练习场、推杆区、中西餐厅和河景休息区。专业球童、PGA 教练及高尔夫模拟室提供全方位支持。

5. 体验与建议  
– 清晨：观赏球道上升起的薄雾。  
– 傍晚：沙丘被金色夕阳染成诗意画面。

6. 预订方式  
请致电 (+84) 0123456789 或访问 TeetimeVn.com 在线预订，享受优惠。
'
WHERE course_id = 8 AND lang = 'zh-CN';

-- course_id = 8 (Van Tri Golf Club), lang = zh-TW
UPDATE golf_course_i18n
SET overview = '
Van Tri 高爾夫俱樂部位於河內市東英區 Kim No 社，臨近紅河，距市中心約30分鐘車程，距內排機場15分鐘:contentReference[oaicite:9]{index=9}。球場於2007年開幕，由 Peter Rousseau 設計，18洞標準桿72桿，全長7,601碼，融合河畔沙丘、原生蘆葦與天然水障礙。

1. 總覽與歷史  
作為河內郊區高爾夫項目的一環，Van Tri 以其現代設計和河畔美景迅速獲得肯定:contentReference[oaicite:10]{index=10}。

2. 設計與景觀  
球道交織於沙丘、蘆葦和白沙沙坑之間；1號發球台盡覽河景，9號球洞沿沙丘蜿蜒，兼具挑戰與舒適。

3. 草坪品質與維護  
果嶺使用 Bentgrass，球道鋪設 Paspalum，依 USGA 標準並配有自動灌溉系統及全天候養護團隊:contentReference[oaicite:11]{index=11}。

4. 施設與服務  
高級會所設有高級儲物櫃、專業球具店、練習場、推桿場、中西餐廳及河景休息室。專業球童、PGA 教練及高爾夫模擬室提供全方位支援。

5. 體驗與建議  
– 清晨：欣賞球道上的薄霧。  
– 傍晚：金色夕陽映照沙丘，景致如畫。

6. 預訂方式  
請電洽 (+84) 0123456789 或造訪 TeetimeVn.com 線上預訂，享受優惠。
'
WHERE course_id = 8 AND lang = 'zh-TW';

-- course_id = 8 (Van Tri Golf Club), lang = ja
UPDATE golf_course_i18n
SET overview = '
Van Tri ゴルフクラブはハノイ市東英区 Kim No 区域に位置し、紅河沿いで市中心部から車で約30分、ノイバイ空港から約15分です:contentReference[oaicite:12]{index=12}。2007年開場、Peter Rousseau 設計の18ホール・パー72コースは全長7,601ヤードで、川沿いの砂丘、原生アシ、天然ウォーターハザードを特徴とします。

1. 概要と歴史  
ハノイ郊外ゴルフ開発プロジェクトの一環として誕生し、モダンな設計とリバーサイドの眺望で高い評価を得ました:contentReference[oaicite:13]{index=13}。

2. コースデザイン＆景観  
フェアウェイは砂丘、葦原、白砂バンカーを縫うように配置。1番ティー台から川景を一望でき、9番ホールは砂丘に沿って挑戦と解放感を提供します。

3. 芝の品質＆メンテナンス  
ベントグラスのグリーンとパスパルムのフェアウェイはUSGA基準で管理され、自動灌漑システムと24時間体制のメンテナンスチームがコースを完璧に維持します:contentReference[oaicite:14]{index=14}。

4. 施設＆サービス  
プレミアムロッカールーム、プロショップ、ドライビングレンジ、パッティンググリーン、アジアン・ウェスタンレストラン、リバービューラウンジ、スパ、高性能ゴルフシミュレーターを備えたモダンクラブハウス。プロキャディとPGAコーチがサポートします。

5. 体験＆アドバイス  
– 早朝：リバーサイドに立ち込める霧と日の出の共演。  
– 夕暮れ：砂丘に映る黄金のサンセットが幻想的。

6. 予約方法  
電話 (+84) 0123456789 または TeetimeVn.com からオンライン予約をどうぞ。
'
WHERE course_id = 8 AND lang = 'ja';

-- course_id = 8 (Van Tri Golf Club), lang = ko
UPDATE golf_course_i18n
SET overview = '
반치 트리 골프 클럽(Van Tri Golf Club)은 하노이 동앙구 Kim No 지역, 홍강변에 위치하며, 시내 중심부에서 차로 약 30분, 노이바이 공항에서 약 15분 거리입니다:contentReference[oaicite:15]{index=15}。2007년 개장, Peter Rousseau 설계의 18홀 파72 코스는 전체 7,601야드를 자랑하며, 리버사이드 모래 언덕, 자생 갈대, 천연 워터 해저드를 특징으로 합니다。

1. 개요 및 역사  
하노이 교외 골프 개발 프로젝트의 일환으로 조성되어 모던한 디자인과 강변 뷰로 주목받았습니다:contentReference[oaicite:16]{index=16}。

2. 코스 디자인 및 경관  
페어웨이는 모래 언덕, 갈대, 화이트 샌드 벙커를 가로지르며 강가 전경을 선사합니다。1번 티에서는 리버뷰를, 9번 홀에서는 언덕을 따라 도전과 해방감을 동시에 경험할 수 있습니다。

3. 잔디 품질 및 유지관리  
Bentgrass 그린과 Paspalum 페어웨이는 USGA 기준에 따라 자동 관개 시스템과 24시간 유지 관리 팀이 완벽한 코스 컨디션을 유지합니다:contentReference[oaicite:17]{index=17}。

4. 시설 및 서비스  
프리미엄 라커룸、프로샵、드라이빙 레인지、퍼팅 그린、아시안-웨스턴 레스토랑、리버뷰 라운지、스파、골프 시뮬레이터를 갖춘 모던 클럽하우스。전문 캐디와 PGA 코치가 지원합니다。

5. 경험 및 팁  
– 이른 아침：안개 낀 리버사이드 일출 감상。  
– 늦은 오후：언덕에 드리운 황금빛 석양이 매력적입니다。

6. 예약 안내  
전화 (+84) 0123456789 또는 TeetimeVn.com 에서 온라인 예약하세요。
'
WHERE course_id = 8 AND lang = 'ko';

-- course_id = 9 (Tam Đảo Golf Course), lang = vi
UPDATE golf_course_i18n
SET overview = '
Sân golf Tam Đảo Golf Resort nằm trên cao nguyên Tam Đảo, huyện Tam Đảo, tỉnh Vĩnh Phúc, ở độ cao gần 900 m, cách Hà Nội khoảng 65 km về phía bắc:contentReference[oaicite:0]{index=0}. Được IMG thiết kế và khai trương năm 2007, sân 18 hố par 72 trải dài 7.169 yards, hài hòa giữa fairway uốn lượn qua rừng thông, hồ nước tự nhiên và bunker trắng.

1. Tổng quan & Lịch sử  
Khởi nguồn từ dự án du lịch sinh thái Tam Đảo, sân nhanh chóng thu hút golfer nhờ khí hậu mát mẻ quanh năm và khung cảnh núi non hùng vĩ:contentReference[oaicite:1]{index=1}.

2. Thiết kế & Cảnh quan  
Sân tận dụng độ dốc tự nhiên của vùng rừng thông để tạo đa dạng góc đánh; bunker trắng và hồ nước phản chiếu mây trời tạo điểm nhấn thị giác.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens sử dụng Bentgrass, fairway dùng Sea Isle Paspalum – cả hai nhập khẩu và bảo dưỡng theo tiêu chuẩn USGA với hệ thống tưới tự động và đội ngũ greenskeeper 24/7:contentReference[oaicite:2]{index=2}.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại với locker cao cấp, pro-shop, driving range, putting green, nhà hàng Á – Âu, lounge và spa. Dịch vụ caddie chuyên nghiệp, huấn luyện viên PGA và phòng Golf Simulator luôn sẵn sàng.

5. Trải nghiệm & Gợi ý  
– Sáng sớm: sương mù lảng bảng giữa rừng thông.  
– Chiều muộn: hoàng hôn trên đỉnh núi Tam Đảo.

6. Đặt chỗ  
Liên hệ (+84) 0123456789 hoặc đặt tee time online tại TeetimeVn.com để nhận ưu đãi.
'
WHERE course_id = 9 AND lang = 'vi';

-- course_id = 9 (Tam Đảo Golf Course), lang = en
UPDATE golf_course_i18n
SET overview = '
Tam Dao Golf Resort sits at about 900 m elevation in the Tam Dao highlands, Vinh Phuc province—approximately 65 km north of Hanoi:contentReference[oaicite:3]{index=3}. Designed by IMG and opened in 2007, the par-72, 18-hole championship course measures 7,169 yards and weaves through pine forests, natural lakes, and pristine white bunkers.

1. Overview & History  
Born from the Tam Dao eco-tourism project, the resort quickly became a favorite for its year-round cool climate and stunning mountain scenery:contentReference[oaicite:4]{index=4}.

2. Course Design & Scenery  
The layout leverages natural slopes for varied shot angles; white-sand bunkers and reflective water hazards provide dramatic vistas.

3. Turf Quality & Maintenance  
Bentgrass greens and Sea Isle Paspalum fairways are maintained to USGA standards with automated irrigation and a 24/7 greenskeeping team:contentReference[oaicite:5]{index=5}.

4. Facilities & Services  
The modern clubhouse features premium lockers, a pro shop, a driving range, a putting green, an Asian-Western restaurant, a lounge, and a spa. Professional caddies, PGA coaches, and a Golf Simulator room are available.

5. Experience & Tips  
– Early morning: mist drifting through the pines.  
– Late afternoon: sunset over the Tam Dao peaks.

6. Booking  
Call (+84) 0123456789 or reserve online at TeetimeVn.com for the best rates.
'
WHERE course_id = 9 AND lang = 'en';

-- course_id = 9 (Tam Đảo Golf Course), lang = zh-CN
UPDATE golf_course_i18n
SET overview = '
塔姆岛高尔夫度假村位于宁福省塔姆岛高原，海拔约900 米，距离河内市中心约65 公里:contentReference[oaicite:6]{index=6}。球场由IMG设计，2007年开幕，18洞标准杆72杆，全长7,169 码，球道穿行于松林、天然湖泊和洁白沙坑之间。

1. 概览与历史  
源自塔姆岛生态旅游项目，该度假村以四季凉爽气候和壮阔山景迅速走红:contentReference[oaicite:7]{index=7}。

2. 设计与景观  
球道利用天然坡度打造多样击球角度；白沙沙坑与水障碍交相辉映，增添视觉冲击。

3. 草坪品质与维护  
果岭采用Bentgrass，球道为Sea Isle Paspalum，按USGA标准维护，配备自动灌溉系统及全天候绿地团队:contentReference[oaicite:8]{index=8}。

4. 设施与服务  
现代化会所设有高级储物柜、专业球具店、练习场、推杆区、中西餐厅、休息室及SPA。提供专业球童、PGA教练和高尔夫模拟室。

5. 体验与建议  
– 清晨：松林薄雾。  
– 傍晚：山巅落日。

6. 预订方式  
请拨打 (+84) 0123456789 或访问 TeetimeVn.com 在线预订，享受优惠。
'
WHERE course_id = 9 AND lang = 'zh-CN';

-- course_id = 9 (Tam Đảo Golf Course), lang = zh-TW
UPDATE golf_course_i18n
SET overview = '
塔姆島高爾夫度假村位於寧福省塔姆島高原，海拔約900 米，距離河內市中心約65 公里:contentReference[oaicite:9]{index=9}。球場由IMG設計，2007年開幕，18洞標準桿72桿，全長7,169 碼，球道穿越松林、天然湖泊及潔白沙坑之中。

1. 總覽與歷史  
源自塔姆島生態旅遊項目，該度假村以全年涼爽氣候與壯觀山景迅速走紅:contentReference[oaicite:10]{index=10}。

2. 設計與景觀  
球道利用天然斜坡創造多樣擊球角度；白沙沙坑與水障礙相映成趣，增添視覺震撼。

3. 草坪品質與維護  
果嶺採用Bentgrass，球道鋪設Sea Isle Paspalum，依USGA標準維護，配備自動灌溉系統及全天候綠地團隊:contentReference[oaicite:11]{index=11}。

4. 施設與服務  
現代化會所配有高級儲物櫃、專業球具店、練習場、果嶺區、中西餐廳、休息室及SPA，並提供專業球童、PGA教練和高爾夫模擬室。

5. 體驗與建議  
– 清晨：松林薄霧。  
– 傍晚：山巔落日。

6. 預訂方式  
請致電 (+84) 0123456789 或造訪 TeetimeVn.com 線上預訂，享受優惠。
'
WHERE course_id = 9 AND lang = 'zh-TW';

-- course_id = 9 (Tam Đảo Golf Course), lang = ja
UPDATE golf_course_i18n
SET overview = '
タムダオゴルフリゾートはビンフック省タムダオ高原に位置し、標高約900 mでハノイ中心部から北へ約65 kmです:contentReference[oaicite:12]{index=12}。IMG設計による本格的な18ホール・パー72コースは、2007年にオープンし、全長7,169 ヤードに及びます。

1. 概要と歴史  
タムダオのエコツーリズム構想から誕生し、年間を通じて涼しい気候と雄大な山岳風景で人気を博しています:contentReference[oaicite:13]{index=13}。

2. コースデザイン＆景観  
ホールは松林の自然な斜面を生かし、多彩な角度からのショットを提供。白砂のバンカーとウォーターハザードが美しいコントラストを描きます。

3. 芝の品質＆メンテナンス  
グリーンはベントグラス、フェアウェイはSea Isle Paspalumを使用し、USGA基準の自動灌漑システムと24時間メンテナンスチームで完璧な状態を維持します:contentReference[oaicite:14]{index=14}。

4. 施設＆サービス  
モダンクラブハウスにはプレミアムロッカー、プロショップ、ドライビングレンジ、パッティンググリーン、アジアン・ウェスタンレストラン、ラウンジ、スパを完備。プロキャディとPGAコーチ、ゴルフシミュレーターがサポートします。

5. 体験＆アドバイス  
– 早朝：松林に立ち込める霧に包まれるひととき。  
– 夕暮れ：山頂に沈む夕陽を堪能。

6. 予約方法  
(+84) 0123456789 までお電話いただくか、TeetimeVn.com からオンライン予約をどうぞ。
'
WHERE course_id = 9 AND lang = 'ja';

-- course_id = 9 (Tam Đảo Golf Course), lang = ko
UPDATE golf_course_i18n
SET overview = '
탐다오 골프 리조트(Tam Dao Golf Resort)는 빈푹성 타마다오 고원에 위치하며, 해발 약 900 m, 하노이 중심부에서 북쪽으로 약 65 km 떨어져 있습니다:contentReference[oaicite:15]{index=15}. IMG가 설계하여 2007년에 개장한 이 파72, 18홀 코스는 전장이 7,169 야드에 이릅니다.

1. 개요 및 역사  
타마다오 생태관광 프로젝트의 일환으로 조성되어 연중 시원한 기후와 우뚝 솟은 산악 풍경으로 인기를 끌고 있습니다:contentReference[oaicite:16]{index=16}.

2. 코스 디자인 & 경관  
홀은 소나무 숲의 자연 경사를 활용해 다양한 각도의 샷을 제공하며, 흰색 벙커와 워터 해저드가 대비를 이룹니다.

3. 잔디 품질 및 유지관리  
그린은 벤트그라스, 페어웨이는 Sea Isle Paspalum을 사용하며, USGA 기준의 자동 관개 시스템과 24시간 그린키퍼 팀이 코스 상태를 완벽히 유지합니다:contentReference[oaicite:17]{index=17}.

4. 시설 및 서비스  
현대적인 클럽하우스에는 프리미엄 라커룸, 프로샵, 드라이빙 레인지, 퍼팅 그린, 아시안·웨스턴 레스토랑, 라운지, 스파가 구비되어 있습니다. 전문 캐디와 PGA 코치, 골프 시뮬레이터가 지원합니다.

5. 경험 및 팁  
– 이른 아침: 소나무 숲 사이로 피어오르는 안개.  
– 늦은 오후: 산등성이에 지는 황금빛 석양.

6. 예약 안내  
(+84) 0123456789로 전화하거나 TeetimeVn.com에서 온라인 예약하세요.
'
WHERE course_id = 9 AND lang = 'ko';

-- course_id = 10 (Montgomerie Links Vietnam)
-- 1. Địa chỉ và vùng: Thôn 1, Điện Dương, Điện Bàn, Quảng Nam (:contentReference[oaicite:0]{index=0})
-- 2. Thiết kế: Colin Montgomerie & IMG London (:contentReference[oaicite:1]{index=1})
-- 3. Chiều dài: 7.090 yards (:contentReference[oaicite:2]{index=2})

UPDATE golf_course_i18n
SET overview = 'Montgomerie Links Việt Nam tọa lạc tại Thôn 1, xã Điện Dương, thị xã Điện Bàn, tỉnh Quảng Nam, cách Đà Nẵng khoảng 15 phút lái xe. Được thiết kế bởi Colin Montgomerie phối hợp cùng IMG London và chính thức mở cửa năm 2010, sân 18 hố par 72 dài 7.090 yards, kết hợp đồi cát ven biển, hồ nước tự nhiên và fairway uốn lượn theo phong cách links truyền thống hiện đại.

**1. Tổng quan & Lịch sử**  
Ra đời nhằm hoàn thiện hệ sinh thái golf miền Trung, Montgomerie Links nhanh chóng trở thành điểm đến yêu thích của golfer trong và ngoài nước. Sân đã đăng cai vòng loại Asian Tour và nhiều giải nghiệp dư quốc tế.

**2. Thiết kế & Cảnh quan**  
Các hố tận dụng địa hình cồn cát ven biển, xen kẽ bunker chiến lược và water hazard. Tee box 1 hướng thẳng ra Biển Đông; fairway 9 ôm quanh hồ cảnh quan rộng lớn.

**3. Chất lượng sân cỏ & Bảo dưỡng**  
Greens Bentgrass và fairway Paspalum đảm bảo độ mượt và tốc độ nhất quán. Đội ngũ greenskeeper vận hành hệ thống tưới tự động, cắt cỏ và bón phân theo tiêu chuẩn USGA 24/7.

**4. Cơ sở vật chất & Dịch vụ**  
Clubhouse hiện đại với locker cao cấp, pro-shop đa dạng, nhà hàng Á–Âu và lounge hướng biển. Dịch vụ caddie chuyên nghiệp, huấn luyện viên PGA, phòng Golf Simulator và spa hoàn thiện trải nghiệm.

**5. Trải nghiệm & Gợi ý**  
Nên đặt tee time buổi sớm để ngắm bình minh trên Biển Đông hoặc buổi chiều để thưởng thức hoàng hôn. Sau vòng golf, bạn có thể thư giãn tại spa hoặc thưởng thức ẩm thực Đà Nẵng tại clubhouse.

**6. Hướng dẫn đặt chỗ**  
Truy cập TeetimeVn.com hoặc gọi 0123456789 để đặt tee time và nhận hỗ trợ 24/7.'
WHERE course_id = 10 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = 'Montgomerie Links Vietnam is located at Thon 1, Dien Duong Commune, Dien Ban Town, Quang Nam Province—just a 15-minute drive from Da Nang. Designed by Colin Montgomerie in collaboration with IMG London and opened in 2010, this par-72, 18-hole course stretches 7,090 yards across coastal dunes, natural lakes, and traditional links-style fairways with a modern twist.

**1. Overview & History**  
Conceived to complete the golf ecosystem of Central Vietnam, Montgomerie Links quickly became a favorite for domestic and international golfers. It has hosted Asian Tour qualifying rounds and numerous amateur championships.

**2. Course Design & Scenery**  
Holes leverage seaside dunes, strategic bunkers, and water hazards. Tee box 1 offers panoramic East Sea views; fairway 9 winds around a large scenic lake.

**3. Turf Quality & Maintenance**  
Bentgrass greens and Paspalum fairways deliver consistent speed and smooth roll. A dedicated greenskeeping team operates automated irrigation, precise mowing, and USGA-standard fertilization 24/7.

**4. Facilities & Services**  
The modern clubhouse features premium lockers, a well-stocked pro shop, an Asian-Western restaurant, and a sea-view lounge. Professional caddies, PGA coaches, a Golf Simulator room, and a spa complete the experience.

**5. Experience & Tips**  
Book early-morning tee times for sunrise over the East Sea or afternoon slots for coastal sunsets. After your round, unwind at the spa or sample local cuisine in the clubhouse.

**6. Booking**  
Visit TeetimeVn.com or call 0123456789 for tee time reservations and 24/7 assistance.'
WHERE course_id = 10 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = 'Montgomerie Links Vietnam 高爾夫俱樂部位於越南廣寧省電白鎮電陽社Thôn 1，距離峴港市中心僅15分鐘車程。球場於2010年由科林·蒙哥馬利（Colin Montgomerie）與IMG London聯手設計並開放，18洞標準桿72桿，全長7,090碼，融合海濱沙丘、天然湖泊與現代鏈式球道。

**1. 概覽與歷史**  
致力於完善中部高爾夫生態，Montgomerie Links迅速成為國內外球手的最愛，曾承辦亚洲巡回赛资格赛及多项业余赛事。

**2. 设计与景观**  
球洞依托滨海沙丘，结合策略性沙坑与水障碍。1号发球台可远眺东海；9号球道环绕大型景观湖。

**3. 草坪品质与维护**  
Bentgrass果岭与Paspalum球道确保速度与滚动一致。专业养护团队24/7自动灌溉、精准修剪并按USGA标准施肥。

**4. 设施与服务**  
现代会所配备高级储物柜、专业球具店、中西餐厅及海景休息室。专业球童、PGA教练、高尔夫模拟室及水疗中心一应俱全。

**5. 体验与建议**  
推荐清晨发球欣赏东海日出，或下午时段观赏海岸落日。赛后可在水疗中心放松或在会所品尝当地美食。

**6. 预订方式**  
请访问 TeetimeVn.com 或拨打 0123456789 进行预订并享受全天候支持。'
WHERE course_id = 10 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = 'Montgomerie Links Vietnam 골프 클럽은 베트남 꽝남성 디엔반군 디엔즈엉사 읍 Thon 1에 위치하며, 다낭공항에서 차로 15분 거리입니다. 2010년에 콜린 몽고메리(Colin Montgomerie)와 IMG London이 공동 설계하여 오픈했으며, 18홀 파72 코스로 총 길이 7,090야드를 자랑합니다. 코스는 해안 모래언덕, 자연 호수 및 전통 링크스 스타일 페어웨이를 현대적으로 재해석했습니다.

**1. 개요 및 역사**  
중부 지역의 골프 생태계를 완성하기 위해 만들어진 이 코스는 국내외 골퍼들에게 사랑받고 있으며, 아시안 투어 예선전 및 다수의 아마추어 대회를 개최했습니다.

**2. 코스 디자인 & 경관**  
홀은 해안 모래언덕과 전략적 벙커, 워터 해저드를 활용해 설계되었습니다. 1번 티에서는 동해를, 9번 페어웨이에서는 광활한 호수 경관을 감상할 수 있습니다.

**3. 잔디 품질 및 유지관리**  
Bentgrass 그린과 Paspalum 페어웨이는 USGA 기준에 따라 자동 관개와 24시간 유지 관리로 최상의 상태를 유지합니다.

**4. 시설 및 서비스**  
프리미엄 라커룸, 프로샵, 아시안·웨스턴 레스토랑, 씨뷰 라운지를 갖춘 모던 클럽하우스. 전문 캐디, PGA 코치, 골프 시뮬레이터 룸, 스파 시설이 완비되어 있습니다.

**5. 경험 및 팁**  
이른 아침 티타임에는 일출을, 오후 라운드에는 해안 일몰을 추천합니다. 라운드 후 스파나 클럽하우스에서 휴식을 즐기세요.

**6. 예약 안내**  
TeetimeVn.com 또는 0123456789로 예약하시면 24/7 지원을 받으실 수 있습니다.'
WHERE course_id = 10 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = 'Montgomerie Links Vietnam ゴルフクラブはベトナム・クアンナム省ディエンバン町ディエンズオン社Thon 1に位置し、ダナン空港から車で約15分です。2010年にコリン・モンゴメリーと IMG London によって設計・開場された18ホール・パー72コースで、全長7,090ヤードのリンクススタイルを現代的に再構築しています。

**1. 概要と歴史**  
中部のゴルフエコシステムを完成させるために誕生し、アジアンツアー予選会や多くのアマチュア大会を開催してきた実績があります。

**2. コースデザイン＆景観**  
シーサイドの砂丘と戦略的なバンカー、水のハザードを巧みに配置。1番ティーからは東シナ海、9番フェアウェイからは広大な湖が望めます。

**3. 芝の品質＆メンテナンス**  
ベントグラスのグリーンとパスパルムのフェアウェイは、USGA基準に基づく自動灌漑システムと24時間体制のメンテナンスで常に最高の状態を保っています。

**4. 施設＆サービス**  
プレミアムロッカー、プロショップ、アジアン・ウェスタンレストラン、シービューラウンジを備えたモダンクラブハウス。プロキャディ、PGAコーチ、ゴルフシミュレーター、スパも完備。

**5. 体験＆アドバイス**  
早朝ティータイムは日の出、午後のラウンドは海岸沿いのサンセットがおすすめです。ラウンド後はスパトリートメントやクラブハウスでのリラックスをお楽しみください。

**6. 予約方法**  
TeetimeVn.com または 0123456789 で予約すれば、24時間対応のサポートを受けられます。'
WHERE course_id = 10 AND lang = 'ja';


-- course_id = 11 (Laguna Lăng Cô Golf Club)
UPDATE golf_course_i18n
SET overview = 'Sân golf Laguna Lăng Cô nằm trong quần thể nghỉ dưỡng Laguna Lăng Cô, xã Lộc Vĩnh, huyện Phú Lộc, tỉnh Thừa Thiên Huế, bên bờ đầm phá Lăng Cô, cách sân bay Phú Bài khoảng 30 phút lái xe. Được thiết kế bởi Sir Nick Faldo và IMG London, chính thức khai trương vào tháng 3 năm 2013, sân 18 hố par 71 trải dài 7.033 yards, hài hòa giữa fairway uốn lượn, hồ nước ngọt và đồi cát ven biển. :contentReference[oaicite:0]{index=0}

1. **Tổng quan & Lịch sử**  
   Khởi nguồn từ dự án nghỉ dưỡng cao cấp của Banyan Tree, Laguna Lăng Cô nhanh chóng trở thành điểm đến yêu thích của golf thủ trong và ngoài nước, đăng cai nhiều giải nghiệp dư quốc gia và sự kiện VIP. :contentReference[oaicite:1]{index=1}

2. **Thiết kế & Cảnh quan**  
   Các hố golf tận dụng địa hình đồi cát và đầm phá: tee box 1 nhìn thẳng ra vịnh, fairway 6 băng qua hồ nước, bunker trắng bố trí chiến lược, mở ra tầm nhìn giữa nước, núi và rừng dừa. :contentReference[oaicite:2]{index=2}

3. **Chất lượng sân cỏ & Bảo dưỡng**  
   Greens sử dụng Bentgrass, fairway phối hợp Zoysia và Paspalum, bảo dưỡng theo tiêu chuẩn USGA. Hệ thống tưới tự động và đội ngũ greenskeeper vận hành 24/7 để đảm bảo mặt sân mượt mà và đồng đều. :contentReference[oaicite:3]{index=3}

4. **Cơ sở vật chất & Dịch vụ**  
   Clubhouse hiện đại với locker cao cấp, pro-shop, nhà hàng Á-Âu và lounge hướng đầm phá. Dịch vụ caddie chuyên nghiệp, huấn luyện viên PGA và phòng Golf Simulator sẵn sàng phục vụ luyện tập và giải trí. :contentReference[oaicite:4]{index=4}

5. **Trải nghiệm & Gợi ý**  
   Thời điểm lý tưởng là buổi sáng sớm khi đầm phá lấp lánh ánh nắng, hoặc chiều muộn khi hoàng hôn dát vàng fairway. Sau vòng golf, bạn có thể thư giãn tại spa hoặc thưởng thức ẩm thực địa phương tại clubhouse. :contentReference[oaicite:5]{index=5}

6. **Hướng dẫn đặt chỗ**  
   Truy cập TeetimeVn.com hoặc gọi 0123456789 để đặt tee time, nhận ưu đãi tốt nhất và hỗ trợ 24/7.'
WHERE course_id = 11 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = 'Laguna Lang Co Golf Club is situated within the Laguna Lang Co resort complex in Phu Loc district, Thua Thien Hue province, on the shores of Lang Co Lagoon, just a 30-minute drive from Phu Bai Airport. Designed by Sir Nick Faldo and IMG London, it officially opened in March 2013; the par-71, 18-hole layout measures 7,033 yards and blends rolling fairways, freshwater lakes, and coastal dunes. :contentReference[oaicite:6]{index=6}

1. **Overview & History**  
   Conceived as part of Banyan Tree’s luxury resort development, Laguna Lang Co quickly became a premier destination, hosting national amateur tournaments and VIP invitational events. :contentReference[oaicite:7]{index=7}

2. **Course Design & Scenery**  
   Holes leverage dune and lagoon landscapes: tee box 1 overlooks the bay; fairway 6 winds along the water’s edge; white-sand bunkers test precision against panoramic mountain and sea backdrops. :contentReference[oaicite:8]{index=8}

3. **Turf Quality & Maintenance**  
   Bentgrass greens and a mix of Zoysia and Paspalum fairways are maintained to USGA standards. Automated irrigation and a 24/7 greenskeeping team ensure consistently smooth surfaces. :contentReference[oaicite:9]{index=9}

4. **Facilities & Services**  
   The modern clubhouse offers premium lockers, a pro shop, an Asian-Western restaurant, and a lagoon-view lounge. Trained caddies, PGA-certified coaches, and a Golf Simulator room cater to practice and leisure. :contentReference[oaicite:10]{index=10}

5. **Experience & Tips**  
   Ideal tee times are early mornings when the lagoon sparkles at sunrise or late afternoons for golden-light fairways. Afterwards, relax at the spa or savor local specialties at the clubhouse restaurant. :contentReference[oaicite:11]{index=11}

6. **Booking**  
   Visit TeetimeVn.com or call 0123456789 to reserve tee times, secure the best rates, and receive 24/7 assistance.'
WHERE course_id = 11 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '拉古娜楞阔高尔夫俱乐部位于越南顺化省富禄县楞阔度假区内，毗邻楞阔潟湖，距富排机场约30分钟车程。球场由 Sir Nick Faldo 与 IMG London 设计，于2013年3月正式开业，18洞标准杆71杆，总长7,033码，将起伏球道、淡水湖泊与海滨沙丘融为一体。 :contentReference[oaicite:12]{index=12}

1. **概览与历史**  
   作为Banyan Tree高端度假区的重要组成，楞阔球场迅速成为国内外球手青睐之地，举办多项国家业余锦标赛和贵宾邀请赛。 :contentReference[oaicite:13]{index=13}

2. **设计与景观**  
   球洞巧妙利用沙丘与潟湖地形：1号发球台可远眺海湾；6号球道沿湖蜿蜒；白沙沙坑考验精准度，云山水色尽收眼底。 :contentReference[oaicite:14]{index=14}

3. **草坪品质与维护**  
   果岭采用Bentgrass，球道混铺Zoysia和Paspalum，按USGA标准维护；自动灌溉与24/7养护团队确保球场平整光滑。 :contentReference[oaicite:15]{index=15}

4. **设施与服务**  
   现代会所配有高级储物柜、专业球具店、中西餐厅及潟湖观景休息室；专业球童、PGA教练和高尔夫模拟室随时为您服务。 :contentReference[oaicite:16]{index=16}

5. **体验与建议**  
   建议清晨发球，欣赏潟湖在朝阳中闪耀；或黄昏发球，感受夕阳映红球道；赛后可在水疗中心放松或在会所餐厅品尝当地美食。 :contentReference[oaicite:17]{index=17}

6. **预订方式**  
   访问 TeetimeVn.com 或致电 0123456789 进行在线预订，享受最佳价格及全天候支持。'
WHERE course_id = 11 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '拉古娜楞闊高爾夫俱樂部位於越南順化省富祿縣楞闊度假區內，臨近楞闊潟湖，距富排機場約30分鐘車程。由Sir Nick Faldo與IMG London設計，於2013年3月正式營運，18洞標準桿71桿，全長7,033碼，融合起伏球道、淡水湖泊與海濱沙丘。 :contentReference[oaicite:18]{index=18}

1. **總覽與歷史**  
   作為Banyan Tree高端度假項目的一環，楞闊球場迅速成為海內外球手的熱門之選，承辦國家級業餘賽和VIP邀請賽。 :contentReference[oaicite:19]{index=19}

2. **設計與景觀**  
   球洞巧妙利用沙丘及潟湖：1號發球台眺望海灣；6號球道沿湖蜿蜒；白沙沙坑佈局戰略性，四季皆美。 :contentReference[oaicite:20]{index=20}

3. **草坪品質與維護**  
   果嶺為Bentgrass，球道混鋪Zoysia和Paspalum，按USGA標準維護；自動灌溉與24/7綠地團隊確保場地平整。 :contentReference[oaicite:21]{index=21}

4. **設施與服務**  
   現代會所設高級儲物櫃、專業球具店、中西餐廳及潟湖觀景休息室；專業球童、PGA教練及高爾夫模擬室隨時支援。 :contentReference[oaicite:22]{index=22}

5. **體驗與建議**  
   清晨發球可賞潟湖朝陽閃耀；傍晚發球感受夕陽染紅球道；賽後可享水療或在會所品嘗當地美食。 :contentReference[oaicite:23]{index=23}

6. **預訂方式**  
   造訪 TeetimeVn.com 或撥打 0123456789 線上預訂，盡享最佳價格與全天候支援。'
WHERE course_id = 11 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '라구나 랑코 골프 클럽(Laguna Lang Co Golf Club)은 베트남 후아티엔후에성 푸록군 록빈사에 위치한 랑코 석호 인근에 자리하며, 푸바이 공항에서 차로 약 30분 거리입니다. Sir Nick Faldo와 IMG London이 설계하여 2013년 3월 정식 개장한 이 파71 18홀 코스는, 7,033야드의 구릉 페어웨이, 담수 호수, 해안 사구가 어우러진 디자인을 자랑합니다. :contentReference[oaicite:24]{index=24}

1. **개요 및 역사**  
   Banyan Tree의 럭셔리 리조트 개발 프로젝트 일환으로 탄생한 본 코스는, 국내외 골퍼들에게 빠르게 인기를 얻으며 다양한 국가 아마추어 토너먼트 및 VIP 초청 이벤트를 개최해 왔습니다. :contentReference[oaicite:25]{index=25}

2. **코스 디자인 & 경관**  
   홀들은 사구와 석호를 적극 활용하도록 설계되었으며, 1번 티에서 바라보는 만 전경 및 6번 페어웨이의 호수 경관이 인상적입니다. 전략적 벙커 배치가 정확성을 요구합니다. :contentReference[oaicite:26]{index=26}

3. **잔디 품질 및 관리**  
   Bentgrass 그린과 Zoysia·Paspalum 페어웨이가 USGA 기준에 따라 관리되며, 자동 관개 시스템과 24시간 운영되는 그린키퍼 팀이 코스 컨디션을 완벽하게 유지합니다. :contentReference[oaicite:27]{index=27}

4. **시설 및 서비스**  
   모던 클럽하우스에는 프리미엄 라커룸, 프로샵, 아시안·웨스턴 레스토랑, 석호 전망 라운지, 전문 캐디, PGA 코치, 골프 시뮬레이터 룸, 스파 시설이 완비되어 있습니다. :contentReference[oaicite:28]{index=28}

5. **경험 및 팁**  
   이른 아침 티타임에는 석호 위로 떠오르는 일출을, 오후 라운드에는 황금빛 석양을 추천합니다. 라운드 후에는 스파 트리트먼트나 지역 특산 요리를 즐기며 휴식을 만끽하세요. :contentReference[oaicite:29]{index=29}

6. **예약 안내**  
   TeetimeVn.com 방문 또는 0123456789로 전화하시면, 최상의 요금과 24/7 고객 지원을 제공합니다.'
WHERE course_id = 11 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = 'ラグーナ・ランコゴルフクラブ(Laguna Lang Co Golf Club)は、ベトナム フートゥエ省フーロック県ロックヴィン社にあるランコ潟湖畔のラグーナランコリゾート内に位置し、プーバイ空港から車で約30分です。Sir Nick FaldoとIMG Londonが設計し、2013年3月にオープンしたこのパー71・18ホールコースは、7,033ヤードの起伏あるフェアウェイ、淡水湖、自然の砂丘が見事に調和しています。 :contentReference[oaicite:30]{index=30}

1. **概要と歴史**  
   Banyan Treeの高級リゾート開発の一環として誕生し、国内外のゴルファーに愛される本コースは、国内アマチュアトーナメントやVIP招待イベントを数多く開催しています。 :contentReference[oaicite:31]{index=31}

2. **コースデザイン＆景観**  
   ホールは砂丘と潟湖の地形を存分に活かして設計されており、1番ティーから望む湾景、6番フェアウェイ沿いの湖景が抜群です。戦略的に配置された白砂のバンカーがショットの精度を試します。 :contentReference[oaicite:32]{index=32}

3. **芝の品質＆メンテナンス**  
   ベントグラスのグリーンとゾイシア・パスパルム混合フェアウェイはUSGA基準で管理され、自動灌漑システムと24時間体制のグリーンキーパーチームが最高のコースコンディションを維持します。 :contentReference[oaicite:33]{index=33}

4. **施設＆サービス**  
   モダンクラブハウスにはプレミアムロッカー、プロショップ、アジアン・ウェスタンレストラン、潟湖ビューテラスを完備。プロキャディ、PGA認定コーチ、ゴルフシミュレーター、スパなど充実の施設が揃います。 :contentReference[oaicite:34]{index=34}

5. **体験＆アドバイス**  
   早朝ティータイムでは潟湖の朝日を、午後ラウンドでは夕日のフェアウェイを楽しむのがおすすめです。プレー後はスパトリートメントや地元料理で至福のひとときを。 :contentReference[oaicite:35]{index=35}

6. **予約方法**  
   TeetimeVn.comをご覧いただくか0123456789までお電話ください。最適なプランと24時間対応のカスタマーサポートでお手伝いします。'
WHERE course_id = 11 AND lang = 'ja';



-- course_id = 12 (Ba Na Hills Light Golf Course)
UPDATE golf_course_i18n
SET overview = 'Sân golf Ba Na Hills Light tọa lạc tại chân núi Bà Nà, phường Hòa Hải, quận Ngũ Hành Sơn, Đà Nẵng, ở độ cao khoảng 500 m so với mực nước biển, cách trung tâm thành phố 25 km. Được thiết kế bởi IMG London phối hợp cùng Luke Donald và chính thức khai trương năm 2018, sân 18 hố par 72 dài 7.200 yards, kết hợp fairway uốn lượn giữa rừng thông, ao hồ nhân tạo và bunker trắng, mang đến trải nghiệm vừa thử thách vừa thư thái.

1. Tổng quan & Lịch sử  
Xuất phát từ ý tưởng tạo nên sân golf trên núi với khí hậu mát mẻ quanh năm, Ba Na Hills Light nhanh chóng thu hút golfer trong nước và quốc tế. Sân đã đăng cai giải nghiệp dư khu vực và là điểm đến lý tưởng cho các sự kiện teambuilding và gala golf.

2. Thiết kế & Cảnh quan  
Các hố golf tận dụng địa hình dốc nhẹ, rừng thông và cảnh quan đồi núi, xen kẽ bunker và ao hồ tạo thành chướng ngại đầy nghệ thuật. Từ tee box 1, golfer có thể ngắm toàn cảnh Đà Nẵng và Biển Đông; fairway 9 chạy dọc triền đồi thông xanh mướt.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens sử dụng Bentgrass, fairway phối hợp Paspalum nhập khẩu, được chăm sóc theo tiêu chuẩn USGA. Hệ thống tưới tự động thông minh và đội ngũ greenskeeper chuyên nghiệp đảm bảo mặt sân luôn mịn và ổn định.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại với locker cao cấp, pro-shop đa dạng, nhà hàng buffet Á-Âu, lounge ngắm cảnh đồi và spa thư giãn. Dịch vụ caddie chuyên nghiệp, huấn luyện viên PGA và phòng Golf Simulator sẵn sàng phục vụ.

5. Trải nghiệm & Gợi ý  
Thời điểm lý tưởng là buổi sáng sớm khi sương mù giăng lối giữa rừng thông hoặc buổi chiều hoàng hôn nhuộm hồng đỉnh núi. Sau vòng golf, bạn có thể thư giãn tại quán cà phê trên độ cao 500 m hoặc tham quan cáp treo Bà Nà Hills.

6. Hướng dẫn đặt chỗ  
Liên hệ hotline (0236) 3 777 888 hoặc đặt trực tuyến qua TEEtimeVN để nhận ưu đãi tốt nhất và hỗ trợ 24/7.'
WHERE course_id = 12 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = 'Ba Na Hills Light Golf Course is perched at the foot of Ba Na Hills, Hoa Hai ward, Ngu Hanh Son district, Da Nang, at an elevation of approximately 500 m above sea level, 25 km from the city center. Designed by IMG London in collaboration with Luke Donald and opened in 2018, this par-72, 18-hole layout stretches 7,200 yards across rolling fairways, pine forests, man-made lakes, and white-sand bunkers, offering both challenge and serenity.

1. Overview & History  
Conceived to create a mountain golf experience with year-round cool climate, Ba Na Hills Light quickly drew domestic and international players. It has hosted regional amateur tournaments and serves as an ideal venue for corporate teambuilding and golf galas.

2. Course Design & Scenery  
Holes leverage gentle slopes, pine woodland, and hillside vistas, interspersed with bunkers and water hazards for artistic obstacles. From tee box 1 you can survey Da Nang and the East Sea; fairway 9 winds along verdant pine slopes.

3. Turf Quality & Maintenance  
Bentgrass greens and imported Paspalum fairways are maintained to USGA standards. An intelligent irrigation system and a professional greenskeeping team ensure consistently smooth and reliable playing surfaces.

4. Facilities & Services  
The modern clubhouse features premium lockers, a comprehensive pro shop, an Asian-Western buffet restaurant, hilltop lounge, and spa. Professional caddies, PGA-certified coaches, and a Golf Simulator room are on hand for practice and leisure.

5. Experience & Tips  
Ideal tee times are early mornings when mist drifts through the pines, or late afternoons when the sunset bathes the mountain peaks in rose light. After your round, unwind at the 500 m-high café or explore the Ba Na Hills cable car.

6. Booking  
Call (0236) 3 777 888 or reserve online via TEEtimeVN for the best rates and 24/7 assistance.'
WHERE course_id = 12 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '巴拿山光速高爾夫球場位於岘港市五行山區和海南社巴拿山腳下，海拔約500米，距市中心25公里。球場由IMG倫敦與盧克·唐納德(Luke Donald)聯袂設計，於2018年開幕，18洞標準桿72桿，全長7,200碼，球道蜿蜒於松林、人造湖泊和白沙沙坑之間，既具挑戰性又令人心曠神怡。

1. 概覽與歷史  
該球場旨在打造全年涼爽的山地高爾夫體驗，迅速吸引國內外球手。已承辦地區業餘錦標賽，並成為企業團建和高爾夫晚宴的理想場地。

2. 設計與景觀  
各洞充分利用緩坡、松林和山丘美景，並穿插沙坑與水障礙，營造藝術性阻礙。從1號發球台可一覽峴港與東海；9號球道沿松林山坡盤旋。

3. 草坪品質與維護  
果嶺採用Bentgrass，球道鋪設進口Paspalum，並按USGA標準維護。智能灌溉系統與專業養護團隊確保場地始終平滑穩定。

4. 設施與服務  
現代會所配有高級儲物櫃、專業球具店、中西自助餐廳、山頂休息室及SPA。專業球童、PGA認證教練與高爾夫模擬室隨時可供練習與休閒。

5. 體驗與建議  
最佳打法時間是清晨松林薄霧繚繞之時，或黃昏山頂夕陽映照之際。賽後可在500米高的咖啡廳放鬆身心，或乘坐巴拿山纜車遊覽。

6. 預訂方式  
請致電 (0236) 3 777 888 或通過 TEEtimeVN 在線預訂，享受最佳價格及全天候支持。'
WHERE course_id = 12 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '巴拿山光速高爾夫球場位於峴港市五行山區與海南社巴拿山腳下，海拔約500米，距市中心25公里。球場由IMG倫敦與盧克·唐納德(Luke Donald)聯手設計，於2018年開放，18洞標準桿72桿，全長7,200碼，球道蜿蜒於松林、人造湖泊與白沙沙坑之間，既具挑戰性又令人心曠神怡。

1. 總覽與歷史  
本球場旨在打造全年涼爽的山地高爾夫體驗，迅速吸引海內外球手。已承辦地區業餘錦標賽，並成為企業團建和高爾夫晚宴的理想場地。

2. 設計與景觀  
各洞充分利用緩坡、松林和山丘美景，並穿插沙坑與水障礙，營造藝術性阻礙。從1號發球台可一覽峴港與東海；9號球道沿松林山坡盤旋。

3. 草坪品質與維護  
果嶺採用Bentgrass，球道鋪設進口Paspalum，並按USGA標準維護。智能灌溉系統與專業養護團隊確保場地始終平滑穩定。

4. 設施與服務  
現代會所配有高級儲物櫃、專業球具店、中西自助餐廳、山頂休息室及SPA。專業球童、PGA認證教練與高爾夫模擬室隨時可供練習與休閒。

5. 體驗與建議  
最佳打法時間是清晨松林薄霧繚繞之時，或黃昏山頂夕陽映照之際。賽後可在500米高的咖啡廳放鬆身心，或乘坐巴拿山纜車遊覽。

6. 預訂方式  
請致電 (0236) 3 777 888 或透過 TEEtimeVN 在線預訂，享受最佳價格及全天候支持。'
WHERE course_id = 12 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '바나힐즈 라이트 골프 코스(Ba Na Hills Light Golf Course)는 베트남 다낭시 응우행산구 호아하이사 바나힐즈 자락, 해발 약 500미터에 자리하며 도심에서 25km 떨어져 있습니다. IMG 런던과 루크 도널드(Luke Donald)가 협업해 설계하고 2018년 개장한 이 18홀 파72 코스는 7,200야드에 이르는 구릉 페어웨이, 소나무 숲, 인공 호수, 화이트 벙커가 어우러진 디자인을 자랑합니다.

1. 개요 및 역사  
사계절 시원한 산악 골프 경험을 제공하기 위해 탄생한 본 코스는 국내외 골퍼들의 사랑을 받으며 지역 아마추어 대회와 기업 행사 장소로 각광받고 있습니다.

2. 코스 디자인 & 경관  
홀들은 완만한 경사, 소나무 숲, 언덕 경관을 활용하여 전략적 벙커와 수역을 배치했습니다. 1번 티에서 바라보는 다낭 시내와 동해 전망이 일품이며, 9번 페어웨이는 소나무 언덕을 따라 이어집니다.

3. 잔디 품질 및 유지관리  
Bentgrass 그린과 Paspalum 페어웨이는 USGA 표준에 따라 관리되며, 자동 관개 시스템과 프로 그린키퍼 팀이 24시간 코스 컨디션을 유지합니다.

4. 시설 및 서비스  
최신식 클럽하우스에는 프리미엄 라커룸, 프로샵, 아시안-웨스턴 레스토랑, 언덕 전망 라운지, 스파가 마련되어 있습니다. 전문 캐디와 PGA 코치, 골프 시뮬레이터가 연습과 라운드를 지원합니다.

5. 경험 및 팁  
이른 아침 티타임에는 소나무 숲 안개와 함께 떠오르는 일출을, 오후 라운드에서는 언덕 위 황금빛 노을을 추천합니다. 라운드 후 500m 고지 카페나 바나힐즈 케이블카 투어로 여정을 마무리하세요.

6. 예약 안내  
티타임 예약은 (0236) 3 777 888로 전화하거나 TEEtimeVN 웹사이트에서 온라인으로 신청하십시오. 24/7 고객 지원팀이 최적의 일정과 패키지를 도와드립니다.'
WHERE course_id = 12 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = 'バナヒルズライトゴルフコース(Ba Na Hills Light Golf Course)は、ベトナム・ダナン市の五行山区ホアハイ社、バナヒルズ麓の海抜約500mに位置し、市内中心部から25km離れています。IMGロンドンとルーク・ドナルド(Luke Donald)の協働設計で2018年に開場した本パー72・18ホールコースは、7,200ヤードにわたる起伏のあるフェアウェイ、松林、人工湖、白砂のバンカーが融合したデザインが魅力です。

1. 概要と歴史  
一年を通じて涼しい山岳ゴルフ体験を目的に建設され、国内外のゴルファーに愛され、地域アマチュア大会や企業イベントの会場としても人気を博しています。

2. コースデザイン＆景観  
各ホールは緩やかな勾配、松林、丘陵の眺望を活かし、戦略的にバンカーと水域が配置されています。1番ティーからはダナン市街と東シナ海を一望でき、9番フェアウェイは松林の丘を縫うように続きます。

3. 芝の品質＆メンテナンス  
ベントグラスのグリーンとパスパルムのフェアウェイはUSGA基準で管理され、自動灌漑システムとプロのグリーンキーパーチームが24時間コースコンディションを維持します。

4. 施設＆サービス  
モダンなクラブハウスにはプレミアムロッカー、プロショップ、アジアン-ウェスタンレストラン、丘陵を望むラウンジ、スパが完備。専属キャディ、PGA認定コーチ、ゴルフシミュレーターが練習とレジャーをサポートします。

5. 体験＆アドバイス  
早朝ティータイムでは松林に漂う霧と共に昇る朝日を、午後ラウンドでは丘陵に映える夕焼けをおすすめします。ラウンド後は標高500mのカフェやバナヒルズケーブルカーでの観光をお楽しみください。

6. 予約方法  
ティータイムの予約は(0236) 3 777 888までお電話いただくか、TEEtimeVNウェブサイトからオンラインでお申し込みください。24時間対応のカスタマーサポートが最適なプランをご提案します。'
WHERE course_id = 12 AND lang = 'ja';

-- course_id = 13 (Vietnam Golf & Country Club)

UPDATE golf_course_i18n
SET overview = '
Vietnam Golf & Country Club (VGCC) tọa lạc tại phường Long Thạnh Mỹ, Thành phố Thủ Đức, TP. Hồ Chí Minh – cách Q.1 khoảng 17 km và chỉ 30 phút lái xe từ sân bay Tân Sơn Nhất. Khu phức hợp sở hữu 36 hố gồm West Course (khai trương 1994, 18 hố par 72 – 7.106 yards, Kiến trúc sư Chen King Shih) và East Course (khai trương 1997, 18 hố par 72 – 6.946 yards, thiết kế Lee Trevino). Fairway dọc theo hàng cây cổ thụ, hồ nước và bunker trắng mang lại trải nghiệm links-parkland đặc trưng miền nhiệt đới.

1. Tổng quan & Lịch sử  
   Là sân gôn 36 hố đầu tiên tại Việt Nam, VGCC từng đăng cai Vietnam Open (Asian Tour 1995, 1997) và nhiều giải nghiệp dư quốc gia, chính thức mở ra kỷ nguyên golf chuyên nghiệp phía Nam. :contentReference[oaicite:1]{index=1}

2. Thiết kế & Cảnh quan  
   West Course nổi bật với fairway cây đồng bộ, East Course kỹ thuật hơn với hồ nước và green lượn sóng. Mỗi tee shot mở ra tầm nhìn xanh mướt giữa đô thị năng động.

3. Chất lượng sân cỏ & Bảo dưỡng  
   Green Bermuda TifEagle, fairway Bermuda pha Paspalum, bảo dưỡng USGA; hệ thống tưới & aera 24/7 giữ tốc độ green ổn định quanh năm.

4. Cơ sở vật chất & Dịch vụ  
   Clubhouse 2 tầng, locker sang trọng, pro-shop, nhà hàng Âu-Á, sân tập driving-range, hồ bơi, sauna. Caddie chuyên nghiệp, HLV PGA, Golf Simulator.

5. Trải nghiệm & Gợi ý  
   Sáng sớm trải nghiệm Tee Time trong làn sương mịn, chiều muộn ngắm hoàng hôn bên hồ. Đừng bỏ lỡ lẩu bò nổi tiếng tại nhà hàng sân.

6. Hướng dẫn đặt chỗ  
   Truy cập TeetimeVn.com hoặc gọi 0123456789 (24/7) để đặt Tee Time và nhận ưu đãi tốt nhất.'
WHERE course_id = 13 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = '
Vietnam Golf & Country Club (VGCC) lies in Long Thanh My Ward, Thu Duc City, Ho Chi Minh City—about 17 km from District 1 and 30 minutes from Tan Son Nhat Airport. The 36-hole complex features the West Course (opened 1994, par 72 – 7,106 yds, architect Chen King Shih) and the East Course (opened 1997, par 72 – 6,946 yds, designer Lee Trevino). Tree-lined parkland fairways, shimmering lakes and white-sand bunkers create a classic yet tropical setting. :contentReference[oaicite:2]{index=2}

1. Overview & History  
   Vietnam’s first 36-hole venue, VGCC hosted the Asian Tour’s Vietnam Open in 1995 & 1997 and remains a cornerstone of southern golf culture.

2. Course Design & Scenery  
   The West Course winds through mature hardwoods; the East Course demands precision with tighter landing areas and water in play. Every tee offers lush views amid fast-growing suburbia.

3. Turf Quality & Maintenance  
   Bermuda TifEagle greens and hybrid Bermuda/Paspalum fairways are kept to USGA specs by a 24-hour agronomy crew and automated irrigation.

4. Facilities & Services  
   Two-storey clubhouse with premium lockers, full pro-shop, Asian-Western dining, lake-view lounge, driving range, pool & sauna. Certified caddies, PGA coaches, indoor Golf Simulator.

5. Experience & Tips  
   Dawn tee times reveal dew-kissed fairways; late-afternoons deliver vibrant sunsets over the lakes. Sample the club’s renowned beef hot-pot after your round.

6. Booking  
   Visit TeetimeVn.com or call 0123456789 (24/7) for reservations and best-rate guarantees.'
WHERE course_id = 13 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '
越南高尔夫乡村俱乐部（Vietnam Golf & Country Club）位于胡志明市守德市龙盛美坊，距市中心约17 公里，距新山一国际机场约30 分钟车程。球场拥有36洞：西场（1994年启用，72杆，7,106码，设计师陈庆世）与东场（1997年启用，72杆，6,946码，设计师李·特维诺）。古树成荫的球道、湖泊与白沙沙坑勾勒出经典热带园林风格。 :contentReference[oaicite:3]{index=3}

1. 概览与历史  
   作为越南首个36洞球场，VGCC曾承办1995、1997年亚洲巡回赛越南公开赛，是南部高尔夫的标杆。

2. 设计与景观  
   西场林间穿梭，东场水障碍更多、落球区更紧凑；每一次开球都可欣赏热带绿意与湖光。

3. 草坪品质与维护  
   TifEagle Bermuda果岭配合Bermuda/Paspalum球道，全天候自动灌溉与专业团队按USGA标准精养。

4. 设施与服务  
   双层会所设高端储物柜、专业球具店、亚欧美食、湖景酒廊、练习场、泳池及桑拿。职业球童、PGA教练与室内模拟器齐备。

5. 体验与建议  
   清晨雾气缭绕，傍晚夕阳映湖皆宜开球；赛后别忘在餐厅品尝招牌牛肉火锅。

6. 预订方式  
   请访问 TeetimeVn.com 或拨打 0123456789（全天候）预约并享最优价格。'
WHERE course_id = 13 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '
越南高爾夫鄉村俱樂部（Vietnam Golf & Country Club）位於胡志明市守德市龍盛美坊，距市中心約17 公里，距新山一機場約30 分鐘車程。場內設有36洞：西場（1994年啟用，Par 72、7,106碼，設計師陳慶世）與東場（1997年啟用，Par 72、6,946碼，設計師Lee Trevino）。古木夾道、湖泊點綴、白沙沙坑勾勒熱帶園林風貌。 :contentReference[oaicite:4]{index=4}

1. 總覽與歷史  
   作為越南首座36洞球場，VGCC曾於1995、1997年承辦亞洲巡迴賽越南公開賽，為南部高球文化奠基。

2. 設計與景觀  
   西場林間穿梭，東場水障礙更甚、落球區更嚴謹；每一擊皆能飽覽綠蔭與湖景。

3. 草坪品質與維護  
   TifEagle Bermuda果嶺搭配Bermuda/Paspalum球道，24小時自動灌溉，專業團隊依USGA標準養護。

4. 設施與服務  
   兩層會所含高級儲物櫃、專業球具店、亞歐餐廳、湖景酒吧、練習場、泳池與桑拿。職業球童、PGA教練及室內模擬器一應俱全。

5. 體驗與建議  
   破曉晨霧與黃昏落日各有風情；賽後推介品嚐招牌牛肉火鍋。

6. 預訂方式  
   請瀏覽 TeetimeVn.com 或撥打 0123456789（24/7）預訂並享優惠。'
WHERE course_id = 13 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '
베트남 골프 & 컨트리 클럽(VGCC)은 호치민시 투득시 롱탄미 지역에 위치해 있으며, 시내 중심에서 약 17 km, 떤선녓 공항에서 30 분 거리에 있습니다. 36홀 단지로, West Course(1994, Par 72 – 7,106야드, 설계 Chen King Shih)와 East Course(1997, Par 72 – 6,946야드, 설계 Lee Trevino)로 구성됩니다. 울창한 수목 페어웨이와 호수, 흰색 벙커가 열대 파크랜드의 멋을 살립니다. :contentReference[oaicite:5]{index=5}

1. 개요 및 역사  
   베트남 최초의 36홀 코스인 VGCC는 1995·1997 아시안 투어 Vietnam Open 개최지로, 남부 골프 문화의 상징입니다.

2. 코스 디자인 & 경관  
   West는 숲길 레이아웃, East는 워터 해저드가 많아 전략성이 높습니다. 티잉 그라운드마다 녹음과 호수를 조망할 수 있습니다.

3. 잔디 품질 & 관리  
   TifEagle 버뮤다 그린과 버뮤다/파스팔럼 페어웨이는 USGA 기준에 따라 24시간 자동 관개·관리됩니다.

4. 시설 & 서비스  
   2층 클럽하우스(프리미엄 라커, 프로샵, 아시안·웨스턴 레스토랑, 레이크 뷰 라운지), 드라이빙 레인지, 수영장·사우나, PGA 코치, 골프 시뮬레이터 완비.

5. 경험 & 팁  
   새벽 티타임의 이슬 맺힌 페어웨이, 석양이 비추는 호수 라운드 모두 추천. 라운드 후 특제 소고기 전골을 맛보세요.

6. 예약 안내  
   TeetimeVn.com 방문 또는 0123456789(24시간)로 문의하여 최저가로 예약하세요.'
WHERE course_id = 13 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = '
ベトナム・ゴルフ＆カントリークラブ（VGCC）はホーチミン市トゥードゥック市ロンタンミー区に位置し、中心部から約17 km、タンソンニャット国際空港から車で30分です。36ホール構成で、ウエストコース（1994年開場、Par 72・7,106ヤード、設計：Chen King Shih）とイーストコース（1997年開場、Par 72・6,946ヤード、設計：リー・トレビノ）を擁します。樹木に囲まれたフェアウェイと湖、水際の白砂バンカーが南国リンクスとパークランドの魅力を融合します。 :contentReference[oaicite:6]{index=6}

1. 概要と歴史  
   ベトナム初の36ホールコースとして1995・1997年のアジアンツアー「Vietnam Open」を開催し、南部ゴルフ文化の礎となりました。

2. コースデザイン＆景観  
   ウエストは林間、イーストはウォーターハザードが多く戦略性が高い設計。ティーグラウンドからは常に緑と湖面が望めます。

3. 芝質＆メンテナンス  
   TifEagleバミューダグリーンとバミューダ／パスパルムフェアウェイをUSGA基準で管理。自動灌漑と24時間体制のグリーンキーパーにより最高のコンディションを維持。

4. 施設＆サービス  
   2階建てクラブハウス（プレミアムロッカー、プロショップ、アジア・西洋料理レストラン、湖畔ラウンジ）、ドライビングレンジ、プール＆サウナ、PGAコーチ、ゴルフシミュレーター完備。

5. 体験＆アドバイス  
   夜明けの霧に包まれたティーショット、夕暮れの湖に映るサンセットは必見。プレー後は名物ビーフホットポットで締めくくりを。

6. 予約方法  
   TeetimeVn.com へアクセス、または 0123456789（24時間）にお電話ください。最適料金でご案内します。'
WHERE course_id = 13 AND lang = 'ja';


-- course_id = 14 (Twin Doves Golf Club)
UPDATE golf_course_i18n
SET overview = 'Sân golf Twin Doves Golf Club toạ lạc tại phường Lái Thiêu, thành phố Thuận An, tỉnh Bình Dương – cách trung tâm TP.HCM khoảng 32 km (45 phút lái xe) và sân bay Tân Sơn Nhất 30 phút. Khai trương tháng 12 năm 2011, sân do kiến trúc sư người Mỹ Peter Rousseau thiết kế, sở hữu 27 hố (3 cụm 9 hố: Luna, Stella, Sole). Khi ghép 18 hố bất kỳ, sân đạt chuẩn par 72 với chiều dài tối đa 7.282 yards – đạt chuẩn quốc tế và là CLB private đầu tiên ở Việt Nam.:contentReference[oaicite:0]{index=0}

1. Tổng quan & Lịch sử  
   Được phát triển nhằm đáp ứng nhu cầu golf cao cấp phía Nam, Twin Doves nhanh chóng trở thành điểm hẹn của golfer trong nước lẫn quốc tế, đăng cai nhiều giải nghiệp dư và các vòng loại chuyên nghiệp.

2. Thiết kế & Cảnh quan  
   Ba cụm 9 hố uốn quanh đồi cát, hồ nước và rặng cây cao su đặc trưng Bình Dương; tee box 1 của nửa vòng Luna mở ra toàn cảnh hồ trung tâm, trong khi các bunker trắng và suối nhân tạo tạo thử thách chiến lược.

3. Chất lượng sân cỏ & Bảo dưỡng  
   Greens Bentgrass mượt, fairway Paspalum duy trì theo tiêu chuẩn USGA; hệ thống tưới tự động & đội ngũ greenskeeper túc trực 24/7 bảo đảm tốc độ bóng ổn định quanh năm.

4. Cơ sở vật chất & Dịch vụ  
   Clubhouse sang trọng gồm locker cao cấp, pro-shop, nhà hàng Á-Âu, lounge nhìn hồ; kèm spa, sân tập đèn đêm, phòng Golf Simulator, đội caddie chuyên nghiệp và HLV PGA.

5. Trải nghiệm & Gợi ý  
   Sáng sớm mùa khô (tháng 11–3) trời mát, sương nhẹ trên fairway; chiều muộn ngắm hoàng hôn bên hồ Stella. Đừng bỏ qua ẩm thực Bình Dương tại nhà hàng sân golf sau vòng chơi.

6. Đặt chỗ  
   Gọi 0123456789 hoặc đặt tee-time trực tuyến tại TeetimeVn.com – hỗ trợ 24/7.'
WHERE course_id = 14 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = 'Twin Doves Golf Club lies in Lai Thieu Ward, Thuan An City, Binh Duong Province – roughly 32 km (about 45 minutes) north of downtown Ho Chi Minh City and 30 minutes from Tan Son Nhat Airport. Officially opened in December 2011 and designed by American architect **Peter Rousseau**, the private-members club offers 27 holes (three 9-hole loops: Luna, Stella, Sole). Any 18-hole combination plays to a par 72 and stretches up to 7,282 yards.:contentReference[oaicite:1]{index=1}

1. Overview & History  
   Created to anchor premium golf in southern Vietnam, Twin Doves has hosted regional amateur championships and professional qualifiers, drawing local and international golfers alike.

2. Course Design & Scenery  
   Rolling sand-based terrain, lakes and mature rubber trees frame each hole; Luna’s 1st tee overlooks the central lake, while white-sand bunkers and meandering streams demand strategic thinking.

3. Turf Quality & Maintenance  
   Smooth Bentgrass greens and Paspalum fairways are maintained to USGA standards via fully automated irrigation and a 24/7 agronomy crew, guaranteeing consistent speed and lies year-round.

4. Facilities & Services  
   A contemporary clubhouse offers premium lockers, a well-stocked pro-shop, an Asian-Western restaurant and lake-view lounge, plus flood-lit driving range, Golf Simulator, PGA coaches and professional caddies.

5. Experience & Tips  
   Opt for early-morning tee times in the dry season (Nov–Mar) for cool air and pastel skies, or late-afternoon rounds to enjoy sunset over Stella’s lake. Reward yourself with local Bình Dương cuisine afterwards.

6. Booking  
   Phone 0123456789 or secure tee times at TeetimeVn.com – assistance available 24/7.'
WHERE course_id = 14 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = 'Twin Doves 高尔夫俱乐部位于越南平阳省顺安市赖𦨭坊，距胡志明市中心约32公里（车程45分钟），距新山一机场约30分钟。球场于2011年12月开放，由美国设计师Peter Rousseau操刀，是越南首家私属会员制27洞球场（三个9洞：Luna、Stella、Sole），18洞组合标准杆72，最长7,282码。:contentReference[oaicite:2]{index=2}

1. 概览与历史  
   作为南部高端高尔夫旗舰，Twin Doves承办多场区域业余赛及职业资格赛，备受国内外球手青睐。

2. 设计与景观  
   球洞依沙质丘陵、湖泊及橡胶林布局；Luna 1号发球台俯瞰中央湖，白沙沙坑与溪流交错，挑战策略。

3. 草坪与养护  
   Bentgrass果岭、Paspalum球道按USGA标准维护，自动灌溉与24小时养护团队确保全年如一的顺滑速度。

4. 设施与服务  
   现代会所设高级更衣柜、专业球具店、亚欧餐厅、湖景酒廊，并配灯光练习场、模拟器、PGA教练与专业球童。

5. 体验与建议  
   冬春旱季清晨凉爽宜人；傍晚夕阳映湖景尤佳。完赛后品尝平阳特色美食或放松SPA。

6. 预订  
   致电0123456789或登陆TeetimeVn.com在线预订，全天候客服支持。'
WHERE course_id = 14 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = 'Twin Doves 高爾夫俱樂部位於越南平陽省順安市賴𦨭坊，距胡志明市中心約32公里（45分鐘車程），距新山一機場約30分鐘。球場於2011年12月開幕，由美籍設計師Peter Rousseau設計，是越南首家私屬會員制27洞球場（三組9洞：Luna、Stella、Sole），任意18洞組合為標準桿72，最長7,282碼。:contentReference[oaicite:3]{index=3}

1. 總覽與歷史  
   Twin Doves作為南部頂級高爾夫旗艦，承辦多場區域業餘賽及職業資格賽，深受海內外球手喜愛。

2. 設計與景觀  
   沙質丘陵、湖泊及橡膠林交織成景；Luna 1號開球台可俯瞰中央湖，白沙沙坑與溪流增添策略挑戰。

3. 草坪與維護  
   Bentgrass果嶺、Paspalum球道依USGA標準維護，配合自動灌溉及24小時養護團隊，確保全年速度穩定。

4. 設施與服務  
   現代會所設高級儲物櫃、專業球具店、亞歐餐廳、湖景酒廊，並提供燈光練習場、模擬器、PGA教練及專業球童。

5. 體驗與建議  
   旱季清晨涼爽，傍晚夕陽映湖最為動人；完賽後可於SPA或酒吧放鬆，品嚐平陽美食。

6. 預訂  
   請撥0123456789或登入TeetimeVn.com線上預訂，24/7客服隨時支援。'
WHERE course_id = 14 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '트윈도브스 골프 클럽은 베트남 빈증성 순안시 라이티우 지역에 위치하며, 호치민 시내에서 북쪽으로 약 32 km(차로 45분), 떤선녓 공항에서 30 분 거리입니다. 2011년 12월 미국 설계자 피터 루소(Peter Rousseau)가 설계해 개장했으며, 루나·스텔라·솔레 3개 9홀(총 27홀)로 구성된 베트남 최초의 프라이빗 멤버십 코스입니다. 18홀 조합 시 파72, 최장 7,282야드입니다.:contentReference[oaicite:4]{index=4}

1. 개요 및 역사  
   남부 프리미엄 골프 허브로 자리 잡은 트윈도브스는 지역 아마추어 챔피언십과 프로 예선전을 개최하며 국내외 골퍼들에게 사랑받고 있습니다.

2. 코스 디자인 & 경관  
   사질 구릉, 호수, 고무나무 숲이 어우러진 레이아웃으로, 루나 1번 티에서 중앙 호수를 조망할 수 있습니다. 화이트 벙커와 시냇물이 전략적 요소를 강화합니다.

3. 잔디 품질 & 관리  
   벤트그라스 그린과 파스팔럼 페어웨이는 USGA 기준으로 유지되며, 자동 관개 시스템과 24시간 그린키퍼 팀이 완벽한 상태를 유지합니다.

4. 시설 & 서비스  
   현대적인 클럽하우스에는 프리미엄 라커, 프로샵, 아시아·웨스턴 레스토랑, 레이크뷰 라운지가 있으며 조명 연습장·골프 시뮬레이터·PGA 코치·프로 캐디가 지원합니다.

5. 경험 & 팁  
   건기(11–3월) 새벽 티타임에는 선선한 날씨와 안개 낀 페어웨이가, 석양 무렵에는 호수를 물들이는 노을이 일품입니다. 라운드 후 스파나 바에서 휴식을 즐기세요.

6. 예약 안내  
   0123456789로 전화하거나 TeetimeVn.com에서 온라인 예약하세요. 24시간 고객 지원이 가능합니다.'
WHERE course_id = 14 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = 'トゥインドーブスゴルフクラブは、ホーチミン市中心部から北へ約32 km（車で45分）、タンソンニャット空港から30 分のビンズオン省スアンアン市ライティエウ地区に位置します。2011年12月に米国の設計家ピーター・ルソーが設計し開場した、ベトナム初の会員制27ホールコース（Luna、Stella、Soleの3つの9ホール）。18ホール組合せでパー72、最長7,282ヤードです。:contentReference[oaicite:5]{index=5}

1. 概要と歴史  
   南部ベトナムのハイエンドゴルフ拠点として誕生し、地域アマチュア大会やプロ予選会の開催地として国内外ゴルファーに支持されています。

2. コースデザイン＆景観  
   砂質の丘陵地、湖、ゴム林を活かしたレイアウトで、Luna 1番ティーからは中央湖を一望。白砂バンカーと小川が戦略性を高めます。

3. 芝の品質＆メンテナンス  
   ベントグラスグリーンとパスパルムフェアウェイはUSGA基準で管理され、自動灌漑と24時間のグリーンキーパーチームにより常に最良の状態を維持。

4. 施設＆サービス  
   近代的なクラブハウスにはプレミアムロッカー、プロショップ、アジア・西洋料理レストラン、湖畔ラウンジのほか、照明付き練習場、ゴルフシミュレーター、PGAコーチ、プロキャディが揃います。

5. 体験＆アドバイス  
   乾季の早朝は涼しく霧がかかり、夕刻は湖面を染めるサンセットが絶景。プレー後はスパやバーでくつろぎ、ビンズオンの郷土料理を味わいましょう。

6. 予約方法  
   0123456789に電話、またはTeetimeVn.comからオンライン予約。24時間体制でサポートします。'
WHERE course_id = 14 AND lang = 'ja';


-- course_id = 15 (Sanctuary Hồ Tràm Golf Club)
UPDATE golf_course_i18n
SET overview = 'Sanctuary Hồ Tràm Golf Club nằm trong quần thể nghỉ dưỡng Hồ Tràm Beach, xã Phước Thuận, huyện Xuyên Mộc, tỉnh Bà Rịa – Vũng Tàu, cách TP. Hồ Chí Minh khoảng 120 km. Được thiết kế bởi IMG London và bác sỹ Nick Faldo hợp tác tư vấn, sân 18 hố par 72 dài 7.050 yards chính thức khai trương năm 2019. Với fairway dọc theo đồi cát ven biển và bunker trắng trải rộng, sân mang phong cách links truyền thống hòa quyện cùng cảnh biển Đông hùng vĩ.

1. Tổng quan & Lịch sử  
Khởi nguồn từ dự án phát triển du lịch biển cao cấp, Sanctuary Hồ Tràm nhanh chóng trở thành điểm đến ưa thích của golf thủ trong và ngoài nước. Sân đã đăng cai các giải nghiệp dư vùng và tổ chức nhiều sự kiện doanh nghiệp.

2. Thiết kế & Cảnh quan  
Fairway uốn lượn quanh đồi cát tự nhiên, kết hợp các hồ nước ngọt và bunker chiến lược. Từ tee box 1, golfer có thể chiêm ngưỡng biển xanh; fairway 9 chạy dọc bờ hồ chắn gió, tạo thử thách về độ chính xác và cự ly.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens Bentgrass và fairway Paspalum được bảo dưỡng theo tiêu chuẩn USGA. Hệ thống tưới tự động thông minh cùng đội ngũ greenskeeper chuyên nghiệp làm việc 24/7, bảo đảm mặt sân luôn mịn màng và đồng đều.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại với locker cao cấp, pro-shop đa dạng, nhà hàng Á-Âu và lounge nhìn ra biển. Dịch vụ caddie chuyên nghiệp, huấn luyện viên PGA và phòng Golf Simulator đáp ứng mọi nhu cầu luyện tập và giải trí.

5. Trải nghiệm & Gợi ý  
Thời điểm lý tưởng là sáng sớm khi gió biển nhẹ nhàng và hoàng hôn muộn trên fairway tạo khung cảnh lãng mạn. Sau vòng golf, bạn có thể tận hưởng spa hoặc dạo biển tại hồ bơi vô cực của resort.

6. Hướng dẫn đặt chỗ  
Liên hệ hotline (0254) 3 888 999 hoặc đặt trực tuyến qua TEEtimeVN để nhận ưu đãi tốt nhất và hỗ trợ 24/7.'
WHERE course_id = 15 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = 'Sanctuary Ho Tram Golf Club is set within the Ho Tram Beach resort complex in Phuoc Thuan Commune, Xuyen Moc District, Ba Ria–Vung Tau Province, approximately 120 km from Ho Chi Minh City. Designed by IMG London with consulting from Nick Faldo and opened in 2019, this par-72, 18-hole layout stretches 7,050 yards along coastal dunes and white-sand bunkers, blending classic links style with sweeping East Sea vistas.

1. Overview & History  
Conceived as part of a premium seaside resort project, Sanctuary Ho Tram quickly became a favorite for domestic and international players. The course has hosted regional amateur championships and numerous corporate events.

2. Course Design & Scenery  
Fairways weave through natural dunes, accented by freshwater lakes and strategically placed bunkers. Tee box 1 offers panoramic ocean views; fairway 9 meanders along a wind-shielding water hazard, testing both accuracy and distance control.

3. Turf Quality & Maintenance  
Bentgrass greens and Paspalum fairways are maintained to USGA standards. An intelligent irrigation system and a dedicated 24/7 greenskeeping team ensure consistently smooth and even playing surfaces.

4. Facilities & Services  
The modern clubhouse features premium lockers, a diverse pro shop, an Asian-Western restaurant, and a sea-view lounge. Professional caddies, PGA-certified coaches, and a Golf Simulator room cater to all practice and leisure needs.

5. Experience & Tips  
Ideal tee times are early morning when the sea breeze is mild or late afternoon for romantic sunset rounds. After your round, unwind at the spa or stroll along the resort’s infinity pool overlooking the beach.

6. Booking  
Call (0254) 3 888 999 or book online via TEEtimeVN for the best rates and 24/7 assistance.'
WHERE course_id = 15 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '圣殿霍特拉姆高尔夫俱乐部坐落在巴地头顿省Xuyên Mộc县Phước Thuận社的Hồ Tràm Beach度假区内，距胡志明市约120公里。球场由IMG伦敦设计，并由高球传奇Nick Faldo顾问，于2019年开放，此18洞标准杆72杆球场全长7,050码，沿海岸沙丘及白沙沙坑布局，将传统链接斯风格与壮阔东海景观完美融合。

1. 概览与历史  
作为高端海滨度假项目的一部分，圣殿霍特拉姆迅速成为国内外球手的首选。球场曾举办区域业余锦标赛及多场企业赛事。

2. 设计与景观  
球道蜿蜒于自然沙丘之间，点缀淡水湖泊和战略性沙坑。1号发球台可俯瞰海景；9号球道环绕防风水障碍，考验击球精准度与距离控制。

3. 草坪品质与维护  
果岭为Bentgrass，球道为Paspalum，均按USGA标准维护。智能灌溉系统与全天候绿地团队确保场地始终平整如新。

4. 设施与服务  
现代会所设有高级储物柜、专业球具店、中西餐厅及海景休息室。专业球童、PGA认证教练和高尔夫模拟室满足练习与休闲需求。

5. 体验与建议  
清晨海风徐徐，或傍晚落日余晖，是最佳发球时段。赛后可在度假村Infinity池畔漫步或享受Spa护理。

6. 预订方式  
请致电 (0254) 3 888 999 或通过 TEEtimeVN 在线预订，享受最优价格及全天候服务。'
WHERE course_id = 15 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '聖殿霍特拉姆高爾夫俱樂部位於巴地頭頓省Xuyên Mộc縣Phước Thuận社的Hồ Tràm Beach度假區內，距胡志明市約120公里。球場由IMG倫敦設計並由高球傳奇Nick Faldo顧問，於2019年開放，18洞標準桿72桿，全長7,050碼，沿海岸沙丘及白沙沙坑布局，將傳統連結斯風格與壯麗東海景觀融為一體。

1. 總覽與歷史  
作為高端海濱度假項目的一部分，聖殿霍特拉姆迅速成為國內外球手的首選。球場曾舉辦區域業餘錦標賽及多場企業賽事。

2. 設計與景觀  
球道蜿蜒於自然沙丘之間，點綴淡水湖泊和策略性沙坑。1號發球台可俯瞰海景；9號球道環繞防風水障礙，考驗擊球精準度與距離控制。

3. 草坪品質與維護  
果嶺為Bentgrass，球道為Paspalum，均按USGA標準維護。智能灌溉系統與全天候綠地團隊確保場地始終平整如新。

4. 施設與服務  
現代會所設有高級儲物櫃、專業球具店、中西餐廳及海景休息室。專業球童、PGA認證教練和高爾夫模擬室滿足練習與休閒需求。

5. 體驗與建議  
清晨海風徐徐，或傍晚落日餘暉，是最佳發球時段。賽後可在度假村Infinity池畔漫步或享受Spa護理。

6. 預訂方式  
請致電 (0254) 3 888 999 或透過 TEEtimeVN 在線預訂，享受最優價格及全天候服務。'
WHERE course_id = 15 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '생추어리 호짬 골프 클럽(Sanctuary Ho Tram Golf Club)은 바리아굴리앙투옹성 Xuyên Mộc군 Phước Thuận사에 위치한 Ho Tram Beach 리조트 단지 내에 자리하며, 호치민시에서 약 120km 떨어져 있습니다. IMG 런던이 설계하고 니클 팰도(Nick Faldo)가 자문한 이 파72 18홀 코스는 2019년에 개장했으며, 7,050야드에 이르는 해안 사구와 화이트 벙커가 어우러진 링크스 스타일 레이아웃을 자랑합니다.

1. 개요 및 역사  
고급 해변 리조트 프로젝트의 일환으로 탄생한 본 클럽은 국내외 골퍼들의 사랑을 받으며 지역 아마추어 대회와 기업 이벤트를 개최해 왔습니다.

2. 코스 디자인 & 경관  
홀은 자연 사구 사이를 유려하게 연결하며, 담수 호수와 전략적 벙커가 도전 과제를 제공합니다. 1번 티에서는 탁 트인 바다 전망을, 9번 페어웨이에서는 방풍 수역을 따라 라운드를 즐길 수 있습니다.

3. 잔디 품질 및 유지관리  
Bentgrass 그린과 Paspalum 페어웨이는 USGA 기준으로 관리되며, 지능형 관개 시스템과 24시간 운영되는 그린키퍼 팀이 완벽한 코스 컨디션을 유지합니다.

4. 시설 및 서비스  
모던한 클럽하우스에는 프리미엄 라커룸, 프로샵, 아시안-웨스턴 레스토랑, 바다 전망 라운지 및 스파가 마련되어 있으며, 전문 캐디와 PGA 코치, 골프 시뮬레이터가 연습과 라운드를 지원합니다.

5. 경험 및 팁  
이른 아침 해풍과 부드러운 햇살을, 저녁엔 황금빛 노을을 감상할 수 있는 티타임이 추천됩니다. 라운드 후 인피니티 풀이나 스파에서 여유를 만끽해 보세요.

6. 예약 안내  
티타임 예약은 (0254) 3 888 999로 전화하거나 TEEtimeVN 웹사이트에서 온라인으로 신청하세요. 24/7 고객 지원팀이 최적의 일정과 패키지를 도와드립니다.'
WHERE course_id = 15 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = 'サンクチュアリーホーチャムゴルフクラブ(Sanctuary Ho Tram Golf Club)は、ベトナムバリア─ブンタウ省Xuyên Mộc地区Phước Thuận社のHo Tram Beachリゾート内に位置し、ホーチミン市から約120km離れています。IMGロンドンが設計し、ゴルフレジェンドのニック・ファルドがアドバイザーを務めたこのパー72・18ホールコースは、2019年にオープンし、7,050ヤードに及ぶリンクススタイルのレイアウトが特徴です。

1. 概要と歴史  
高級シーサイドリゾートプロジェクトの一環として誕生し、国内外のゴルファーに支持され、地域アマチュア大会や企業イベントの会場としても利用されています。

2. コースデザイン＆景観  
フェアウェイは自然な砂丘を活かし、淡水湖と戦略的なバンカーが挑戦を演出します。1番ティーからは壮大な海景を、9番フェアウェイからは防風水域沿いのコースを楽しめます。

3. 芝の品質＆メンテナンス  
ベントグラスのグリーンとパスパルムのフェアウェイはUSGA基準で管理され、自動かんがいシステムと24時間体制のグリーンキーパーチームが常に最高のコンディションを維持します。

4. 施設＆サービス  
モダンクラブハウスにはプレミアムロッカー、プロショップ、アジアン・ウェスタンレストラン、オーシャンビューラウンジ、スパ施設を完備。専属キャディとPGAコーチ、ゴルフシミュレーターも利用可能です。

5. 体験＆アドバイス  
早朝の海風とやわらかな陽光、夕方のゴールデンアワーが美しいティータイムを演出します。ラウンド後はインフィニティプールやスパでくつろいでください。

6. 予約方法  
ティータイムの予約は(0254) 3 888 999までお電話いただくか、TEEtimeVNウェブサイトからオンラインでお申し込みください。24時間対応のカスタマーサポートが最適なプランを提案します。'
WHERE course_id = 15 AND lang = 'ja';


-- course_id = 16 (Vinpearl Phú Quốc Golf Course)
UPDATE golf_course_i18n
SET overview = 'Sân golf Vinpearl Phú Quốc tọa lạc tại bãi biển Ông Lang, huyện Phú Quốc, tỉnh Kiên Giang, chỉ cách sân bay Phú Quốc 10 phút lái xe. Được thiết kế bởi IMG phối hợp cùng Sir Nick Faldo và chính thức khai trương năm 2014, sân 18 hố par-72 dài 7.189 yards uốn lượn qua cồn cát ven biển, rừng dương liễu và bunkers trắng tinh.

1. Tổng quan & Lịch sử  
Vinpearl Phú Quốc được phát triển nằm trong quần thể nghỉ dưỡng đẳng cấp của Vinpearl, nhanh chóng trở thành điểm đến yêu thích của golfer trong và ngoài nước. Sân đã đăng cai các giải chuyên nghiệp và là nơi tập huấn cho nhiều đội tuyển.

2. Thiết kế & Cảnh quan  
Các hố golf tận dụng địa hình cồn cát tự nhiên, kết hợp bunker chiến lược và hồ nước điểm xuyết giữa fairway. Tee box 1 cho tầm nhìn bao quát vịnh Thái Lan, fairway 9 chạy dọc theo rừng dương liễu.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens sử dụng Bentgrass, fairway phối hợp Paspalum và Zoysia nhập khẩu, bảo dưỡng nghiêm ngặt theo tiêu chuẩn USGA. Hệ thống tưới tự động và đội ngũ greenskeeper chuyên nghiệp hoạt động 24/7 đảm bảo mặt sân luôn mịn mượt.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse hiện đại với locker cao cấp, pro-shop đa dạng, nhà hàng Á-Âu và lounge ngắm biển. Dịch vụ caddie chuyên nghiệp, huấn luyện viên PGA, phòng Golf Simulator và spa đều sẵn sàng phục vụ.

5. Trải nghiệm & Gợi ý  
Thời điểm lý tưởng là sáng sớm khi bình minh trên biển hoặc chiều hoàng hôn khi gió biển lồng lộng. Sau vòng golf, bạn có thể thư giãn tại spa hoặc ngắm hoàng hôn từ bar trên cao.

6. Hướng dẫn đặt chỗ  
Liên hệ hotline (0297) 3 789 999 hoặc đặt trực tuyến qua Vinpearl.com để nhận ưu đãi tốt nhất và hỗ trợ 24/7.'
WHERE course_id = 16 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = 'Vinpearl Phu Quoc Golf Course is located on Ong Lang Beach, Phu Quoc Island, Kien Giang Province, just a 10-minute drive from Phu Quoc Airport. Designed by IMG in collaboration with Sir Nick Faldo and opened in 2014, this par-72, 18-hole layout stretches 7,189 yards through coastal dunes, casuarina groves, and pristine white bunkers.

1. Overview & History  
Developed as part of the world-class Vinpearl resort ecosystem, Vinpearl Phu Quoc quickly became a favorite among domestic and international golfers. The club has hosted professional tournaments and serves as a training venue for top teams.

2. Course Design & Scenery  
Holes leverage natural dune formations with strategic bunkers and water features woven through the fairways. Tee box 1 offers panoramic views of the Gulf of Thailand; fairway 9 winds along casuarina-lined shores.

3. Turf Quality & Maintenance  
Bentgrass greens and Paspalum-Zoysia fairways are meticulously maintained to USGA standards. An automated irrigation system and 24/7 greenskeeping team ensure consistently smooth playing surfaces.

4. Facilities & Services  
The modern clubhouse features premium lockers, a well-stocked pro shop, an Asian-Western restaurant, a sea-view lounge, professional caddies, PGA coaches, a Golf Simulator, and a spa.

5. Experience & Tips  
Ideal tee times are early morning at dawn or late afternoon in the sea breeze. After your round, unwind at the spa or enjoy sunset cocktails at the rooftop bar.

6. Booking  
Call (0297) 3 789 999 or book online at Vinpearl.com for the best rates and 24/7 assistance.'
WHERE course_id = 16 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '珍珠岛高尔夫俱乐部位于越南富国岛Ông Lang海滩，靠近富国机场仅10分钟车程。该球场由IMG与爵士尼克·法尔多合作设计，2014年开业，18洞标准杆72杆，总长7,189码，球道蜿蜒于海岸沙丘、刺槐林和洁白沙坑之间。

1. 概览与历史  
作为Vinpearl五星度假区的一部分，富国珍珠岛高尔夫迅速成为国内外球手的首选。球场承办过多项职业赛事，并为顶级球队提供训练场地。

2. 设计与景观  
球洞充分利用自然沙丘地形，巧妙布置沙坑和水障碍。1号发球台可纵览泰国湾全景；9号球道沿刺槐林展开，景色宜人。

3. 草坪品质与维护  
果岭采用Bentgrass，球道由Paspalum与Zoysia混铺，严格按照USGA标准维护。自动灌溉系统与24/7养护团队确保球场始终平滑如新。

4. 设施与服务  
现代化会所配备高级储物柜、专业球具店、中西餐厅、海景休息室、专业球童、PGA教练、高尔夫模拟器和水疗中心。

5. 体验与建议  
清晨曙光或傍晚海风下的发球是最佳体验。赛后可在水疗中心放松，或在屋顶酒吧欣赏日落美景。

6. 预订方式  
请致电 (0297) 3 789 999 或访问 Vinpearl.com 在线预订，享受最优价格及全天候支持。'
WHERE course_id = 16 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '珍珠島高爾夫俱樂部位於越南富國島Ông Lang海灘，距富國機場僅10分鐘車程。球場由IMG與爵士尼克·法爾多合作設計，2014年開幕，18洞標準桿72桿，全長7,189碼，球道蜿蜒於海岸沙丘、刺槐林與白沙沙坑之間。

1. 總覽與歷史  
作為Vinpearl五星度假區的一部分，富國珍珠島高爾夫迅速成為國內外球手首選。球場承辦多項職業賽事，並為頂級球隊提供訓練場地。

2. 設計與景觀  
球洞充分利用自然沙丘地形，巧妙配置沙坑與水障礙。1號發球台可飽覽泰國灣全景；9號球道沿刺槐林展開，景色怡人。

3. 草坪品質與維護  
果嶺採用Bentgrass，球道由Paspalum與Zoysia混鋪，嚴格依USGA標準維護。自動灌溉系統與24/7養護團隊確保球場始終平滑如新。

4. 施設與服務  
現代化會所配備高級儲物櫃、專業球具店、中西餐廳、海景休息室、專業球童、PGA教練、高爾夫模擬器與水療中心。

5. 體驗與建議  
清晨曙光或傍晚海風下的發球為最佳體驗。賽後可在水療中心放鬆，或在屋頂酒吧賞日落美景。

6. 預訂方式  
請致電 (0297) 3 789 999 或訪問 Vinpearl.com 在線預訂，享受最優價格及全天候支持。'
WHERE course_id = 16 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '빈펄푸꾸옥 골프 클럽(Vinpearl Phu Quoc Golf Club)은 베트남 깐장성 푸꾸옥군 Ông Lang 해변에 위치하며, 푸꾸옥공항에서 차로 10분 거리입니다. IMG와 닉 팔도가 협업해 설계한 이 파72 18홀 코스는 2014년 개장했으며, 7,189야드에 달하는 해안 사구, 가시나무 숲, 화이트 벙커가 어우러진 레이아웃을 자랑합니다.

1. 개요 및 역사  
빈펄 리조트의 일환으로 개발된 본 골프장은 국내외 골퍼들에게 빠르게 사랑받으며, 프로 대회 개최와 팀 훈련 장소로 활용되고 있습니다.

2. 코스 디자인 & 경관  
홀은 자연 사구 지형을 따라 이어지며 전략적 벙커와 수역이 배치되었습니다. 1번 티에서 바라보는 태국만 전경과 9번 페어웨이의 가시나무 숲 경관이 인상적입니다.

3. 잔디 품질 및 유지 관리  
Bentgrass 그린과 Paspalum·Zoysia 페어웨이는 USGA 기준에 따라 관리되며, 자동 관개 시스템과 24시간 그린키퍼 팀이 완벽한 상태를 유지합니다.

4. 시설 및 서비스  
모던 클럽하우스에는 프리미엄 라커룸, 프로샵, 아시안·웨스턴 레스토랑, 오션뷰 라운지, 프로 캐디, PGA 코치, 골프 시뮬레이터, 스파가 갖춰져 있습니다.

5. 경험 및 팁  
이른 아침 일출과 부드러운 해풍, 오후 일몰 라운드가 모두 매력적입니다. 라운드 후 스파에서 휴식을 취하거나 옥상 바에서 칵테일을 즐기세요.

6. 예약 안내  
티타임 예약은 (0297) 3 789 999로 전화하거나 Vinpearl.com에서 온라인으로 신청하세요. 24/7 고객 지원팀이 최적의 일정을 도와드립니다.'
WHERE course_id = 16 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = 'ヴィンパールフーコックゴルフクラブ(Vinpearl Phu Quoc Golf Club)は、ベトナムキエンザン省フーコック郡Ông Langビーチに位置し、フーコック空港から車で約10分です。IMGとサー・ニック・ファルドが協働設計し、2014年にオープンしたこのパー72・18ホールコースは、全長7,189ヤードにわたる沿岸砂丘、カシアの林、白砂のバンカーが調和したレイアウトが特徴です。

1. 概要と歴史  
ヴィンパールリゾートの一翼として開発され、本クラブは国内外のゴルファーに愛され、プロトーナメントやチームトレーニングの会場としても利用されています。

2. コースデザイン＆景観  
ホールは自然砂丘に沿ってレイアウトされ、戦略的なバンカーとウォーターハザードが配置されています。1番ティーから望むタイ湾の大パノラマと、9番フェアウェイのカシア林が印象的です。

3. 芝の品質＆メンテナンス  
ベントグラスグリーンとパスパルム・ゾイシアフェアウェイはUSGA基準で管理され、自動灌漑システムと24時間体制のグリーンキーパーチームが完璧なコースコンディションを維持します。

4. 施設＆サービス  
モダンなクラブハウスにはプレミアムロッカー、プロショップ、アジアン・ウェスタンレストラン、オーシャンビューテラス、プロキャディ、PGAコーチ、ゴルフシミュレーター、スパが完備されています。

5. 体験＆アドバイス  
早朝のサンライズラウンドや、午後のシーウィンドとサンセットラウンドがおすすめです。ラウンド後はスパでリラックスしたり、ルーフトップバーでカクテルを楽しんでください。

6. 予約方法  
ティータイムの予約は(0297) 3 789 999までお電話いただくか、Vinpearl.comでオンライン予約をお申し込みください。24時間対応のカスタマーサポートが最適なプランをご案内します。'
WHERE course_id = 16 AND lang = 'ja';



-- course_id = 17 (Đà Lạt 1200 Golf Club)
UPDATE golf_course_i18n
SET overview = 'Sân golf Đà Lạt 1200 nằm tại thị trấn Lạc Dương, Lâm Đồng, trên cao nguyên Lang Biang ở độ cao khoảng 1.200 m so với mực nước biển, cách trung tâm Đà Lạt 25 km. Được thiết kế bởi IMG London và chính thức khai trương năm 2018, sân 18 hố par 72 dài 7.085 yards uốn lượn giữa rừng thông, hồ nước và thảm cỏ tự nhiên.

1. Tổng quan & Lịch sử  
Đà Lạt 1200 ra đời nhằm khai thác tiềm năng golf trên cao nguyên Lâm Viên, với khí hậu mát mẻ quanh năm và khung cảnh núi rừng hùng vĩ. Sân đã tổ chức các giải nghiệp dư khu vực và thu hút golf thủ quốc tế.

2. Thiết kế & Cảnh quan  
Fairway tận dụng đường nét đồi thông, xen kẽ hồ nhỏ và bunker trắng tạo thử thách. Từ tee box 1, golfer có thể ngắm toàn cảnh Lang Biang; fairway 9 ôm quanh hồ phẳng lặng giữa rừng.

3. Chất lượng sân cỏ & Bảo dưỡng  
Greens sử dụng Bentgrass, fairway phối hợp Paspalum và Zoysia, bảo dưỡng nghiêm ngặt theo tiêu chuẩn USGA. Hệ thống tưới tự động và đội ngũ greenskeeper chuyên nghiệp làm việc 24/7 đảm bảo mặt sân luôn mịn màng.

4. Cơ sở vật chất & Dịch vụ  
Clubhouse thiết kế hiện đại với locker cao cấp, pro-shop đa dạng, nhà hàng Á-Âu và lounge nhìn ra fairway. Dịch vụ caddie chuyên nghiệp, huấn luyện viên PGA và phòng Golf Simulator phục vụ mọi nhu cầu.

5. Trải nghiệm & Gợi ý  
Thời điểm lý tưởng là buổi sáng khi sương mù còn giăng lối giữa thông, hoặc chiều hoàng hôn nhuộm hồng đỉnh núi. Sau vòng golf, bạn có thể thưởng thức trà ở lounge hoặc tham quan đồi chè Cầu Đất.

6. Hướng dẫn đặt chỗ  
Liên hệ hotline (0263) 3 999 1200 hoặc đặt trực tuyến qua TEEtimeVN để nhận ưu đãi và hỗ trợ 24/7.'
WHERE course_id = 17 AND lang = 'vi';

UPDATE golf_course_i18n
SET overview = 'Da Lat 1200 Golf Club is perched at 1,200 m above sea level on the Lang Biang plateau in Lac Duong district, Lam Dong province, about 25 km from downtown Da Lat. Designed by IMG London and opened in 2018, this par-72, 18-hole layout stretches 7,085 yards through pine forests, mountain lakes, and natural fairways.

1. Overview & History  
Conceived to harness the highland’s year-round cool climate and scenic beauty, Da Lat 1200 has hosted regional amateur tournaments and draws international players.

2. Course Design & Scenery  
Fairways weave along pine-forested ridges, with small lakes and white bunkers adding strategic interest. From tee box 1 you can survey the Lang Biang peak; fairway 9 hugs a tranquil forest lake.

3. Turf Quality & Maintenance  
Bentgrass greens and Paspalum-Zoysia fairways are maintained to USGA standards. Automated irrigation and a dedicated 24/7 greenskeeping team ensure pristine playing surfaces.

4. Facilities & Services  
The modern clubhouse features premium lockers, a well-stocked pro shop, an Asian-Western restaurant, and a fairway-view lounge. Professional caddies, PGA coaches, and a Golf Simulator room complete the offering.

5. Experience & Tips  
Early-morning tee times reveal mist drifting through the pines; late-afternoon rounds showcase sunset hues on mountain peaks. After your round, enjoy tea in the lounge or visit the nearby Cau Dat tea terraces.

6. Booking  
Call (0263) 3 999 1200 or book online via TEEtimeVN for the best rates and 24/7 assistance.'
WHERE course_id = 17 AND lang = 'en';

UPDATE golf_course_i18n
SET overview = '达拉特1200高尔夫俱乐部位于林同省拉克占县Lang Biang高原，海拔约1,200米，距离大叻市中心25公里。球场由IMG London设计，2018年开业，18洞标准杆72杆，全长7,085码，球道穿越松林、山间湖泊和自然草坪。

1. 概览与历史  
该球场旨在利用高原全年凉爽气候和优美景观，已举办多项区域业余赛事并吸引国际球手。

2. 设计与景观  
球道沿松林山脊蜿蜒，点缀小型湖泊和白沙沙坑。1号发球台可眺望Lang Biang山峰；9号球道环绕宁静的森林湖泊。

3. 草坪品质与维护  
果岭采用Bentgrass，球道为Paspalum-Zoysia混铺，按USGA标准维护。自动灌溉系统和全天候绿地团队确保球场状态一流。

4. 设施与服务  
现代会所配备高级储物柜、专业球具店、中西餐厅和球道景休息室。专业球童、PGA教练及高尔夫模拟室提供全方位服务。

5. 体验与建议  
清晨雾气在松林中飘逸；傍晚球局可欣赏山峰落日。赛后可在休息室品茗或参观附近的茶园。

6. 预订方式  
请致电 (0263) 3 999 1200 或通过 TEEtimeVN 在线预订，享受最佳价格及全天候支持。'
WHERE course_id = 17 AND lang = 'zh-CN';

UPDATE golf_course_i18n
SET overview = '達拉特1200高爾夫俱樂部位於寧王省拉克占縣Lang Biang高原，海拔約1,200米，距大叻市中心25公里。球場由IMG London設計，2018年開放，18洞標準桿72桿，全長7,085碼，球道穿越松林、山間湖泊與自然草坪。

1. 總覽與歷史  
本球場旨在利用高原四季涼爽氣候與優美景觀，已承辦多項區域業餘賽事並吸引國際球手。

2. 設計與景觀  
球道沿松林山脊蜿蜒，點綴小型湖泊和白沙沙坑。1號發球台可眺望Lang Biang山峰；9號球道環繞寧靜的森林湖泊。

3. 草坪品質與維護  
果嶺採用Bentgrass，球道為Paspalum-Zoysia混鋪，依USGA標準維護。自動灌溉系統和全天候綠地團隊確保球場狀態一流。

4. 設施與服務  
現代會所配備高級儲物櫃、專業球具店、中西餐廳和球道景休息室。專業球童、PGA教練及高爾夫模擬室提供全方位服務。

5. 體驗與建議  
清晨霧氣在松林中飄逸；傍晚球局可欣賞山峰落日。賽後可在休息室品茗或參觀附近茶園。

6. 預訂方式  
請致電 (0263) 3 999 1200 或透過 TEEtimeVN 在線預訂，享受最佳價格及全天候支持。'
WHERE course_id = 17 AND lang = 'zh-TW';

UPDATE golf_course_i18n
SET overview = '달랏1200 골프 클럽(Da Lat 1200 Golf Club)은 람동성 락장군 Lang Biang 고원 해발 약 1,200m 지점에 위치하며, 달랏 시내에서 약 25km 떨어져 있습니다. IMG 런던이 설계하고 2018년 개장한 이 파72 18홀 코스는 7,085야드에 달하며, 솔숲, 산간 호수, 자연 페어웨이를 따라 펼쳐진 레이아웃이 특징입니다.

1. 개요 및 역사  
고원지대의 연중 온화한 기후와 수려한 풍광을 활용하기 위해 조성된 본 코스는 지역 아마추어 대회를 개최하며 국제 골퍼들의 사랑을 받고 있습니다.

2. 코스 디자인 & 경관  
페어웨이는 솔숲 능선을 따라 이어지며, 작은 호수와 화이트 벙커가 전략적 장애물로 배치됩니다. 1번 티에서는 Lang Biang 봉우리를 조망할 수 있고, 9번 페어웨이는 고즈넉한 숲속 호수를 끼고 이어집니다.

3. 잔디 품질 및 유지관리  
Bentgrass 그린과 Paspalum-Zoysia 페어웨이는 USGA 기준에 따라 관리되며, 자동 관개 시스템과 24시간 그린키퍼 팀이 최고 상태를 유지합니다.

4. 시설 및 서비스  
모던 클럽하우스에는 프리미엄 라커, 프로샵, 아시안-웨스턴 레스토랑, 페어웨이 뷰 라운지 등이 갖춰져 있습니다. 전문 캐디와 PGA 코치, 골프 시뮬레이터가 연습과 라운드를 지원합니다.

5. 경험 및 팁  
이른 아침, 안개 낀 솔숲 사이에서 플레이를, 저녁에는 Lang Biang 맞은편 산봉우리에 물드는 노을 라운드를 추천합니다. 라운드 후 라운지에서 차를 즐기거나 인근 찻밭을 둘러보세요.

6. 예약 안내  
티타임 예약은 (0263) 3 999 1200으로 전화하거나 TEEtimeVN 웹사이트에서 온라인 예약을 이용하세요. 24/7 고객 지원팀이 최적의 일정을 도와드립니다.'
WHERE course_id = 17 AND lang = 'ko';

UPDATE golf_course_i18n
SET overview = 'ダラット1200ゴルフクラブ(Da Lat 1200 Golf Club)は、ランビアン高原（標高約1,200m）のラームドン省ラックザン県に位置し、ダラット市中心部から約25kmです。IMGロンドンが設計し、2018年にオープンしたこのパー72・18ホールコースは、全長7,085ヤードに及び、松林、山間湖、自然のフェアウェイが広がる設計が魅力です。

1. 概要と歴史  
高原地帯の年間を通じた涼しい気候と絶景を生かすために誕生した本コースは、地域のアマチュア大会を開催し、国際的なゴルファーの人気を集めています。

2. コースデザイン＆景観  
フェアウェイは松林の尾根に沿って描かれ、小さな湖とホワイトバンカーが戦略的に配置されています。1番ティーからはLang Biang山頂を望め、9番フェアウェイは静寂な森の湖に沿って続きます。

3. 芝の品質＆メンテナンス  
ベントグラスのグリーンとパスパルム-ゾイシアのフェアウェイはUSGA基準で管理され、自動灌漑システムと24時間体制のグリーンキーパーチームが最高のコース状態を維持します。

4. 施設＆サービス  
モダンなクラブハウスにはプレミアムロッカー、プロショップ、アジアン・ウェスタンレストラン、フェアウェイビューラウンジが整備されています。専属キャディとPGAコーチ、ゴルフシミュレーターが練習とラウンドをサポートします。

5. 体験＆アドバイス  
早朝は霧に包まれた松林でプレイを楽しみ、夕方はLang Biang山の夕焼けを背景にラウンドするのがおすすめです。ラウンド後はラウンジでお茶を楽しんだり、近隣の茶畑を散策したりしてみてください。

6. 予約方法  
ティータイムの予約は(0263) 3 999 1200までお電話いただくか、TEEtimeVNウェブサイトからオンライン予約をご利用ください。24時間対応のカスタマーサポートが最適なプランをご案内します。'
WHERE course_id = 17 AND lang = 'ja';

"""

# Thực thi nhiều lệnh cùng lúc
cur.executescript(sql)

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("Đã cập nhật xong overview")
