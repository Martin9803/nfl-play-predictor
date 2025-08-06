def predict_play(scenario):
    if scenario['down'] == 4 and scenario['distance'] > 3:
        return "punt"
    if scenario['yard_line'] >= 35 and scenario['down'] == 4 and scenario['distance'] <= 3:
        return "field goal"
    if scenario['distance'] <= 2:
        return "run"
    if scenario['distance'] <= 6:
        return "pass (short)"
    if scenario['distance'] <= 15:
        return "pass (medium)"
    return "pass (deep)"
