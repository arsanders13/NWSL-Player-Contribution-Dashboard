import streamlit as st
import sqlite3
import pandas as pd
import altair as alt

st.title("NWSL Player Contribution Dashboard")

#sidebar navigation
page = st.sidebar.selectbox(
    "Choose a page",
    ["Top Contributors", "Top Scorers", "Top Assisters", "Top Tacklers", "Best Passers", "Lowest Turnovers", "Player Search", "Compare Players" ]
)

#connect to the database
conn = sqlite3.connect("nwsl.db")


#query contributors
query = """
SELECT DISTINCT
p.player_name,
p.team,
    (
        s.goals * 5 +
        s.assists * 4 +
        s.on_target_scoring_attempts * 1.5 +
        s.tackles * 1.2 +
        s.accurate_pass_percentage * 0.1 -
        s.turnovers * 0.5
    ) AS contribution_score
FROM Players p
JOIN PlayerStats s
    ON p.conc_player_name = s.conc_player_name
ORDER BY contribution_score DESC
LIMIT 15;
"""
#query for scorers
query_scorers = """
SELECT DISTINCT p.player_name, p.team, s.goals
FROM Players p 
JOIN PlayerStats s 
ON p.conc_player_name = s.conc_player_name 
ORDER BY s.goals DESC LIMIT 15;
"""
#query for assists
query_assists = """
SELECT DISTINCT p.player_name, p.team, s.assists
FROM Players p JOIN PlayerStats s
ON p.conc_player_name = s.conc_player_name
ORDER BY s.assists DESC LIMIT 15;
"""
#query for tacklers
query_tacklers = """
SELECT DISTINCT p.player_name, p.team, s.tackles
FROM Players p JOIN PlayerStats s
ON p.conc_player_name = s.conc_player_name
ORDER BY s.tackles DESC LIMIT 15;
"""

#query for pass acc
query_pass = """
SELECT DISTINCT p.player_name, p.team, s.accurate_pass_percentage
FROM Players p JOIN PlayerStats s
ON p.conc_player_name = s.conc_player_name
ORDER BY s.accurate_pass_percentage DESC LIMIT 15;
"""

#query for turnovers
query_turnovers="""
SELECT DISTINCT p.player_name, p.team, s.turnovers
FROM Players p JOIN PlayerStats s
ON p.conc_player_name = s.conc_player_name
ORDER BY s.turnovers ASC LIMIT 30;
"""

#query player search
query_search ="""
SELECT DISTINCT
    p.player_name,
    p.team,
    s.goals,
    s.assists,
    s.on_target_scoring_attempts,
    s.tackles,
    s.accurate_pass_percentage,
    s.turnovers,
    (
        s.goals * 5 +
        s.assists * 4 +
        s.on_target_scoring_attempts * 1.5 +
        s.tackles * 1.2 +
        s.accurate_pass_percentage * 0.1 -
        s.turnovers * 0.5
    ) AS contribution_score
FROM Players p
JOIN PlayerStats s
    ON p.conc_player_name = s.conc_player_name
WHERE p.player_name LIKE ?
"""
query_compare= """
SELECT player_name FROM Players ORDER BY player_name;
"""
df = pd.read_sql_query(query, conn)
df.index = df.index + 1

df_scorers = pd.read_sql_query(query_scorers, conn)
df_scorers.index = df_scorers.index+1

df_assister = pd.read_sql_query(query_assists, conn)
df_assister.index= df_assister.index +1

df_tackler = pd.read_sql_query(query_tacklers, conn)
df_tackler.index= df_tackler.index +1

df_pass = pd.read_sql_query(query_pass, conn)
df_pass['accurate_pass_percentage'] = pd.to_numeric(df_pass['accurate_pass_percentage'], errors='coerce')
df_pass.index= df_pass.index +1

df_turnovers = pd.read_sql_query(query_turnovers, conn)
df_turnovers.index= df_turnovers.index +1

df_compare = pd.read_sql_query(query_compare, conn)
player_list = df_compare["player_name"].tolist()

#page logic
if page == "Top Contributors":
    st.subheader("Top 15 Contributors")
    st.dataframe(df)
    chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('player_name', sort=None),
    y='contribution_score',
    tooltip=['player_name', 'team', 'contribution_score']
    ).properties(
    width=700,
    height=400,
    title="Contribution Score Bar Chart"
    )
    st.altair_chart(chart, use_container_width=True)

if page == "Top Scorers":
    st.subheader("Top 15 Goal Scorers")
    st.dataframe(df_scorers)
    chart = alt.Chart(df_scorers).mark_bar().encode(
    x=alt.X('player_name', sort=None),
    y='goals',
    tooltip=['player_name', 'team', 'goals']
    ).properties(
    width=700,
    height=400,
    title="Goals Bar Chart"
    )
    st.altair_chart(chart, use_container_width=True)

if page == "Top Assisters":
    st.subheader("Top 15 Assisters")
    st.dataframe(df_assister)
    chart = alt.Chart(df_assister).mark_bar().encode(
    x=alt.X('player_name', sort=None),
    y='assists',
    tooltip=['player_name', 'team', 'assists']
    ).properties(
    width=700,
    height=400,
    title="Assists Bar Chart"
    )
    st.altair_chart(chart, use_container_width=True)

