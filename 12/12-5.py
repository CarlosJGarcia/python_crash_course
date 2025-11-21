# Python Crash Course
# Carlos Garcia, Londres, Octubre 2025
"""
Make a pygame file that creates an empty screen.
In the event loop, print the event.key attribute whenever a pygame.KEYDOWN event is detected.
Run the program and press various keys to see how pygame responds
"""

import pygame

width = 640
height = 480
frame_rate = 60

font_size = 25
fg_color = (0, 0, 0)
bg_color = (255, 255, 255)


# Inicialización pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

# Caption
pygame.display.set_caption("Ejercicio 12-5")    

# Contenido pantalla
font = pygame.font.SysFont(None, font_size)
text_surface = font.render("", True, fg_color)
text_rect = text_surface.get_rect()


# Bucle principal
while running:

    # Gestión de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # El usuario ha pulsado el botón rojo en la esquina izda de la ventana para cerrarla
            running = False
        elif event.type == pygame.KEYDOWN:
            text = "event.key = " + str(event.key)
            text_surface = font.render(text, True, fg_color)
            text_rect = text_surface.get_rect()
            text_rect.bottomleft = (20, height - 20)  # 10 pixels above the bottom
            
    # Fill background every frame
    screen.fill(bg_color)

    # Screen render - Draw text
    screen.blit(text_surface, text_rect)

    # Update diplay and tick clock
    pygame.display.flip()
    clock.tick(frame_rate)

pygame.quit()