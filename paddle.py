# Aaron Xaymountry
# axaymountry@csu.fullerton.edu
# Pong with no walls assignment

import pygame


class Paddle():
    def __init__(self, x, y, ai_settings, screen):
        """Create a paddle"""
        self.screen = screen
        self.x = x
        self.y = y
        self.width = ai_settings.paddle_width
        self.length = ai_settings.paddle_length
        # Create paddle
        self.rect = pygame.Rect(x, y, ai_settings.paddle_width, ai_settings.paddle_length)

        self.color = ai_settings.color
        self.speed_factor = ai_settings.speed_factor

        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)




