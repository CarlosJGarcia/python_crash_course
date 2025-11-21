import matplotlib.pyplot as plt

num_puntos = 5

def function(x):
    y = x ** 2 + x + 1
    return y

x_values, y_values = [], []
for n in range(-1 * num_puntos , num_puntos):
    x_values.append(n)
    y_values.append(function(n))

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()       # return fig, ax
ax.scatter(x_values, y_values, s=200)

# Set chart title and label axes
ax.set_title("Scatter plotter", fontsize=24)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)

plt.show()