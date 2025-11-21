import requests
from operator import itemgetter

# Make a REST API call and check the response
# Hacker News - Current top articles

def get_articulos():

    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    headers ={'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    response_code = r.status_code
    response_list = r.json()

    print(f"Items devueltos: {len(response_list)}")

    articulos_dict = []
    for item in response_list[:3]:
        # Make a new API call for each submission
        url = f"https://hacker-news.firebaseio.com/v0/item/{item}.json"
        r = requests.get(url, headers=headers)
        response_code = r.status_code
        response_dict = r.json()
        # En response_dict tenemos el artículo
        articulo = {'title': response_dict['title'], 'comentarios': response_dict['descendants'], 'URL': response_dict['url']}
        articulos_dict.append(articulo)

    articulos_dict = sorted(articulos_dict, key=itemgetter('comentarios'), reverse=True)

    return articulos_dict, response_code, response_list

n = 1
articulos, response, list = get_articulos()

print()
print("* Primeros 3 artículos en Hacker News *")
print()
for item in articulos:
    print(f"Titulo #{n}: {item['title']}")
    print(f"Comentarios #{n}: {item['comentarios']}")
    print(f"URL #{n}: {item['URL']}")
    print()
    n +=1

print("Fin del programa.")