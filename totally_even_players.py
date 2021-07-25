#%% Imports
from Match import Match
import pandas as pd

#%% Simulate matches
results = {}
for i in range(100000):
    match = Match(1)
    winner_index = match.play_full_match()

    if winner_index == 1:
        match_score = []
        for match_set in match.score.games_for_set:
            match_score.append([match_set[1], match_set[0]])
    else:
        match_score = match.score.games_for_set
    flat_match_score = tuple([item for sublist in match_score for item in sublist])
    if flat_match_score in results:
        results[flat_match_score] = results.get(flat_match_score) + 1
    else:
        results[flat_match_score] = 1

#%% Create dataframe
df = pd.DataFrame(list(zip(results.keys(), results.values())), columns =['Result', 'Quantity'])