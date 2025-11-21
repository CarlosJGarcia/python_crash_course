import json
from pathlib import Path
import plotly.express as px

# Read text (JSON file)
print("Reading JSON")
#file = Path('eq_data/eq_30_day_m1.geojson')
file = Path('eq_data/significant_month.geojson')
content = file.read_text(encoding='utf-8')

# Convert to a python object
all_eq_data = json.loads(content)

# title = all_eq_data['metadata']['title']
# print(title)

# Examine all the earthquakes in the dataset. Get the data associated to key 'features'
all_eq_dicts = all_eq_data['features']

# Creo una listas con todas las magnitudes y coordenadas (latitud, longitud)
mags, lons, lats, titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    titles.append(eq_dict['properties']['title'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    
# Representación gráfica
title = all_eq_data['metadata']['title']
fig = px.scatter_geo(lat=lats, lon=lons, title=title, size=mags, color=mags, hover_name=titles, projection='natural earth')
fig.show()

print("Program ends")
