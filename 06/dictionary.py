# Ejercicios con diccionarios
# 2/Jul/2025
# Ejecutar en VSCode para mac con ctrl+F5. En algunos teclados, para que funcione F5 hay que pulsar también fn

"""
# Ejercicio 6-4
fav_numbers = {'carlos': 42,
    'eva': 6,
    'ali': 10,
    'peter': 1,
    'paul': 2,
    'mary': 3,
    'ron': 4,
    'vecino': 5,
    }

print('Ejercicio 6-4. Listado de números favoritos:')
for key in fav_numbers.keys():
    nombre = key.title()
    numero = fav_numbers[key]
    print(f"{nombre}: {numero}")
"""

"""
# Ejercicio 6-5
rivers = {'tajo': 'portugal',
     'ebro': 'españa',
    'rin': 'suiza'
    }

print("\nEjercicio 6-5.")
print("Listado de frases:")
for key in rivers.keys():
    rio = key.title()
    pais = rivers[key].title()
    print(f"El {rio} pasa por {pais}")

print("\nListado de rios:")
for key in rivers.keys():
    print(key.title())

print("\nListado de paises:")
for key in rivers.keys():
    print(rivers[key].title())
"""
    
# Ejercicio 6-5
favorite_languages = {'carlos': 'spanish',
    "eva": "spanish",
    "ali": "german",
    "ron": "gato",
    "paul": "inglés",
    }

people_poll = ['peter', 'paul']
personas_languages = favorite_languages.keys()

for persona_poll in people_poll:
    if persona_poll in personas_languages:
        print (f"Gracias {persona_poll.title()} por completar la información")
    else:
        print(persona_poll.title(), "tienes que completar la información")