import json
import os

def load_team_stats(team_name):
    path = os.path.join("data", "roster", f"{team_name.lower()}.json")
    if not os.path.exists(path):
        return {"message": "No stats available"}
    with open(path, 'r') as f:
        return json.load(f)
