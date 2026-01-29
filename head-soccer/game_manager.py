from constants import *


class GameManager:
    def __init__(self):
        self.player_score = 0
        self.cpu_score = 0
        self.time_left = GAME_TIME
        self.is_overtime = False
        self.match_started = False

    def reset_match(self):
        self.player_score = 0
        self.cpu_score = 0
        self.time_left = GAME_TIME
        self.is_overtime = False
        self.match_started = False

    def add_goal(self, scored_by):
        if scored_by == "player":
            self.player_score += 1
        else:
            self.cpu_score += 1

    def update_timer(self):
        if self.match_started and not self.is_overtime:
            self.time_left -= 1 / FPS
            if self.time_left <= 0:
                self.time_left = 0

    def check_game_over(self):
        return (
            self.time_left <= 0
            and not self.is_overtime
            and self.player_score != self.cpu_score
        )

    def check_tie(self):
        return (
            self.time_left <= 0
            and not self.is_overtime
            and self.player_score == self.cpu_score
        )

    def start_overtime(self):
        self.is_overtime = True

    def get_winner(self):
        if self.player_score > self.cpu_score:
            return "player"
        elif self.cpu_score > self.player_score:
            return "cpu"
        return None
