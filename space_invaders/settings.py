class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""

        # Screen settings
        self.frame_rate = 60
        self.bg_color = (0, 0, 0)
        self.fg_color = (255, 255, 255)
        self.ln_color = (0, 255, 0)
        self.screen_width = 250 * 3
        self.screen_height = 280 * 3

         # Ship settings
        self.ship_limit = 2     # 3 Naves 0, 1 y 2 :-)

         # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 1

         # Alien/Fleet settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.5

        # Scoring settings
        self.alien_points = 30
        """
        Bottom-row alien: 10 points
        Middle-row alien: 20 points
        Top-row alien: 30 points
        Mystery spaceship UFO at the top: 50-300 points, depending on where it appeared (randomly)
        """
        
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Initialize game dynamic settings"""

        # Ship settings
        self.ship_speed = 4.5

        # Bullet settings
        self.bullet_speed = 5.5

        # Alien/Fleet settings
        self.alien_speed = 1.0
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale