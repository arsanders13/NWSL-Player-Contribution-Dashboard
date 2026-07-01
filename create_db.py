import sqlite3
#create a connection to the database
conn = sqlite3.connect("nwsl.db")
cursor = conn.cursor()
#read my SQL file
with open("sql/create_tables.sql", "r") as f:
    sql_script = f.read()
#execute the SQL commands
cursor.executescript(sql_script)

conn.commit()
conn.close()

print("database and tables are madeeeee")