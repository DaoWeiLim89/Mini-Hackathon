import pygame
import sys
from constants import *
from game_state import GameState
from player import Player
from cpu import CPU
from ball import Ball
from game_manager import GameManager
from mode_select import ModeSelect
from tournament import Tournament
from ui import UI


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Head Soccer")
        self.clock = pygame.time.Clock()
        self.state = GameState.MODE_SELECT

        self.mode_select = ModeSelect()
        self.tournament = Tournament()
        self.game_manager = GameManager()

        self.player = Player(120, GROUND_Y - PLAYER_HEIGHT, RED)
        self.cpu = CPU(CENTER_X + 50, GROUND_Y - PLAYER_HEIGHT)
        self.ball = Ball()

        self.is_tournament = False
        self.scoring_timer = 0

    def reset_match(self):
        self.game_manager.reset_match()
        self.ball.drop()
        self.player.x = 120
        self.player.y = GROUND_Y - PLAYER_HEIGHT
        self.player.vel_x = 0
        self.player.vel_y = 0
        self.cpu.x = 550
        self.cpu.y = GROUND_Y - PLAYER_HEIGHT
        self.cpu.vel_x = 0
        self.cpu.vel_y = 0
        self.ball.drop()
        self.game_manager.match_started = True

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == KEY_ESC:
                        if self.state in [GameState.PLAYING, GameState.OVERTIME]:
                            self.state = GameState.MODE_SELECT
                            self.tournament.reset()

                    if self.state == GameState.MODE_SELECT:
                        mode = self.mode_select.handle_input(event)
                        if mode == "Quick Game":
                            self.is_tournament = False
                            self.reset_match()
                            self.state = GameState.PLAYING
                        elif mode == "Tournament":
                            self.is_tournament = True
                            self.tournament.reset()
                            self.reset_match()
                            self.state = GameState.TOURNAMENT_PROGRESS

                    elif self.state == GameState.TOURNAMENT_PROGRESS:
                        if event.key == KEY_ENTER:
                            self.reset_match()
                            self.state = GameState.PLAYING

                    elif self.state == GameState.GAME_OVER:
                        if event.key == KEY_ENTER:
                            winner = self.game_manager.get_winner()
                            if self.is_tournament:
                                next_state = self.tournament.record_result(winner)
                                self.state = next_state
                            else:
                                self.state = GameState.MODE_SELECT

                    elif self.state == GameState.CHAMPION:
                        if event.key == KEY_ENTER:
                            self.state = GameState.MODE_SELECT

            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def update(self):
        if self.state == GameState.PLAYING:
            self.update_playing()
        elif self.state == GameState.OVERTIME:
            self.update_overtime()
        elif self.state == GameState.SCORING:
            self.update_scoring()

    def update_playing(self):
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)
        self.cpu.update_ai(self.ball.x, self.ball.vel_x, self.ball.y)

        self.player.update()
        self.cpu.update()
        self.ball.update()

        self.ball.check_collision_with_player(self.player)
        self.ball.check_collision_with_player(self.cpu)

        goal = self.ball.check_goal()
        if goal:
            self.game_manager.add_goal("player" if goal == "right" else "cpu")
            self.state = GameState.SCORING
            self.scoring_timer = 60

        self.game_manager.update_timer()

        if self.game_manager.check_game_over():
            winner = self.game_manager.get_winner()
            self.state = GameState.GAME_OVER
        elif self.game_manager.check_tie():
            self.game_manager.start_overtime()
            self.state = GameState.OVERTIME

    def update_overtime(self):
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)
        self.cpu.update_ai(self.ball.x, self.ball.vel_x, self.ball.y)

        self.player.update()
        self.cpu.update()
        self.ball.update()

        self.ball.check_collision_with_player(self.player)
        self.ball.check_collision_with_player(self.cpu)

        goal = self.ball.check_goal()
        if goal:
            self.game_manager.add_goal("player" if goal == "right" else "cpu")
            winner = self.game_manager.get_winner()
            self.state = GameState.GAME_OVER

    def update_scoring(self):
        if self.scoring_timer > 0:
            self.scoring_timer -= 1
            if self.scoring_timer <= 0:
                self.player.x = 120
                self.player.y = GROUND_Y - PLAYER_HEIGHT
                self.player.vel_x = 0
                self.player.vel_y = 0
                self.cpu.x = CENTER_X + 50
                self.cpu.y = GROUND_Y - PLAYER_HEIGHT
                self.cpu.vel_x = 0
                self.cpu.vel_y = 0
                self.ball.drop()
                if self.game_manager.check_game_over():
                    winner = self.game_manager.get_winner()
                    self.state = GameState.GAME_OVER
                elif self.game_manager.is_overtime:
                    pass
                else:
                    self.state = GameState.PLAYING

    def draw(self):
        if self.state == GameState.MODE_SELECT:
            self.mode_select.draw(self.screen)
        elif self.state == GameState.TOURNAMENT_PROGRESS:
            UI.draw_field(self.screen)
            UI.draw_tournament_progress(self.screen, self.tournament)
        elif self.state in [GameState.PLAYING, GameState.OVERTIME, GameState.SCORING]:
            UI.draw_field(self.screen)
            self.player.draw(self.screen)
            self.cpu.draw(self.screen)
            self.ball.draw(self.screen)
            UI.draw_score(
                self.screen, self.game_manager.player_score, self.game_manager.cpu_score
            )
            UI.draw_timer(
                self.screen, self.game_manager.time_left, self.game_manager.is_overtime
            )
        elif self.state == GameState.GAME_OVER:
            UI.draw_field(self.screen)
            UI.draw_score(
                self.screen, self.game_manager.player_score, self.game_manager.cpu_score
            )
            winner = self.game_manager.get_winner()
            UI.draw_game_over(self.screen, winner)
        elif self.state == GameState.CHAMPION:
            UI.draw_field(self.screen)
            UI.draw_champion(self.screen)


if __name__ == "__main__":
    game = Game()
    game.run()
