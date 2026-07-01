import sqlite3

conn = sqlite3.connect("nwsl.db")
cursor = conn.cursor()

#TOP CONTRIBUTION SCORES WITH TEAM NAMES
scores = cursor.execute("""
SELECT DISTINCT p.player_name, p.team,
        (s.goals * 5 +
        s.assists * 4 +
        s.on_target_scoring_attempts * 1.5 +
        s.tackles * 1.2 +
        s.accurate_pass_percentage * 0.1 -
        s.turnovers * 0.5) AS contribution_score
FROM Players p
JOIN PlayerStats s     
ON p.conc_player_name = s.conc_player_name
ORDER BY contribution_score DESC
LIMIT 15;                                                                                                                                           
""")

for s in scores:
    print(s)
#py z_final.py