import os
import sys
from time import sleep

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from ship import Ship
from alien import Alien
from button import Button
from bullet import Bullet
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard


class AlienInvasion:
    """Overall class to manage game assets and vehavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")                                              

        
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)             # Create an instance to store game statisticks and create a scoreboard
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self._create_fleet()

        # Start the game in inactive state
        self.game_active = False

        # Make the Play button
        self.play_button = Button(self, "Play")

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)  

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
    
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row, reset x value and increment y value
            current_x = alien_width
            current_y += 2 * alien_height

    def _check_fleet_edges(self):
        """Respond appropiately if any alien reaches an screen edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # El usuario ha pulsado Cmd+Q o el botón rojo en la esquina izda de la ventana para cerrarla
                # Salimos con sys.exit() ya que si intento salir con pygame.quit() da varios errores
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos, event)
              
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            mouse_pos = pygame.mouse.get_pos()
            self._check_play_button(mouse_pos, event)


    def _check_keyup_events(self, event):
        """Respond to keyreleases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False   

    def _start_game(self):
        # Reset the game statistics
            self.stats.reset_stats()

            # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Ocultar el puntero del ratón
            pygame.mouse.set_visible(False)

            # Activamos el juego
            self.game_active = True

    def _check_play_button(self, mouse_pos, event):
        """Start a new game when the player clicks Play"""
        
        # La comprobación solo funciona cuando el juego está parado y el botón está activo (no ha sido pulsado todavía)
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.init_dynamic_settings()
            self._start_game()
            self.sb.prep_score()
        elif event.key == pygame.K_p and not self.game_active:
            self.settings.init_dynamic_settings()
            self._start_game()
            self.sb.prep_score()    
            

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collision."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # Cuenta los puntos
        if collisions:
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()

        # Comprueba si se han destruido todos los aliens
        if not self.aliens:
            # Destroy existing bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
    
    def _update_bullets(self):
        """Update position of bullets and get rid of bullets that have dissapeared (not in the screen anymore)"""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have dissapeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        # Check for bullets that have hit aliens and get rid of the alien and the bullet
        self._check_bullet_alien_collisions()

    def _update_aliens(self):
        """Update the position of all aliens in the fleet."""
        #Check if the fleet is at an edge, then update postions
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen (¿cuando pasa esto?)
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            # Decrement ships left
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False

             # Vuelvo a mostrar el puntero del ratón
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any alien has reached the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break

    def _update_screen(self):
        """Redraw the screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the score information
        self.sb.show_score()

        # If the game is inactive, draw the play button
        if not self.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            self.clock.tick(self.settings.frame_rate)

if __name__ == '__main__':
    # Make a game instance and run the game. Crea una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()
