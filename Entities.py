import random

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

class Match():

    def __init__(self, sets_to_win, player_one_win_point_probability_function=None):
        self.player_one_win_point_probability_function = player_one_win_point_probability_function
        self.sets_to_win = sets_to_win
        self.score = Score()
        self.match_is_over = False
        self.player_serving = random.choice([0, 1])

    def play_full_match(self):
        while not self.match_is_over:
            winner_player_index = self.play_point()
            self.score_point(winner_player_index)
            if self.have_to_change_server():
                self.player_serving = (self.player_serving + 1) % 2
            self.match_is_over = self.is_match_over()
        return self.winner_player_index()

    def winner_player_index(self):
        if self.player_one_win_point_probability_function == None:
            return 0 if self.score.sets[0] > self.score.sets[1] else 1
        return self.player_one_win_point_probability_function(self.score, self.player_serving == 0)

    def have_to_change_server(self):
        return self.score.is_new_game() or (self.score.playing_tiebreak and (self.score.points[0] + self.score.points[1]) % 2 == 1)

    def play_point(self):
        return random.choice([0, 1])

    def score_point(self, winner_player_index):
        self.score.score_point(winner_player_index)

    def is_match_over(self):
        return self.score.sets[0] == self.sets_to_win or self.score.sets[1] == self.sets_to_win
