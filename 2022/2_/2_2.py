points = {'C Z': 1 + 6,
          'A Y': 1 + 3,
          'B Y': 2 + 3,
          'B Z': 3 + 6,
          'C X': 2 + 0,
          'B X': 1 + 0,
          'C Y': 3 + 3,
          'A X': 3 + 0,
          'A Z': 2 + 6}


with open("data.txt") as file:
    data = file.read()
    data = data.splitlines()


def score(strategy_guide, score_guide):
    final_score = 0

    for game_setting, points_for_setting in score_guide.items():
        occurrences = strategy_guide.count(game_setting)
        final_score += occurrences * points_for_setting

    return final_score


print(score(data, points))
