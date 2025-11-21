import plotly.express as px

from die import Die

# Create a D6
die = Die()
tiradas = 1000


# Make some rolls and store results in a list
results = []
for roll_num in range(tiradas):
    result = die.roll()
    results.append(result)

"""
print(f"Resultado de tirar {roll_num} veces un dado de seis caras")
print(results)
print()
"""

# Analyze the results
frequencies = []
poss_results = range(1, die.num_sides)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = f"Results of Rolling One D6 {tiradas} times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()