""" 16-2 Data Science Sitka / Death Valley Comparison """
# Muestra un gráfico de intervalos de temperatura altas / bajas para
# death_valley_2021_simple.csv
# sitka_weather_2021_simple.csv

import csv
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt

def f2c(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

sk_path = Path('weather_data/sitka_weather_2021_simple.csv')
sk_lines = sk_path.read_text(encoding='utf-8').splitlines()

sk_reader = csv.reader(sk_lines)
sk_header_row = next(sk_reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)
for index, column_header in enumerate(sk_header_row):
    print(index, column_header)

# Death 2 DATE, 3 TMAX, 4 TMIN
# Sitka 2 DATE 4 TMAX 5 TMIN

# Extract dates, high and low temperatures
sk_dates, sk_highs, sk_lows = [], [], []
for row in sk_reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')

    try:
        high_f = int(row[4])
        low_f = int(row[5])
        high_c = f2c(high_f)
        low_c = f2c(low_f)
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        sk_dates.append(current_date)
        sk_highs.append(high_c)
        sk_lows.append(low_c)

# Extract dates, high and low temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')

    try:
        high_f = int(row[3])
        low_f = int(row[4])
        high_c = f2c(high_f)
        low_c = f2c(low_f)
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high_c)
        lows.append(low_c)

# Plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='red', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

ax.plot(sk_dates, sk_highs, color='blue', alpha=0.5)
ax.plot(sk_dates, sk_lows, color='blue', alpha=0.5)
ax.fill_between(sk_dates, sk_highs, sk_lows, facecolor='yellow', alpha=0.1)


# Format plot
ax.set_title("Death Valley and Sitka daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)", fontsize=16)
ax.tick_params(labelsize=16)

# Toggles full-screen mode
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()  

plt.show()
