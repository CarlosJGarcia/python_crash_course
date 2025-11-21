"""
Replace ax.scatter() with ax.plot
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

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

# Genera el dataset
rw = RandomWalk()
rw.fill_walk()

# Datos
point_numbers = range(0,rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=2)
ax.set_aspect('equal')

plt.show()