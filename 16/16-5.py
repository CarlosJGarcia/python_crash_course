

import csv
from pathlib import Path
import matplotlib.pyplot as plt
# from datetime import datetime

# Carga los datos del fichero
path = Path("garmin/weight.csv")
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)

# Lee cabecera
header_row = next(reader)

# Extract weight
n = 0
dates, weight = [], []
for row in reader:    
    if len(row) == 2:
        print(f"Fecha: {row}")
    elif len(row) > 2: 
        print(f"Weight: {row}")
        print()
        weight_str = row[1]
        weight_flt = float(weight_str.replace(" kg", ""))
        dates.append(n)
        weight.append(weight_flt)
        n +=1
weight.reverse()

# Plot the weight
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, weight, color='red', alpha=0.5)

# Format plot
ax.set_title("Weight, Oct 2024 - Oct 2025", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("rain", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
