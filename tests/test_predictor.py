def test_predict_play():
    from models.predictor import predict_play
    scenario = {
        "team": "Eagles",
        "down": 1,
        "distance": 10,
        "yard_line": 25,
        "quarter": 1,
        "time_remaining": 900,
        "score_diff": 0
    }
    assert predict_play(scenario).startswith("pass")
