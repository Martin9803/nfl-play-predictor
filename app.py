import streamlit as st
from models.predictor import predict_play
from utils.data_loader import load_team_stats, load_team_rank

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
gameclock = st.text_input("Time Remaining in Quarter (mm:ss)", value="5:00")
score_diff = st.text_input("Score Differential (your_team - opponent_team)", value="0")

# Convert mm:ss to total seconds
try:
    minutes, seconds = map(int, gameclock.strip().split(":"))
    time_remaining = minutes * 60 + seconds
except:
    time_remaining = 0

# Convert score differential input to integer
try:
    score_diff_int = int(score_diff.strip())
except:
    score_diff_int = 0

if st.button("Predict Best Play"):
    scenario = {
        "team": team,
        "down": down,
        "distance": distance,
        "yard_line": yard_line,
        "quarter": quarter,
        "time_remaining": time_remaining,
        "score_diff": score_diff_int
    }

    team_stats = load_team_stats(team)
    rank_info = load_team_rank(team)
    prediction = predict_play(scenario)

    st.subheader("Prediction Result")
    st.success(f"{team} should: **{prediction.upper()}**")

    if rank_info:
        pass_rank = rank_info.get("pass_rank")
        rush_rank = rank_info.get("rush_rank")
        st.caption(f"📊 Based on team rankings — Pass Rank: #{pass_rank}, Rush Rank: #{rush_rank}")
        if prediction.startswith("run"):
            st.info("Rushing strategy is favored due to strong rushing rank.")
        elif prediction.startswith("pass"):
            st.info("Passing strategy is favored due to stronger pass rank.")
        elif prediction == "field goal":
            st.info("Field goal likely due to short 4th down near FG range.")
        elif prediction == "punt":
            st.info("Punt suggested due to 4th and long situation.")

    st.subheader("Team Analytics")
    st.json({"stats": team_stats, "rankings": rank_info})







