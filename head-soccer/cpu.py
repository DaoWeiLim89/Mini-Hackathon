import random
from player import Player
from constants import *


class CPU(Player):
    def __init__(self, x, y):
        super().__init__(x, y, BLUE, is_player=False)
        self.reaction_delay = 0
        self.target_x = x

    def update_ai(self, ball_x, ball_vel_x, ball_y):
        self.reaction_delay -= 1

        if self.reaction_delay <= 0:
            reaction_time = random.randint(1, 5)
            self.reaction_delay = reaction_time

            if ball_x > CENTER_X:
                self.target_x = ball_x - 20
                if (
                    self.on_ground
                    and ball_y > self.y - 130
                    and abs(ball_x - self.x) < 100
                ):
                    self.vel_y = JUMP_FORCE
                    self.on_ground = False
            else:
                self.target_x = self.x

        left_boundary = GOAL_WIDTH + 50
        right_boundary = SCREEN_WIDTH - GOAL_WIDTH - 50

        if self.target_x < left_boundary:
            self.target_x = left_boundary
        elif self.target_x > right_boundary:
            self.target_x = right_boundary

        diff = self.target_x - self.x
        if abs(diff) > PLAYER_SPEED:
            if diff > 0:
                self.vel_x = PLAYER_SPEED
            else:
                self.vel_x = -PLAYER_SPEED
        else:
            self.vel_x = 0

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.vel_y += GRAVITY

        left_boundary = GOAL_WIDTH + 50
        right_boundary = SCREEN_WIDTH - GOAL_WIDTH - 50

        if self.x < left_boundary:
            self.x = left_boundary
        elif self.x + self.width > right_boundary:
            self.x = right_boundary - self.width

        if self.y >= GROUND_Y - self.height:
            self.y = GROUND_Y - self.height
            self.vel_y = 0
            self.on_ground = True
