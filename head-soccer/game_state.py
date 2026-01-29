from enum import Enum


class GameState(Enum):
    MODE_SELECT = 0
    MAIN_MENU = 1
    PLAYING = 2
    SCORING = 3
    OVERTIME = 4
    GAME_OVER = 5
    TOURNAMENT_MENU = 6
    TOURNAMENT_PROGRESS = 7
    CHAMPION = 8
