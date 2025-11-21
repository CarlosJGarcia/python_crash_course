import matplotlib.pyplot as plt

num_puntos = 50000

def function(x):
    y = x ** 2 + x + 1
    return y

input_values = []
squares = []
for n in range(-1 * num_puntos , num_puntos + 1):
    input_values.append(n)
    squares.append(function(n))


# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()       # return fig, ax

# Set chart title and label axes
ax.set_title("Function plotter", fontsize=24)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

ax.plot(input_values, squares, linewidth=3)
plt.show()
