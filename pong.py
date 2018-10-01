# Aaron Xaymountry
# axaymountry@csu.fullerton.edu
# Pong with no walls assignment

import sys

import pygame

from settings import Settings
from paddle import Paddle
from ball import Ball
from button import Button
from menu import Menu
import game_functions as gf


def run_game():

    # Initialize pygame, settings, and screen object.
    pygame.init()
    topbot_settings = Settings(True)
    side_settings = Settings(False)
    paddlegap = 10

    screen = pygame.display.set_mode((side_settings.screen_width, side_settings.screen_height))
    pygame.display.set_caption("Pong AI without walls")

    # Make the ball
    ball = Ball(side_settings, screen)
    balls = pygame.sprite.Group()
    balls.add()

    # Make play button
    play_button = Button(side_settings.screen_width / 2, side_settings.screen_height / 2, side_settings, screen, "Play")

    # Make menu
    menu = Menu(side_settings, screen, play_button)

    # Make player paddles
    playerPaddle = Paddle(paddlegap, ((side_settings.screen_height / 2) - (side_settings.paddle_length / 2)),
                          side_settings, screen)
    playertoppaddle = Paddle(((side_settings.screen_width / 4) - (topbot_settings.paddle_width / 2))
                             , 10, topbot_settings, screen)
    playerbotpaddle = Paddle(((side_settings.screen_width / 4) - (topbot_settings.paddle_width / 2)),
                             (side_settings.screen_height - paddlegap - topbot_settings.paddle_length),
                             topbot_settings, screen)

    # Make ai/player 2 paddles
    aiPaddle = Paddle((side_settings.screen_width - side_settings.paddle_width - paddlegap),
                      ((side_settings.screen_height / 2) - (side_settings.paddle_length / 2)), side_settings, screen)
    aitop = Paddle(((side_settings.screen_width - (side_settings.screen_width / 4)) -
                    (topbot_settings.paddle_width / 2)), paddlegap, topbot_settings, screen)
    aibot = Paddle(((side_settings.screen_width - (side_settings.screen_width / 4)) -
                    (topbot_settings.paddle_width / 2)), (side_settings.screen_height - paddlegap -
                                                          topbot_settings.paddle_length), topbot_settings, screen)

    # TESTING MENU SCREEN HERE
    menu.makeScreen(side_settings, screen, play_button)

    # Start the main loop for the game.
    while True:
        gf.check_events(side_settings, screen, playerPaddle, playertoppaddle, playerbotpaddle)
        gf.update_screen(side_settings, screen, playerPaddle, playertoppaddle, playerbotpaddle)

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(side_settings.bg_color)

        # Draw the ball in the middle
        ball.draw(screen)

        # Draws player side paddles
        playerPaddle.draw()
        playertoppaddle.draw()
        playerbotpaddle.draw()

        # Draws ai side paddles
        aiPaddle.draw()
        aitop.draw()
        aibot.draw()

        # Draws the middle line
        pygame.draw.line(screen, (250, 250, 250), (side_settings.screen_width / 2, 0),
                         (side_settings.screen_width / 2, side_settings.screen_height))

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()