import csv
from pathlib import Path
import plotly.express as px

# Read text (CSV file)
print("Reading file")
file = Path('eq_data/world_fires_7_day.csv')
lines = file.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)
# print(header_row)

# Extract dates and rainfoll
brightness, lons, lats = [], [], []
for row in reader:
    lat = float(row[0])
    lats.append(lat)
    lon = float(row[1])
    lons.append(lon)
    bri = float(row[2])
    brightness.append(bri)

    
# Representación gráfica
title = "World Fires"
fig = px.scatter_geo(lat=lats, lon=lons, size=brightness, color=brightness, projection='natural earth')
fig.show()

print("Program ends")
