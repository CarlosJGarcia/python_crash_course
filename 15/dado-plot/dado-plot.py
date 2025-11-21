"""
A number raised to the third power is a cube. Plot the first five cubic numbers and then plot the first 5.000 cubic numbers
Apply a colormap to your cubes plot
Version orientada a objetos
"""

import matplotlib.pyplot as plt

from dataset import Dataset

# Genera el dataset
ds = Dataset(300)
ds.generate()

# Inicializa el gráfico
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()       # return fig, ax

# Set chart title and label axes
ax.set_title("Scatter plotter. Press Q to exit.", fontsize=24)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)

# Toggles full-screen mode
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()  

# Datos
ax.scatter(ds.x_values, ds.y_values, c=ds.y_values, cmap=plt.cm.Blues)

plt.show()