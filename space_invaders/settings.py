class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""

        # Screen settings
        self.frame_rate = 60
        self.bg_color = (0, 0, 0)
        self.screen_width = 224 * 3
        self.screen_height = 256 * 3

         # Ship settings
        self.ship_limit = 2     # 3 Naves 0, 1 y 2 :-)
        self.ship_speed = 4.5

         # Bullet settings
        self.bullet_speed = 5.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 1

         # Alien/Fleet settings
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.fleet_drop_speed = 10