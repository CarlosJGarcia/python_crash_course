import plotly.express as px

from die import Die

# Create two D6
die_1 = Die()
die_2 = Die(10)

tiradas = 50000


# Make some rolls and store results in a list
results = []
for roll_num in range(tiradas):
    result = die_1.roll() + die_2.roll()
    results.append(result)

"""
print(f"Resultado de tirar {roll_num} veces un dado de seis caras")
print(results)
print()
"""

# Analyze the results
frequencies = []
poss_results = range(2, die_1.num_sides + die_2.num_sides)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = f"Results of Rolling One D6 {tiradas} times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
fig.write_html('dice-plot-d6d10.html')