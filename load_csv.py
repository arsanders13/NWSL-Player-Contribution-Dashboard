import sqlite3
import csv
conn = sqlite3.connect("nwsl.db")
cursor = conn.cursor()
csv_path = "data/2024_nwsl_0525.csv"

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        cursor.execute(
            "INSERT INTO Players (player_name, conc_player_name, team, position)"
            " VALUES(?,?,?,?)",
            (
                row["player_name"],
                row["conc_player_name"],
                row["\ufeffteam"],
                row["position"]
            )

        )
conn.commit()
conn.close()