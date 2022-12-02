points = {'C A': 6 + 1,
          'B B': 3 + 2,
          'B A': 0 + 1,
          'A C': 0 + 3,
          'C B': 0 + 2,
          'A B': 6 + 2,
          'B C': 6 + 3,
          'A A': 3 + 1,
          'C C': 3 + 3}

with open("data.txt") as file:
    data = file.read()
    data = data.replace("X", "A").replace("Y", "B").replace("Z", "C")
    data = data.splitlines()


def score(strategy_guide, score_guide):
    final_score = 0

    for game_setting, points_for_setting in score_guide.items():
        occurrences = strategy_guide.count(game_setting)
        final_score += occurrences * points_for_setting

    return final_score


print(score(data, points))
