import numpy as np
import pygame

DIRECTIONS = {
    "top_left": [-1, -1],
    "top_right": [1, -1],
    "bot_left": [-1, 1],
    "bot_right": [1, 1],
}


def random_direction():
    return DIRECTIONS[np.random.choice(list(DIRECTIONS.keys()))]


# accessing position as tuple
X, Y = 0, 1


class Ball:
    VELOCITY = 8

    def __init__(self, pos):
        self.direction = random_direction()
        self.init_pos = pos

        # underlying rectangle representing the ball
        # the position is given by Rect members (.x, .y)
        self.rect = pygame.Rect(pos[X], pos[Y], 30, 30)

    def draw(self, canvas):
        pygame.draw.rect(canvas, pygame.Color("white"), self.rect)

    def set_position(self, nx, ny):
        self.rect.x = nx
        self.rect.y = ny

    def get_position(self):
        return self.rect.x, self.rect.y

    def in_paddle_area(self, paddle):
        py = paddle.get_position()
        temp_boolean=(py <= self.rect.y <= py + Paddle.LENGTH or py<=self.rect.y+ 30<= py + Paddle.LENGTH )
        return temp_boolean

    def reset(self):
        self.direction = random_direction()
        self.rect = pygame.Rect(self.init_pos[X], self.init_pos[Y], 30, 30)


class Paddle:
    VELOCITY = 8
    LENGTH = 50

    def __init__(self, pos, color="green"):
        self.init_pos = pos
        self.direction = 0
        self.color = color

        # position is given by rect member (.x, .y)
        self.rect = pygame.Rect(pos[X], pos[Y], 1, Paddle.LENGTH)

    def set_position(self, ny):
        self.rect.y = ny

    def get_position(self):
        return self.rect.y

    def draw(self, canvas):
        pygame.draw.rect(canvas, pygame.Color(self.color), self.rect)

    def reset(self):
        self.direction = 0
        self.rect = pygame.Rect(self.init_pos[X], self.init_pos[Y], 1, Paddle.LENGTH)
