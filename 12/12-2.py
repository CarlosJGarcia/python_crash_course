# Python Crash Course
# Carlos Garcia, Basel Septiembre 2025
# Make a Pygame window with a blue background -> Spectrum splash screen

import sys
import pygame

width = 640 * 1.7
height = 480 * 1.5
frame_rate = 60

bg_color = (255, 255, 255)
fg_color = (0, 0, 0)
font_size = 25

# Inicialización pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

# Caption
pygame.display.set_caption("Ejercicio 12-1")    

# Contenido pantalla
font = pygame.font.SysFont(None, font_size)
text_surface = font.render("Sinclair ZX Spectrum 48K con Interface 1 y ZX Microdrive", True, fg_color)
text_rect = text_surface.get_rect()
text_rect.bottomleft = (20, height - 20)  # 10 pixels above the bottom

# Load the Spectrum with Microdrive image and get its rect
image = pygame.image.load('images/spectrum_with_microdrive.png')
image_rect = image.get_rect()
screen_rect = screen.get_rect


# Bucle principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # El usuario ha pulsado el botón rojo en la esquina izda de la ventana para cerrarla
            running = False

    # Fill background every frame
    screen.fill(bg_color)

    # Screen render - Image and text
    screen.blit(image, image_rect)  
    screen.blit(text_surface, text_rect)

    # Update diplay and tick clock
    pygame.display.flip()
    clock.tick(frame_rate)

pygame.quit()