class Employee:
    """Declaration of class Employee"""

    def __init__(self, first_name, last_name, annual_salary):
        """Store the information as class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Method that by default adds $5.000 to the annual salary but also accepts a different raise amount"""
        self.annual_salary += amount