"""
15-1 A number raised to the third power is a cube. Plot the first five cubic numbers and then plot the first 5.000 cubic numbers
15-2 Apply a colormap to your cubes plot
"""

import matplotlib.pyplot as plt

num_puntos = 5000

def function(x):
    y = x ** 3
    return y

x_values, y_values = [], []
for n in range(0 , num_puntos):
    x_values.append(n)
    y_values.append(function(n))

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()       # return fig, ax
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues)

# Set chart title and label axes
ax.set_title("Scatter plotter", fontsize=24)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)

plt.show()