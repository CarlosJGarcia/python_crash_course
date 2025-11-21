import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star in the field."""

    def __init__(self, game):
        """Initialize the star and set its starting position"""
        super().__init__()
        self.screen = game.screen

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load("images/star.bmp")
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width  # Anchura de la estrella
        self.rect.y = self.rect.height # Altura de la estrella

        # Store the star's exact horizontal position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Pintar la estrella en su ubicación actual"""
        self.screen.blit(self.image, self.rect)