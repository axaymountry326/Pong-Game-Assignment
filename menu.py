# Aaron Xaymountry
# axaymountry@csu.fullerton.edu
# Pong with no walls assignment

import sys
import pygame
import pygame.font
from button import Button

from pygame.sprite import Group

from settings import Settings


class Menu():

    def __init__(self, theSettings, screen, button):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.theSettings = Settings
        self.button = Button

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        screen = pygame.display.set_mode((theSettings.screen_width, theSettings.screen_height))
        pygame.display.set_caption('PONG')
        screen.fill(theSettings.bg_color)

    def makeScreen(self, theSettings, screen, button):
        pygame.init()
        button = Button(theSettings.screen_width / 2, theSettings.screen_height / 2, theSettings, screen, "PLAY")
        screen = pygame.display.set_mode((theSettings.screen_width, theSettings.screen_height))
        pygame.display.set_caption("PONG with NO WALLS")

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill(theSettings.bg_color)

        # Display text
        font = pygame.font.Font(None, 144)
        text1 = font.render("PONG", 2, (10, 100, 250))
        #textpos = text.get_rect()
        #textpos.centerx = background.get_rect().centerx
        textpos1 = (theSettings.screen_width / 8, theSettings.screen_height / 60)
        font = pygame.font.Font(None, 100)
        text2 = font.render("AI -- NO WALLS", 1, (255, 255, 255))
        textpos2 = (theSettings.screen_width / 50, theSettings.screen_height / 6)
        background.blit(text1, textpos1)
        background.blit(text2, textpos2)

        # Blit everything to screen
        screen.blit(background, (200, 200))
        button.draw_button
        pygame.display.flip()

        while True:
            click_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button.isOver(click_pos):
                        print('button clicked')
                        return

            screen.blit(background, (0, 0))
            button.draw_button()
            pygame.display.flip()