import pygame
from constants import *


class ModeSelect:
    def __init__(self):
        self.selected_option = 0
        self.options = ["Quick Game", "Tournament"]

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == KEY_LEFT:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == KEY_RIGHT:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == KEY_ENTER:
                return self.options[self.selected_option]
        return None

    def draw(self, screen):
        screen.fill(GREEN)

        title_font = pygame.font.SysFont(None, 64)
        font = pygame.font.SysFont(None, 48)

        title = title_font.render("HEAD SOCCER", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title, title_rect)

        start_y = 250
        for i, option in enumerate(self.options):
            color = YELLOW if i == self.selected_option else WHITE
            text = font.render(option, True, color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, start_y + i * 80))
            screen.blit(text, text_rect)

            if i == self.selected_option:
                pygame.draw.rect(
                    screen,
                    color,
                    (
                        text_rect.left - 10,
                        text_rect.top - 10,
                        text_rect.width + 20,
                        text_rect.height + 20,
                    ),
                    3,
                )

        instruction = font.render(
            "Use LEFT/RIGHT to select, ENTER to confirm", True, WHITE
        )
        instruction_rect = instruction.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        )
        screen.blit(instruction, instruction_rect)
