import matplotlib.pyplot as plt

from die import Die

# Create two D8
die_1 = Die(8)
die_2 = Die(8)

tiradas = 5_000_000


# Make some rolls and store results in a list
results = []
for roll_num in range(tiradas):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
poss_results = range(2, die_1.num_sides * die_2.num_sides)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results (matplotlib)
title = f"Results of Rolling two D8 {tiradas} times"
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))
x = list(poss_results)
ax.bar(x, frequencies, align='center')
ax.set_title(title)
ax.set_xlabel('Result')
ax.set_ylabel('Frequency of Result')
ax.set_xticks(x)
# rotate xtick labels only if crowded
if len(x) > 20:
    plt.setp(ax.get_xticklabels(), rotation=90)
plt.tight_layout()
plt.show()