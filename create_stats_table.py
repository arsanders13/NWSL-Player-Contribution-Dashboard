import sqlite3
conn = sqlite3.connect("nwsl.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS PlayerStats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conc_player_name TEXT,
    games_played INTEGER,
    games_started INTEGER,
    minutes_played INTEGER,
    goals INTEGER,
    assists INTEGER,
    total_scoring_attempts INTEGER,
    on_target_scoring_attempts INTEGER,
    tackles INTEGER,
    fouls_committed INTEGER,
    fouls_suffered INTEGER,
    yellow_cards INTEGER,
    red_cards INTEGER,
    accurate_pass_percentage REAL,
    accurate_passes INTEGER,
    total_passes INTEGER,
    turnovers INTEGER,
    goals_avg_over_90_mins REAL,
    assists_avg_over_90_mins REAL
);
""")

conn.commit()
conn.close()