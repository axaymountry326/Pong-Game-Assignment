# Aaron Xaymountry
# axaymountry@csu.fullerton.edu
# Pong with no walls assignment

class Settings(object):
    """A class to store all settings for Pong game"""

    def __init__(self, isSide):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.speed_factor = 1
        if isSide:
            self.paddle_width = 100
            self.paddle_length = 10
        else:
            self.paddle_width = 10
            self.paddle_length = 100
        self.color = (250, 250, 250)
        self.bg_color = (0, 0, 0)
