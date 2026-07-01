
import sqlite3

conn = sqlite3.connect("nwsl.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM PlayerStats LIMIT 10")
rows = cursor.fetchall()

for r in rows:
    print(r)

conn.close()
