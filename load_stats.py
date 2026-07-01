import sqlite3
import csv

conn = sqlite3.connect("nwsl.db")
cursor = conn.cursor()

csv_path = "data/2024_nwsl_0525.csv"

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute(
            """
            INSERT INTO PlayerStats(
                conc_player_name,
                games_played,
                games_started,
                minutes_played,
                goals,
                assists,
                total_scoring_attempts,
                on_target_scoring_attempts,
                tackles,
                fouls_committed,
                fouls_suffered,
                yellow_cards,
                red_cards,
                accurate_pass_percentage,
                accurate_passes,
                total_passes,
                turnovers,
                goals_avg_over_90_mins,
                assists_avg_over_90_mins
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                row["conc_player_name"],
                row["games_played"],
                row["games_started"],
                row["minutes_played"],
                row["goals"],
                row["assists"],
                row["total_scoring_attempts"],
                row["on_target_scoring_attempts"],
                row["tackles"],
                row["fouls_committed"],
                row["fouls_suffered"],
                row["yellow_cards"],
                row["red_cards"],
                row["accurate_pass_percentage"],
                row["accurate_passes"],
                row["total_passes"],
                row["turnovers"],
                row["goals_avg_over_90_mins"],
                row["assists_avg_over_90_mins"] 
            )
        )
conn.commit()
conn.close()
