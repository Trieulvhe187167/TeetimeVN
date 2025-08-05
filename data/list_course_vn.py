import sqlite3

DB_PATH = 'teetimevn_dev.db'


def list_courses_vietnamese():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    rows = cursor.execute("""
        SELECT course_id, name FROM golf_course_i18n
        WHERE lang='zh-CN'
        ORDER BY course_id
    """).fetchall()
    conn.close()

    for course_id, name in rows:
        print(f"{course_id:>3} - {name}")

if __name__ == "__main__":
    list_courses_vietnamese()
