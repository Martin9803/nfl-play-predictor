if __name__ == "__main__":
    from scenarios.scenario_input import get_game_scenario
    from models.predictor import predict_play

    scenario = get_game_scenario()
    decision = predict_play(scenario)
    print("Predicted Offensive Play:", decision)

