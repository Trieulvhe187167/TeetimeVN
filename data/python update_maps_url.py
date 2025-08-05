# update_maps_url.py
import sqlite3
from pathlib import Path

DB = Path("data/teetimevn_dev.db")
MAPS_EMBED = ("https://www.google.com/maps/embed?pb="
              "!1m18!1m12!1m3!1d4548.977514045348!"
              "2d108.0466116757594!3d16.01753034081862!"
              "2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!"
              "3m3!1m2!1s0x31421df6e3a730bb:0xd899060c1d60086f!"
              "2sBa%20Na%20Hills%20Golf%20Club!5e1!3m2!1szh-CN!2s!"
              "4v1746714467989!5m2!1szh-CN!2s")

conn = sqlite3.connect(DB)
cur  = conn.cursor()

cur.execute("UPDATE golf_course SET maps_url=? WHERE id=1", (MAPS_EMBED,))
conn.commit()
cur.close()
conn.close()
print("✅ maps_url 已更新")
