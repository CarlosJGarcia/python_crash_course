import os
import pygame.font
from pygame.sprite import Group

from ship import Ship
from settings import Settings

class Scoreboard:
    """A class to display scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.settings = Settings()

        # Font settins to display score information
        self.text_color = self.settings.fg_color
        # self.font = pygame.font.SysFont(None, 48)

        # Load font otherwise fallback to default
        font_path = "fonts/press_start2p-regular.ttf"
        if os.path.exists(font_path):
            self.font = pygame.font.Font(font_path, 25)
        else:
            self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_title()
        self.prep_title_highscore()
        self.prep_title_score2()
        self.prep_score()
        self.prep_high_score()
        self.prep_ships()
        

    def prep_ships(self):
        """Show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.bottom = self.screen_rect.bottom - 20
            self.ships.add(ship)

    def prep_title(self):
        """Turn the titole into a rendered image"""
        title_str = "SCORE<1>"
        self.title_image = self.font.render(title_str, True, self.settings.fg_color, self.settings.bg_color)

        # Display the score at the top left of the screen
        self.title_rect = self.title_image.get_rect()
        self.title_rect.left = self.screen_rect.left + 10
        self.title_rect.top = 10
    
    def prep_title_highscore(self):
        """Turn the high score title into a rendered image"""
        title_str = "HI-SCORE"
        self.title_hiscore_image = self.font.render(title_str, True, self.settings.fg_color, self.settings.bg_color)

        # Display the score at the top left of the screen
        self.title_hiscore_rect = self.title_hiscore_image.get_rect()
        self.title_hiscore_rect.centerx = self.screen_rect.centerx
        self.title_hiscore_rect.top = 10

    def prep_title_score2(self):
        """Turn the score-2 title into a rendered image"""
        title_str = "SCORE<2>"
        self.title_score2_image = self.font.render(title_str, True, self.settings.fg_color, self.settings.bg_color)

        # Display the score at the top left of the screen
        self.title_score2_rect = self.title_score2_image.get_rect()
        self.title_score2_rect.right = self.screen_rect.right - 10
        self.title_score2_rect.top = 10

    def prep_score(self):
        """Turn the score into a rendered image"""
        score_str = f"{self.stats.score:04}"
        self.score_image = self.font.render(score_str, True, self.settings.fg_color, self.settings.bg_color)

        # Display the score at the top left of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 40
        self.score_rect.top = 60

    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        high_score_str = f"{self.stats.high_score:04}"
        self.high_score_image = self.font.render(high_score_str, True, self.settings.fg_color, self.settings.bg_color)

        # Display the score at the top center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 60

    def show_score(self):
        """Draw score (title, high-score and score) to the screen"""
        self.screen.blit(self.title_image, self.title_rect)
        self.screen.blit(self.title_hiscore_image, self.title_hiscore_rect)
        self.screen.blit(self.title_score2_image, self.title_score2_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)
        
    def check_high_score(self):
        """Check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
