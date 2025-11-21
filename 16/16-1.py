import csv
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime

def f2c(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

path = Path("weather_data/sitka_weather_2021_full.csv")
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

print(header_row)

# Extract dates and rainfoll
dates, rain = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    print(row[5])
    current_rain = float(row[5])
    dates.append(current_date)
    rain.append(current_rain)

# Plot the rain
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rain, color='red', alpha=0.5)


# Format plot
ax.set_title("Daily rain, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("rain", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()