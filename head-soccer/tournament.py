from game_state import GameState


class Tournament:
    def __init__(self):
        self.current_round = 0
        self.rounds = ["Quarterfinals", "Semi Finals", "Finals"]
        self.wins = 0
        self.losses = 0
        self.completed = False
        self.is_champion = False

    def reset(self):
        self.current_round = 0
        self.wins = 0
        self.losses = 0
        self.completed = False
        self.is_champion = False

    def advance_round(self):
        self.current_round += 1
        if self.current_round >= len(self.rounds):
            self.completed = True

    def record_result(self, winner):
        if winner == "player":
            self.wins += 1
            if self.current_round == len(self.rounds) - 1:
                self.is_champion = True
                return GameState.CHAMPION
            self.advance_round()
            return GameState.TOURNAMENT_PROGRESS
        else:
            self.losses += 1
            return GameState.MAIN_MENU

    def get_current_round(self):
        if self.current_round < len(self.rounds):
            return self.rounds[self.current_round]
        return "Completed"

    def get_progress(self):
        return f"Round {self.current_round + 1}/3 - Wins: {self.wins} - Losses: {self.losses}"
