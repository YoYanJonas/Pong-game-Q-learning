import numpy as np
import pygame
import random




BASE_DISTANCE_VALUE=50
BLOCK_LENGTH=80
BLOCK_WIDTH=1
BALL_SIZE= 30

DIRECTIONS = {
    "top_left": [-1, -1],
    "top_right": [1, -1],
    "bot_left": [-1, 1],
    "bot_right": [1, 1],
}
WHITE = (255, 255, 255)

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
        self.rect = pygame.Rect(pos[X], pos[Y], BALL_SIZE, BALL_SIZE)

    def draw(self, canvas):
        pygame.draw.rect(canvas, pygame.Color("white"), self.rect)

    def set_position(self, nx, ny):
        self.rect.x = nx
        self.rect.y = ny

    def get_position(self):
        return self.rect.x, self.rect.y

    def in_paddle_area(self, paddle):
        py = paddle.get_position()
        temp_boolean=(py <= self.rect.y <= py + Paddle.LENGTH or py<=self.rect.y+ BALL_SIZE<= py + Paddle.LENGTH )
        return temp_boolean
    
    def in_block_area(self, block):
        bx = block.get_position()
        temp_boolean=(bx <= self.rect.x <= bx + BLOCK_LENGTH or bx <= self.rect.x + BALL_SIZE <= bx + BLOCK_LENGTH)

        return temp_boolean

    def reset(self):
        self.direction = random_direction()
        self.rect = pygame.Rect(BASE_DISTANCE_VALUE*random.randint(5,13), BASE_DISTANCE_VALUE*random.randint(0,4)+BALL_SIZE, BALL_SIZE, BALL_SIZE)

class MovingBlock:
    COLOR=WHITE
    VELOCITY= 8
    directions=[-1,1]

    def __init__(self, y):
        self.x=self.original_x=8.5*BASE_DISTANCE_VALUE
        self.y=self.original_y=y
        self.direction=self.directions[random.randint(0,1)]
        self.rect = pygame.Rect(8.5*BASE_DISTANCE_VALUE,y, BLOCK_LENGTH, BLOCK_WIDTH )

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.COLOR, self.rect)


    def shift_back(self):
        self.direction *= -1
    
    def get_position(self):
        return self.rect.x
    
    def set_position(self, next_x):
        self.rect.x= next_x
    
    # def move(self):
    #     if (self.x <= 5*BASE_DISTANCE_VALUE) :
    #         self.x_vel *= -1
    #     elif(self.x >= 13*BASE_DISTANCE_VALUE-BLOCK_LENGTH):
    #         self.x_vel *= -1
    #     self.x += self.x_vel

    def reset(self):
        self.x=self.original_x
        self.y=self.original_y
        self.direction=self.directions[random.randint(0,1)]


class Paddle:
    VELOCITY = 8
    LENGTH = 60

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
