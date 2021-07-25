class Score():
    def __init__(self):
        self.points = [0, 0]
        self.games = [0, 0]
        self.sets = [0, 0]
        self.playing_tiebreak = False
        self.games_for_set = []

    def score_point(self, winner_player_index):
        self.points[winner_player_index] += 1
        if self.is_game_finished(winner_player_index):
            self.score_game(winner_player_index)
            self.points = [0, 0]

    def score_game(self, winner_player_index):
        self.games[winner_player_index] += 1
        if self.is_set_finished(winner_player_index):
            self.score_set(winner_player_index, self.games)
            self.games = [0, 0]
        self.playing_tiebreak = self.is_tiebreak()

    def score_set(self, winner_player_index, game_result):
        self.sets[winner_player_index] += 1
        self.games_for_set.append(game_result)

    def is_tiebreak(self):
        return self.games[0] == 6 and self.games[0] == self.games[1]

    def is_game_finished(self, winner_player_index):
        if self.playing_tiebreak:
            return self.points[winner_player_index] >= 7 and self.points[winner_player_index] > self.points[(winner_player_index + 1) % 2] + 1
        else:
            return self.points[winner_player_index] >= 4 and self.points[winner_player_index] > self.points[(winner_player_index + 1) % 2] + 1

    def is_set_finished(self, winner_player_index):
        if self.playing_tiebreak:
            return self.games[winner_player_index] == 7
        else:
            return self.games[winner_player_index] >= 6 and self.games[winner_player_index] > self.games[(winner_player_index + 1) % 2] + 1

    def is_new_game(self):
        return self.points[0] == 0 and self.points[1] == 0

    def print_score(self):
        print('Points : ' + str(self.points))
        print('Games : ' + str(self.games))
        print('Sets : ' + str(self.sets))