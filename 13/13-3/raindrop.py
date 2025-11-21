import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single star in the field."""

    def __init__(self, game):
        """Initialize the raindrop and set its starting position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load("images/raindrop.bmp")
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width  # Anchura de la estrella
        self.rect.y = self.rect.height # Altura de la estrella

        # Store the star's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the raindrop down"""
        print("Función update")
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y

    def blitme(self):
        """Pintar la estrella en su ubicación actual"""
        self.screen.blit(self.image, self.rect)