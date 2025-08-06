import streamlit as st
from models.predictor import predict_play
from utils.data_loader import load_team_stats

st.set_page_config(page_title="NFL Play Predictor", layout="centered")
st.title("🏈 NFL Play Predictor")

st.markdown("""
This tool predicts the optimal offensive play (run, pass, punt, field goal) based on in-game NFL scenario data.
Select the scenario below:
""")

nfl_teams = sorted([
    "49ers", "Bears", "Bengals", "Bills", "Broncos", "Browns", "Buccaneers",
    "Cardinals", "Chargers", "Chiefs", "Colts", "Commanders", "Cowboys",
    "Dolphins", "Eagles", "Falcons", "Giants", "Jaguars", "Jets", "Lions",
    "Packers", "Panthers", "Patriots", "Raiders", "Rams", "Ravens",
    "Saints", "Seahawks", "Steelers", "Texans", "Titans", "Vikings"
])

team = st.selectbox("Select Team", nfl_teams)
down = st.selectbox("Down", [1, 2, 3, 4])
distance = st.slider("Yards to First Down", 1, 20, 10)
yard_line = st.slider("Yard Line (1 = own end zone, 99 = opponent's)", 1, 99, 50)
quarter = st.selectbox("Quarter", [1, 2, 3, 4])
time_remaining = st.number_input("Time Remaining in Quarter (sec)", min_value=0, max_value=900, value=300)
score_diff = st.number_input("Score Differential (team - opponent)", value=0)

if st.button("Predict Best Play"):
    scenario = {
        "team": team,
        "down": down,
        "distance": distance,
        "yard_line": yard_line,
        "quarter": quarter,
        "time_remaining": time_remaining,
        "score_diff": score_diff
    }

    team_stats = load_team_stats(team)
    prediction = predict_play(scenario)

    st.subheader("Prediction Result")
    st.success(f"{team} should: **{prediction.upper()}**")

    st.subheader("Team Analytics")
    st.json(team_stats)

