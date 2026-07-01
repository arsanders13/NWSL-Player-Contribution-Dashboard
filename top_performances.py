import sqlite3

conn = sqlite3.connect("nwsl.db")
cursor = conn.cursor()

#print top 10 scorers-----------------
rows = cursor.execute("""
SELECT conc_player_name, goals FROM PlayerStats ORDER BY goals DESC LIMIT 10;                      
""").fetchall()

for r in rows:
    print(r)

print()

#print top 10 assisters---------------
bars = cursor.execute("""
SELECT DISTINCT(conc_player_name), assists FROM PlayerStats ORDER BY assists DESC LIMIT 10;
""").fetchall()

for b in bars:
    print(b)

print()

#print top 10 tackle performances---------------
tacks = cursor.execute("""
SELECT DISTINCT(conc_player_name), tackles FROM PlayerStats ORDER BY tackles DESC LIMIT 10;                       
""").fetchall()

for t in tacks:
    print(t)

print()

#print top 10 pass accuracy performances------------
passes = cursor.execute("""
SELECT DISTINCT(conc_player_name), accurate_pass_percentage FROM PlayerStats ORDER BY accurate_pass_percentage DESC LIMIT 10;
""").fetchall()

for p in passes:
    print(p)

print()

#print top 10 lowest turnover rate---------
turns = cursor.execute("""
SELECT DISTINCT(conc_player_name), turnovers FROM PlayerStats ORDER BY turnovers LIMIT 10;
""")

for u in turns:
    print(u)

print()

#print top 10 highest contributions per game
highs = cursor.execute("""
SELECT DISTINCT(conc_player_name),(goals_avg_over_90_mins + assists_avg_over_90_mins) AS contribution_over_game FROM PlayerStats ORDER BY (goals_avg_over_90_mins + assists_avg_over_90_mins) DESC LIMIT 10;
""")
 
for h in highs:
    print(h)

conn.close()
#py top_scorers.py