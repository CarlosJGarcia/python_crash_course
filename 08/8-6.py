"""
def city_country(city, country):
    cadena = f"{city.title()}, {country.title()}"
    return cadena

valor = city_country("Madrid", "España")
print(valor)

valor = city_country("Bern", "Schweiz")
print(valor)

valor = city_country("Paris", "France")
print(valor)
"""

def make_album(artist_name, album_title, number_songs = None):
    album = {'artist': artist_name, 'title': album_title}

    if number_songs:
        album.update({'songs': number_songs})

    return album


dict = make_album("Héroes del Silencio", "El mar no cesa")
for clave, valor in dict.items():
    print(clave, "-->", valor)

dict = make_album("Nirvana", "Nevermind")
for clave, valor in dict.items():
    print(clave, "-->", valor)

dict = make_album("REM", "Out of time")
for clave, valor in dict.items():
    print(clave, "-->", valor)    

dict = make_album("Pink Floid", "Animals", 6)
for clave, valor in dict.items():
    print(clave, "-->", valor)    

while True:
    print("\nType an album's artist and title")
    print("(enter 'q' at any time to quit)")

    band = input("Album's artist: ")
    if band == 'q':
        break

    title = input("Album's title: ")
    if title == 'q':
        break

    dict = make_album(band, title)
    for clave, valor in dict.items():
        print(clave, "-->", valor)    
