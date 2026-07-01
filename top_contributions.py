import sqlite3

conn = sqlite3.connect("nwsl.db")
cursor = conn.cursor()

goats = cursor.execute("""
SELECT DISTINCT(conc_player_name), 
(goals * 5) +
(assists * 4) +
(on_target_scoring_attempts * 1.5) +
(tackles * 1.2) +
(accurate_pass_percentage * 0.1) -
(turnovers * 0.5) AS contribution
FROM PlayerStats ORDER BY contribution DESC LIMIT 10;                       
""")

for g in goats:
    print(g)

print()

bests = cursor.execute("""
SELECT DISTINCT(p.player_name), p.team, s.goals, s.assists
FROM Players p JOIN PlayerStats S
ON p.conc_player_name = s.conc_player_name LIMIT 12;                                              
""")

for b in bests:
    print(b)

conn.close()