if page == "Top Tacklers":
    st.subheader("Top 15 Tacklers")
    st.dataframe(df_tackler)
    chart = alt.Chart(df_tackler).mark_bar().encode(
    x=alt.X('player_name', sort=None),
    y='tackles',
    tooltip=['player_name', 'team', 'tackles']
    ).properties(
    width=700,
    height=400,
    title="Tackles Bar Chart"
    )
    st.altair_chart(chart, use_container_width=True)

if page == "Best Passers":
    st.subheader("Top 15 Passers")
    st.dataframe(df_pass)
    chart = alt.Chart(df_pass).mark_bar().encode(
    x=alt.X('player_name', sort=None),
    y='accurate_pass_percentage',
    tooltip=['player_name', 'team', 'accurate_pass_percentage']
    ).properties(
    width=700,
    height=400,
    title="Passing Bar Chart"
    )
    st.altair_chart(chart, use_container_width=True)

if page == "Lowest Turnovers":
    st.subheader("Top 30 with the Lowest Turnovers")
    st.dataframe(df_turnovers)
    chart = alt.Chart(df_turnovers).mark_bar().encode(
    x=alt.X('player_name', sort=None),
    y='turnovers',
    tooltip=['player_name', 'team', 'turnovers']
    ).properties(
    width=700,
    height=400,
    title="Turnovers Bar Chart"
    )
    st.altair_chart(chart, use_container_width=True)

if page == "Player Search":
    st.subheader("Search for a Player")
    name = st.text_input("Enter Player Name")
    if name:
        df_search = pd.read_sql_query(query_search, conn, params=[f"%{name}%"])
        if df_search.empty:
            st.write("No player found.")
        else:
            player = df_search.iloc[0]
            st.markdown(f"## {player['player_name']} — {player['team']}")

            st.markdown("### Player Profile")
            st.write({
                "Goals": player["goals"],
                "Assists": player["assists"],
                "On-Target Attempts": player["on_target_scoring_attempts"],
                "Tackles": player["tackles"],
                "Pass Accuracy (%)": player["accurate_pass_percentage"],
                "Turnovers": player["turnovers"],
                "Contribution Score": round(player["contribution_score"], 2)
            })
            st.markdown("### Goals Chart")

            goals_chart = alt.Chart(df_search).mark_bar().encode(
                x=alt.X('player_name', sort=None),
                y='goals',
                tooltip=['player_name','team', 'goals']
            ).properties(
                width=500,
                height=300,
                title="Goals"
            )
            st.markdown("### Assists Chart")

            assists_chart = alt.Chart(df_search).mark_bar().encode(
                x=alt.X('player_name', sort=None),
                y='assists',
                tooltip=['player_name','team', 'assists']
            ).properties(
                width=500,
                height=300,
                title="Assists"
            )

            st.altair_chart(assists_chart, use_container_width=True)
            st.markdown("### Tackles Chart")

            tackles_chart = alt.Chart(df_search).mark_bar().encode(
                x=alt.X('player_name', sort=None),
                y='tackles',
                tooltip=['player_name','team', 'tackles']
            ).properties(
                width=500,
                height=300,
                title="Tackles"
            )

            st.altair_chart(tackles_chart, use_container_width=True)
            st.markdown("### Pass Accuracy Chart")

            pass_chart = alt.Chart(df_search).mark_bar().encode(
                x=alt.X('player_name', sort=None),
                y='accurate_pass_percentage',
                tooltip=['player_name','team', 'accurate_pass_percentage']
            ).properties(
                width=500,
                height=300,
                title="Pass Accuracy (%)"
            )

            st.altair_chart(pass_chart, use_container_width=True)
            st.markdown("### Turnovers Chart")

            turnovers_chart = alt.Chart(df_search).mark_bar().encode(
                x=alt.X('player_name', sort=None),
                y='turnovers',
                tooltip=['player_name','team', 'turnovers']
            ).properties(
                width=500,
                height=300,
                title="Turnovers"
            )

            st.altair_chart(turnovers_chart, use_container_width=True)
if page == "Compare Players":
    st.subheader("Compare Two Players")

    col1, col2 = st.columns(2)

    with col1:
        player_a = st.selectbox("Select Player A", player_list)

    with col2:
        player_b = st.selectbox("Select Player B", player_list)

    if player_a and player_b:
        df_a = pd.read_sql_query(query_search, conn, params=[player_a])
        df_b = pd.read_sql_query(query_search, conn, params=[player_b])

        if df_a.empty or df_b.empty:
            st.write("One or both players not found.")
        else:
            pa = df_a.iloc[0]
            pb = df_b.iloc[0]

            st.markdown("### Player Profiles")

            colA, colB = st.columns(2)

            with colA:
                st.markdown(f"#### {pa['player_name']} — {pa['team']}")
                st.write({
                    "Goals": int(pa["goals"]),
                    "Assists": int(pa["assists"]),
                    "Tackles": int(pa["tackles"]),
                    "Pass Accuracy (%)": float(pa["accurate_pass_percentage"]),
                    "Turnovers": int(pa["turnovers"]),
                    "Contribution Score": int(round(pa["contribution_score"], 2))
                })

            with colB:
                st.markdown(f"#### {pb['player_name']} — {pb['team']}")
                st.write({
                    "Goals": int(pb["goals"]),
                    "Assists": int(pb["assists"]),
                    "Tackles": int(pb["tackles"]),
                    "Pass Accuracy (%)": float(pb["accurate_pass_percentage"]),
                    "Turnovers": int(pb["turnovers"]),
                    "Contribution Score": int(round(pb["contribution_score"], 2))
                })
conn.close()