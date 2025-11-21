from django.db import models

class Pizza(models.Model):
	"""A pizza."""
	name = models.TextField()

	def __str__(self):
		"""Return a string representation of the model."""
		return self.name

class Topping(models.Model):
	"""Something that goes on top of a pizza."""
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	name = models.TextField()

	class Meta:
		verbose_name_plural = 'toppings'

	def __str__(self):
                """Return a string representation of the model."""
                return self.name
