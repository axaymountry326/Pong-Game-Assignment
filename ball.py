# Aaron Xaymountry
# axaymountry@csu.fullerton.edu
# Pong with no walls assignment

import pygame
import random
import math
from settings import Settings

class Ball(object):
    def __init__(self, thesettings, screen):
        super(Ball, self).__init__()
        self.screen = screen
        thesettings = Settings
        self.x = 400
        self.y = 300
        self.vx = -.5
        self.vy = -.5
        self.color = (0, 100, 250)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)




