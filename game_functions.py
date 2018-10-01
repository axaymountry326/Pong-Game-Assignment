# Aaron Xaymountry
# axaymountry@csu.fullerton.edu
# Pong with no walls assignment

import sys

import pygame

from paddle import Paddle


def check_keydown_events(event, ai_settings, screen, side_paddle, top_paddle, bot_paddle):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        top_paddle.moving_right = bot_paddle.moving_right = True
    elif event.key == pygame.K_LEFT:
        top_paddle.moving_left = bot_paddle.moving_left = True

    if event.key == pygame.K_UP:
        side_paddle.moving_up = True
    elif event.key == pygame.K_DOWN:
        side_paddle.moving_down = True

    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, side_paddle, top_paddle, bot_paddle):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        top_paddle.moving_right = bot_paddle.moving_right = False
    elif event.key == pygame.K_LEFT:
        top_paddle.moving_left = bot_paddle.moving_left = False
    if event.key == pygame.K_UP:
        side_paddle.moving_up = False
    elif event.key == pygame.K_DOWN:
        side_paddle.moving_down = False


def check_events(ai_settings, screen, side_paddle, top_paddle, bot_paddle):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, side_paddle, top_paddle, bot_paddle)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, side_paddle, top_paddle, bot_paddle)


def update_screen(ai_settings, screen, side_paddle, top_paddle, bot_paddle):
    '''
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    paddle.draw()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
    '''

    if top_paddle.moving_right and (top_paddle.rect.x + top_paddle.width) < (ai_settings.screen_width / 2):
        top_paddle.rect.x += ai_settings.speed_factor
        bot_paddle.rect.x += ai_settings.speed_factor

    elif top_paddle.moving_left and top_paddle.rect.x > 0:
        top_paddle.rect.x -= ai_settings.speed_factor
        bot_paddle.rect.x -= ai_settings.speed_factor

    if side_paddle.moving_up and side_paddle.rect.y > 0:
        side_paddle.rect.y -= ai_settings.speed_factor

    elif side_paddle.moving_down  and (side_paddle.rect.y + side_paddle.length) < ai_settings.screen_height:
        side_paddle.rect.y += ai_settings.speed_factor

