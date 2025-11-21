class Dataset:
    """ A class to model and generate the dataset"""

    def __init__(self, num_puntos=5000):
        """Initialize dataset attributes, by default it has 5000 points"""
        self.num_puntos = num_puntos
        self.x_values, self.y_values = [], []
    
    # Codificación en python de la función y=f(x)
    def _function(self, x):
        y = x ** 3
        return y

    def generate(self):
        """ Generate the data in the dataset """
        for n in range(0 , self.num_puntos):
            self.x_values.append(n)
            self.y_values.append(self._function(n))
