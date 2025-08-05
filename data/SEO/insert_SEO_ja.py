import sqlite3
from pathlib import Path

# データベースへのパス
DB_PATH = Path(__file__).resolve().parent / 'teetimevn_dev.db'

# ゴルフ場一覧（ID、日本語名）
golf_courses = [
    (1, "BRGキングスアイランドゴルフリゾート"),
    (2, "チーリンスタ―ゴルフ＆カントリークラブ"),
    (3, "ヘロンレイクゴルフ場"),
    (4, "ロンビエンゴルフクラブ"),
    (5, "スカイレイクゴルフリゾート"),
    (6, "FLCハロン湾ゴルフクラブ"),
    (7, "トゥアンチャウゴルフリゾート"),
    (8, "バントリゴルフクラブ"),
    (9, "タムダオゴルフリゾート"),
    (10, "モンゴメリーリンクスベトナム"),
    (11, "ラグーナランコーゴルフクラブ"),
    (12, "バーナーヒルズGCライトコース"),
    (13, "ベトナムゴルフ＆カントリークラブ"),
    (14, "ツインダブズゴルフクラブ"),
    (15, "サンクチュアリホートラムゴルフ"),
    (16, "ビンパールゴルフフーコック"),
    (17, "ダラット1200ゴルフクラブ"),
    (44, "チャンアンゴルフ＆カントリークラブ"),
    (45, "ロイヤルゴルフコース"),
    (46, "ドラゴンゴルフリンクス"),
    (47, "ハイフォンビンパールゴルフ"),
    (48, "ハイフォンソノフェリーチェCC"),
    (49, "ハイフォンルビーツリーゴルフリゾート"),
    (50, "モンカイ国際ゴルフクラブ"),
    (51, "アンバーヒルズゴルフ＆リゾート"),
    (52, "ストーンハイランドゴルフリゾート"),
    (53, "イエンバイスターゴルフリゾート"),
    (54, "サパグランドゴルフコース"),
    (55, "コーンヒルゴルフ＆リゾート"),
    (56, "ヴァンランエンパイアゴルフクラブ"),
]

def generate_seo_content(name):
    seo_title = f"{name}のティータイム予約 | TEEtimeVN"
    seo_description = f"{name}はベトナムのトップクラスのゴルフ場。美しいデザインと高品質なサービス。TEEtimeVNで簡単に予約可能。"
    meta_keywords = f"{name}, ベトナムゴルフ場, ゴルフ予約, ティータイム予約, ゴルフリゾート"
    fee_note = "料金にはキャディーと電動カートが含まれます。祝日は対象外。"
    tips_note = "快適な気候を楽しむために、早朝のティータイム予約をおすすめします。"
    best_season = "10月〜4月（乾季）"

    return {
        "seo_title": seo_title,
        "seo_description": seo_description,
        "meta_keywords": meta_keywords,
        "fee_note": fee_note,
        "tips_note": tips_note,
        "best_season": best_season
    }

def insert_seo():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    lang = 'ja'

    for course_id, name in golf_courses:
        content = generate_seo_content(name)

        cursor.execute("SELECT id FROM golf_course_i18n WHERE course_id=? AND lang=?", (course_id, lang))
        exists = cursor.fetchone()

        if exists:
            cursor.execute("""
                UPDATE golf_course_i18n
                SET seo_title=?, seo_description=?, meta_keywords=?,
                    fee_note=?, tips_note=?, best_season=?
                WHERE course_id=? AND lang=?
            """, (
                content["seo_title"],
                content["seo_description"],
                content["meta_keywords"],
                content["fee_note"],
                content["tips_note"],
                content["best_season"],
                course_id, lang
            ))
            print(f"✅ SEOを更新しました: {name}")
        else:
            cursor.execute("""
                INSERT INTO golf_course_i18n (
                    course_id, lang, name,
                    seo_title, seo_description, meta_keywords,
                    fee_note, tips_note, best_season
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                course_id, lang, name,
                content["seo_title"],
                content["seo_description"],
                content["meta_keywords"],
                content["fee_note"],
                content["tips_note"],
                content["best_season"]
            ))
            print(f"➕ SEOを追加しました: {name}")

    conn.commit()
    conn.close()
    print("🎉 日本語SEOの登録・更新が完了しました！")

if __name__ == "__main__":
    insert_seo()
