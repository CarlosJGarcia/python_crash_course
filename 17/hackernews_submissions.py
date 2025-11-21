import json
import requests

# Make a REST API call and check the response
# Hacker News - Current top article

url = 'https://hacker-news.firebaseio.com/v0/item/31353677.json'
headers ={'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
response_code = r.status_code
response_dict = r.json()

print()
print("* Hacker News query *")
print(f"Petición: {url}")
print(f"Respuesta - status code: {response_code}")
print(f"Respuesta - claves del diccionario: {response_dict.keys()}")

print()
print(f"Título del artículo principal: {response_dict['title']}")
print(f"Número de comentarios: {response_dict['descendants']}")
print(f"Enlace (URL): {response_dict['url']}")

print()

response_string = json.dumps(response_dict, indent=4)
print(response_string)
