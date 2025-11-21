class Cat:
    """Clase gato"""
    def __init__(self, name, age):
        """Attributes"""
        self.name = name
        self.age = age
        self.sleeping = False

    def sleep(self):
        """Makes the cat sleep"""
        self.sleeping = True
        print("The cat is sleeping.")