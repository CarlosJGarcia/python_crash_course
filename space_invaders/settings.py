class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""

        # Screen settings
        self.screen_width = 224 * 3
        self.screen_height = 256 * 3
        self.frame_rate = 60
        self.bg_color = (0, 0, 0)

         # Ship settings
        self.ship_speed = 4.5

         # Bullet settings
        self.bullet_speed = 5.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 1