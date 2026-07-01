# NWSL-Player-Contribution-Dashboard

This project is an interactive data dashboard built with Python, SQL, Pandas, Altair, and Streamlit. It analyzes NWSL player performances using different features.

## Project Overview

As it is the summer of the 2026 World Cup it is impossible to ignore the firey competition. That energy inspired me to combine my fresh SQL knowledge with something happening in the real world. This dashboard analyzes NWSL player performance using a custom weighted contribution score. It includes multiple leaderboard pages, a player search feature, and a player comparison tool. The app is built with Streamlit for the UI and SQLite for the database backend.

## Tech Stack

- Python
- Streamlit
- Pandas
- Altair
- SQLite
- SQL

## Contribution Score Formula

The dashboard uses a custom weighted formula to measure total player contribution:

goals * 5
assists * 4
on_target_scoring_attempts * 1.5
tackles * 1.2 
accurate_pass_percentage * 0.1 
-(turnovers * 0.5)

This score is a reflection of a player's overall impact!

## Features
- Top Contributors Leaderboard
- Top Scorers
- Top Assisters
- Top Tacklers
- Top Passers
- Lowest Turnovers
- Player Search with full stat profile
- Player Comparison (side‑by‑side analysis)
- Interactive Altair charts
- SQLite database backend (`nwsl.db`)

## Project Structure
app.py                # Streamlit application
nwsl.db               # SQLite database
requirements.txt      # Python dependencies
README.md             # Project documentation


## Purpose
This project is part of my preparation for entering the Computer Science & Engineering along with data analytics program at The Ohio State University. During my internship at BERPL Tech I gained a SQL and Python certification and want to apply my knowledge into a project that refelcted my hobbies. I built it to strengthen my SQL, Python, and data analysis skills while creating a real, meaningful project for my portfolio.
