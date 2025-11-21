import requests

# Make a REST API call and check the response
# Github - list all python repositories, sorted by amount of stars
url = 'https://api.github.com/search/repositories?q=language=python+sort:stars'

headers ={'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
response_code = r.status_code
response_dict = r.json()
print()
print("* GitHub query *")
print(f"Petición: {url}")
print(f"Respuesta - status code: {response_code}")
print(f"Respuesta - claves del diccionario: {response_dict.keys()}")

# Work with the response, 1st level
print(f"Datos: Número de repositorios python en GitHub: {response_dict['total_count']}")
print(f"Datos: Complete results: {not response_dict['incomplete_results']}")
repo_dicts = response_dict['items']
print(f"Datos: Número de resultados recibidos: {len(repo_dicts)}")

# Work with the response, 2nd level
n = 0
repo_dict = repo_dicts[0]
print("Información de cada repositorio:")
for key in sorted(repo_dict.keys()):
    n += 1
    print(f"  {n:02d} : {key}")
    
# Selected information about the first repository
print()
print("Selected information about the first repository")
print(f"- Name: {repo_dict['name']}")
print(f"- Stars: {repo_dict['stargazers_count']}")
print(f"- Repository: {repo_dict['html_url']}")
print(f"- Description: {repo_dict['description'][:80]}")
print(f"- Created: {repo_dict['created_at']}")
print(f"- Updated: {repo_dict['updated_at']}")
                  
# More selected information about the first 10 repositories
print()
print("First 10 python Github repositories:")
print()
n = 0
for repo_dict in repo_dicts:
    n = n+1
    if n <= 10:
        print(f"Number {n}")
        print(f"- Name: {repo_dict['name']}")
        print(f"- Stars: {repo_dict['stargazers_count']}")
        print(f"- Description: {repo_dict['description'][:100]}")
        print(f"- URL: {repo_dict['html_url']}")
        print()

print("Fin del programa")
print()