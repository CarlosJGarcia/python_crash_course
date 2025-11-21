import requests
from operator import itemgetter
import plotly.express as px

# Make a REST API call and check the response
# Hacker News - Current top articles
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
headers ={'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
response_code = r.status_code
response_list = r.json()

articulos_dict = []
for item in response_list[:10]:
    # Make a new API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{item}.json"
    r = requests.get(url, headers=headers)
    response_code = r.status_code
    response_dict = r.json()
    # En response_dict tenemos el artículo
    articulo = {'title': response_dict['title'], 'comentarios': response_dict['descendants'], 'URL': response_dict['url']}
    articulos_dict.append(articulo)

articulos_dict = sorted(articulos_dict, key=itemgetter('comentarios'), reverse=True)

art_name, art_stars, art_hover_text = [], [], []
n = 1
print()
print("* Primeros 10 artículos en Hacker News *")
print()
for item in articulos_dict:
    print(f"Titulo #{n}: {item['title']}")
    art_name.append(item['title'])
    print(f"Comentarios #{n}: {item['comentarios']}")
    art_stars.append(item['comentarios'])
    print(f"URL #{n}: {item['URL']}")
    art_hover_text.append(item['URL'])
    print()
    n +=1

print(art_hover_text)

# Visualization
title = "Most starred Github Python repositories"
labels = {'x': 'Repository', 'y': "Stars"}
# fig = px.bar(x=art_name, y=art_stars, title=title, labels=labels, hover_name=art_hover_text)
fig = px.bar(x=art_name, y=art_stars, title=title, labels=labels, hover_name=art_hover_text)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='Steelblue', marker_opacity=0.6)
fig.show()

print("Fin del programa.")