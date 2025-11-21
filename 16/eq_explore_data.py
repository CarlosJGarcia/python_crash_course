import json
from pathlib import Path
import plotly.express as px

# Read text (JSON file)
print("Reading JSON")
#file = Path('eq_data/eq_1_day_m1.geojson')
file = Path('eq_data/eq_30_day_m1.geojson')
content = file.read_text(encoding='utf-8')

# Convert to a python object
all_eq_data = json.loads(content)

# Create a more readable version 
readable_contents = json.dumps(all_eq_data, indent=4)

# Write to a file (JSON) that is more readable
print("Writing JSON")
file = Path('eq_data/readable_eq_data.geojson')
file.write_text(readable_contents)

# Examine all the earthquakes in the dataset. Get the data associated to key 'features'
all_eq_dicts = all_eq_data['features']
print(f"Number of earthquakes: {len(all_eq_dicts)}")

# Creo una listas con todas las magnitudes y coordenadas (latitud, longitud)
mags, lons, lats, titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    lons.append(lon)
    lats.append(lat)
    title = eq_dict['properties']['title']
    titles.append(title)
print(f"Las 10 primeras magnitudes: {mags[:10]}")
print(f"Las 5 primeras logitudes: {lons[:5]}")
print(f"Las 5 primeras latitudes: {lats[:5]}")

# Representación gráfica
title = "Global Earthquakes"
fig = px.scatter_geo(lat=lats, lon=lons, title=title, size=mags, color=mags, hover_name=titles, projection='natural earth')
fig.show()

print("Program ends")
