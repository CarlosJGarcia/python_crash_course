# Find an image of a star
# Make a grid of raindrops appear on the screen
# Make the raindrops fall towards the bottom of the screen until they dissapear
# When a row of raindrops dissapears off the bottom of the screen, a new row appears a the top of the screen and begins to fall

import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from raindrop import Raindrop
from settings import Settings

class Raindrops:
    """Overall class to manage assets and vehavior."""

    def __init__(self):
        """Initialize the display, clock and create game resources: star object"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption("Raindrops")
        self.raindrops = pygame.sprite.Group()                                    
        self._create_grid()
    

    def _create_grid(self):
        """Create the grid of Raindrops"""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        current_x, current_y = raindrop_width, raindrop_height
        while current_y < (self.settings.screen_height - raindrop_height):
            self._create_row(current_y, raindrop_width, raindrop_height)
            current_y += 2 * raindrop_height

    def _create_row(self, y, raindrop_width, raindrop_height):
        """Create a row of raindrops at a given y position"""
        current_x = raindrop_width        
        while current_x < (self.settings.screen_width - raindrop_width):
            new_raindrop = Raindrop(self)
            new_raindrop.x = current_x
            new_raindrop.y = y
            new_raindrop.rect.x = current_x
            new_raindrop.rect.y = y
            self.raindrops.add(new_raindrop)
            current_x += 2 * raindrop_width
            
    def _check_and_add_new_row(self):
        """Check if any row has left the screen and add a new row at the top"""
        if not self.raindrops:
            return
        raindrop = next(iter(self.raindrops))
        raindrop_height = raindrop.rect.height

        # Find all raindrops at the bottom (off screen)
        rows_to_remove = set()
        for drop in self.raindrops:
            if drop.rect.top >= self.settings.screen_height:
                rows_to_remove.add(drop.rect.y)

        # Remove those rows and add new ones at the top
        for y in rows_to_remove:
            for drop in list(self.raindrops):
                if drop.rect.y == y:
                    self.raindrops.remove(drop)
            self._create_row(raindrop_height, raindrop.rect.width, raindrop_height)


    def run_game(self):
        """Start the main loop for the game."""
        
        # Bucle del juego
        while True:
            # Bucle de eventos (keyboard and mouse events)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Update raindrops and check for new rows
            self.raindrops.update()
            self._check_and_add_new_row() 

            # Pintar fondo y objecos en pantalla
            self.screen.fill(self.settings.bg_color)
      
            self.raindrops.draw(self.screen)
            

            # Redibujar la pantalla y ciclo de reloj
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    # Make a game instance and run the game
    rd = Raindrops()
    rd.run_game()
