# Aaron Xaymountry
# axaymountry@csu.fullerton.edu
# Pong with no walls assignment


import pygame.font


class Button():

    def __init__(self, x, y, the_settings, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 100)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object, and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.x = x - 100
        self.y = y - 50

        # The button message only needs to be prepped once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image, and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button, then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def isOver(self, pos):
        # Check if the mouse is over the button
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False
