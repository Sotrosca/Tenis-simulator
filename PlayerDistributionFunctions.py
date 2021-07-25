# Devuelven 0 si el punto lo gana el jugador A y 1 sino con cierta probabilidad

import numpy as np

def worst_on_decisive_games(score, is_serving):
    if score.games[0] >= 4 and score.games[1] >= 4:
        win_probability = 0.45
    else:
        win_probability = 0.6
    return np.random.binomial(1, 1 - win_probability, size=None)