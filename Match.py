from Score import Score
import random

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
