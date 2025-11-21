from random import choice

class RandomWalk:
    """A class to generate random walks"""
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # Start at (0,0)
        self.x_values, self.y_values = [0], [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches the desired lenght
        while len(self.x_values) < self.num_points:

            # Movimiento en eje X: Decide which direction to go and how far to go
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance

            # Movimiento en eje Y: Decide which direction to go and how far to go
            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step   # Último valor de la X + step-x
            y = self.y_values[-1] + y_step   # Último valor de la Y + step-y
            self.x_values.append(x)
            self.y_values.append(y)