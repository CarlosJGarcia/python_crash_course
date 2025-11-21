import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single star in the field."""

    def __init__(self, game):
        """Initialize the raindrop and set its starting position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load("images/raindrop.bmp")
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width  # Anchura de la gota
        self.rect.y = self.rect.height # Altura de la gota

        # Store the raindrop's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the raindrop down"""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y

    def blitme(self):
        """Pintar la estrella en su ubicación actual"""
        self.screen.blit(self.image, self.rect)