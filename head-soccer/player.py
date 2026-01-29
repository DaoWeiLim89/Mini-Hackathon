import pygame
from constants import *


class Player:
    def __init__(self, x, y, color, is_player=True):
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.color = color
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.on_ground = False
        self.is_player = is_player

    def handle_input(self, keys):
        if self.is_player:
            self.vel_x = 0
            if keys[KEY_LEFT]:
                self.vel_x = -PLAYER_SPEED
            if keys[KEY_RIGHT]:
                self.vel_x = PLAYER_SPEED
            if keys[KEY_JUMP] and self.on_ground:
                self.vel_y = JUMP_FORCE
                self.on_ground = False

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.vel_y += GRAVITY

        boundaries = GOAL_WIDTH if self.is_player else SCREEN_WIDTH - GOAL_WIDTH

        if self.x < boundaries:
            self.x = boundaries
        elif self.x + self.width > SCREEN_WIDTH - boundaries:
            self.x = SCREEN_WIDTH - boundaries - self.width

        if self.y >= GROUND_Y - self.height:
            self.y = GROUND_Y - self.height
            self.vel_y = 0
            self.on_ground = True

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def get_head_rect(self):
        head_size = 30
        head_x = self.x + (self.width - head_size) / 2
        head_y = self.y - head_size
        return pygame.Rect(head_x, head_y, head_size, head_size)

    def draw(self, screen):
        body_rect = self.get_rect()
        pygame.draw.rect(screen, self.color, body_rect)

        head_rect = self.get_head_rect()
        pygame.draw.circle(
            screen,
            (255, 220, 180),
            (int(head_rect.centerx), int(head_rect.centery)),
            15,
        )

        eyes_x = int(head_rect.centerx) - 5
        pygame.draw.circle(screen, BLACK, (eyes_x, int(head_rect.centery) - 2), 3)
        pygame.draw.circle(screen, BLACK, (eyes_x + 10, int(head_rect.centery) - 2), 3)
