from Entities import Score

score = Score()

score.games = [5, 5]

for i in range(40):
    score.print_score()
    winner_player_index = int(input('0: Punto jugador 1, 1: Punto jugador 2 -> '))
    score.score_point(winner_player_index)