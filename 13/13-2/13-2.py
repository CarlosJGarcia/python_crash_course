# Find an image of a star
# Make a grid of stars appear on the screen
# Make a more realistic star pattern by introducing a randomness when placing each star

import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from star import Star
from random import randint
from settings import Settings


class StarField:
    """Overall class to manage assets and vehavior."""

    def __init__(self):
        """Initialize the display, clock and create game resources: star object"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption("Star field")
        self.stars = pygame.sprite.Group()                                    
        self._create_grid()
    

    def _create_grid(self):
        """Create the grid of stars"""
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.settings.screen_height - star_height):
            while current_x < (self.settings.screen_width - star_width):
                new_star = Star(self)
                random_number = randint(-1 * self.settings.random_factor, self.settings.random_factor)
                new_star.x = current_x + random_number
                new_star.y = current_y + random_number
                new_star.rect.x = current_x + random_number
                new_star.rect.y = current_y + random_number
                self.stars.add(new_star)
                current_x += 2 * star_width
            current_x = star_width
            current_y += 2 * star_height


    def run_game(self):
        """Start the main loop for the game."""
        
        # Bucle del juego
        while True:
            # Bucle de eventos (keyboard and mouse events)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Pintar fondo y objecos en pantalla
            self.screen.fill(self.settings.bg_color)
            self.stars.draw(self.screen)
            
            # Redibujar la pantalla y ciclo re reloj
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    # Make a game instance and run the game
    sf = StarField()
    sf.run_game()
