import pygame
from constants import *


class UI:
    @staticmethod
    def draw_field(screen):
        screen.fill(GREEN)

        pygame.draw.line(screen, WHITE, (0, GROUND_Y), (SCREEN_WIDTH, GROUND_Y), 3)

        pygame.draw.rect(
            screen, WHITE, (0, GROUND_Y - GOAL_HEIGHT, GOAL_WIDTH, GOAL_HEIGHT), 3
        )
        pygame.draw.rect(
            screen,
            WHITE,
            (
                SCREEN_WIDTH - GOAL_WIDTH,
                GROUND_Y - GOAL_HEIGHT,
                GOAL_WIDTH,
                GOAL_HEIGHT,
            ),
            3,
        )

        pygame.draw.line(
            screen,
            WHITE,
            (0, GROUND_Y - GOAL_HEIGHT),
            (GOAL_WIDTH, GROUND_Y - GOAL_HEIGHT),
            3,
        )
        pygame.draw.line(
            screen,
            WHITE,
            (SCREEN_WIDTH - GOAL_WIDTH, GROUND_Y - GOAL_HEIGHT),
            (SCREEN_WIDTH, GROUND_Y - GOAL_HEIGHT),
            3,
        )

        for x in range(50, SCREEN_WIDTH, 50):
            pygame.draw.line(
                screen, (200, 255, 200), (x, GROUND_Y), (x, GROUND_Y - 100), 1
            )

        pygame.draw.rect(screen, WHITE, (CENTER_X - 60, GROUND_Y - 100, 120, 100), 2)

    @staticmethod
    def draw_score(screen, player_score, cpu_score):
        font = pygame.font.SysFont(None, 72)

        player_text = font.render(str(player_score), True, WHITE)
        cpu_text = font.render(str(cpu_score), True, WHITE)

        screen.blit(player_text, (SCREEN_WIDTH // 4 - player_text.get_width() // 2, 20))
        screen.blit(cpu_text, (3 * SCREEN_WIDTH // 4 - cpu_text.get_width() // 2, 20))

        separator = font.render("-", True, WHITE)
        screen.blit(separator, (SCREEN_WIDTH // 2 - separator.get_width() // 2, 20))

    @staticmethod
    def draw_timer(screen, time_left, is_overtime):
        font = pygame.font.SysFont(None, 48)

        if is_overtime:
            text = font.render("GOLDEN GOAL", True, YELLOW)
        else:
            text = font.render(f"{int(time_left)}", True, WHITE)
            if time_left <= 10:
                text = font.render(f"{int(time_left)}", True, RED)

        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 80))
        screen.blit(text, text_rect)

    @staticmethod
    def draw_game_over(screen, winner, tournament=None):
        font = pygame.font.SysFont(None, 72)
        small_font = pygame.font.SysFont(None, 48)

        if winner == "player":
            text = font.render("YOU WIN!", True, YELLOW)
        elif winner == "cpu":
            text = font.render("CPU WINS!", True, RED)
        else:
            text = font.render("DRAW!", True, WHITE)

        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(text, text_rect)

        instruction = small_font.render("Press ENTER to continue", True, WHITE)
        instruction_rect = instruction.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        )
        screen.blit(instruction, instruction_rect)

    @staticmethod
    def draw_champion(screen):
        font = pygame.font.SysFont(None, 96)
        small_font = pygame.font.SysFont(None, 48)

        text = font.render("CHAMPION!", True, YELLOW)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(text, text_rect)

        instruction = small_font.render("Press ENTER to return to menu", True, WHITE)
        instruction_rect = instruction.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        )
        screen.blit(instruction, instruction_rect)

    @staticmethod
    def draw_tournament_progress(screen, tournament):
        font = pygame.font.SysFont(None, 48)

        round_text = font.render(tournament.get_current_round(), True, WHITE)
        round_rect = round_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40)
        )
        screen.blit(round_text, round_rect)

        progress_text = font.render(tournament.get_progress(), True, WHITE)
        progress_rect = progress_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)
        )
        screen.blit(progress_text, progress_rect)

        instruction = font.render("Press ENTER to start", True, YELLOW)
        instruction_rect = instruction.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120)
        )
        screen.blit(instruction, instruction_rect)
