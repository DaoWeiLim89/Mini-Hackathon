import pygame
import random
from constants import *


class Ball:
    def __init__(self):
        self.x = CENTER_X
        self.y = 0
        self.vel_x = 0
        self.vel_y = 0
        self.radius = BALL_RADIUS

    def drop(self):
        self.x = CENTER_X + random.randint(-15, 15)
        self.y = CENTER_Y - 150
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.vel_y += GRAVITY * 0.5

        crossbar_y = GROUND_Y - GOAL_HEIGHT

        if self.y + self.radius >= GROUND_Y:
            self.y = GROUND_Y - self.radius
            self.vel_y *= -0.8
            if abs(self.vel_y) < 1:
                self.vel_y = 0

        if self.y - self.radius <= 0:
            self.y = self.radius
            self.vel_y *= -0.8

        if self.x - self.radius <= 0:
            self.x = self.radius
            self.vel_x *= -0.8
        elif self.x + self.radius >= SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.radius
            self.vel_x *= -0.8

        left_crossbar = (
            self.x >= GOAL_WIDTH - BALL_RADIUS
            and self.x <= GOAL_WIDTH + BALL_RADIUS
            and self.y >= crossbar_y - BALL_RADIUS
            and self.y <= crossbar_y + BALL_RADIUS
        )

        right_crossbar = (
            self.x >= SCREEN_WIDTH - GOAL_WIDTH - BALL_RADIUS
            and self.x <= SCREEN_WIDTH - GOAL_WIDTH + BALL_RADIUS
            and self.y >= crossbar_y - BALL_RADIUS
            and self.y <= crossbar_y + BALL_RADIUS
        )

        if left_crossbar:
            self.vel_y *= -0.8
            if self.y < crossbar_y:
                self.y = crossbar_y - self.radius
            else:
                self.y = crossbar_y + self.radius

        if right_crossbar:
            self.vel_y *= -0.8
            if self.y < crossbar_y:
                self.y = crossbar_y - self.radius
            else:
                self.y = crossbar_y + self.radius

    def check_collision_with_player(self, player):
        player_rect = player.get_rect()
        head_rect = player.get_head_rect()
        ball_rect = pygame.Rect(
            self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2
        )

        if ball_rect.colliderect(head_rect):
            self.vel_x = (self.x - head_rect.centerx) * 0.3
            self.vel_y -= 8
            self.vel_y = max(self.vel_y, BALL_SPEED_Y_MAX * -1)
            return True
        elif ball_rect.colliderect(player_rect):
            self.vel_x = (self.x - player_rect.centerx) * 0.5
            self.vel_y -= 5
            return True
        return False

    def check_goal(self):
        crossbar_y = GROUND_Y - GOAL_HEIGHT

        left_goal = (
            self.x - self.radius <= GOAL_WIDTH
            and self.y > crossbar_y
            and self.y < GROUND_Y
        )
        right_goal = (
            self.x + self.radius >= SCREEN_WIDTH - GOAL_WIDTH
            and self.y > crossbar_y
            and self.y < GROUND_Y
        )

        if self.y >= GROUND_Y - 10 and self.y <= GROUND_Y:
            if self.x >= GOAL_WIDTH and self.x <= GOAL_WIDTH + BALL_RADIUS * 2:
                return "left"
            if (
                self.x >= SCREEN_WIDTH - GOAL_WIDTH - BALL_RADIUS * 2
                and self.x <= SCREEN_WIDTH - GOAL_WIDTH
            ):
                return "right"

        if left_goal:
            return "left"
        elif right_goal:
            return "right"
        return None

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius, 2)

        pattern_x = int(self.x - self.radius * 0.5)
        pattern_y = int(self.y - self.radius * 0.5)
        pattern_size = int(self.radius)
        pattern_rect = pygame.Rect(pattern_x, pattern_y, pattern_size, pattern_size)
        pygame.draw.rect(screen, BLACK, pattern_rect, 2)

        pygame.draw.line(
            screen,
            BLACK,
            (pattern_x, pattern_y + pattern_size),
            (pattern_x + pattern_size, pattern_y),
            2,
        )
        pygame.draw.line(
            screen,
            BLACK,
            (pattern_x + pattern_size, pattern_y + pattern_size),
            (pattern_x, pattern_y),
            2,
        )
