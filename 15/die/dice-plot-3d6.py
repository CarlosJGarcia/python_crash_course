import plotly.express as px

from die import Die

# Create three D6
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

tiradas = 5_000_000


# Make some rolls and store results in a list
results = []
for roll_num in range(tiradas):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results
frequencies = []
poss_results = range(2, die_1.num_sides + die_2.num_sides + die_3.num_sides)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = f"Results of Rolling three D6 {tiradas} times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
