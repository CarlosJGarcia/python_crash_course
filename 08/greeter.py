"""
def saluda(nombre='defecto'):
    print(f"Hola {nombre.title()}!")

print("\nComienza el programa")
person = input("¿Como te llamas?: ")
saluda(person)
saluda()
print("Fin del programa.\n")
"""

"""
def define_animal(nombre, tipo = 'perro'):
    print(f"Tenemos un {tipo}")
    print(f"Este {tipo} se llama {nombre}\n")

print("\n")
define_animal("Capibara", "Pablo")
define_animal("Hamster", "Harry")
define_animal("Toby")
"""

def format_name(first_name, last_name, middle_name = ""):
    
    if middle_name:
        name = f"{first_name} {middle_name} {last_name}"
    else:
        name = f"{first_name} {last_name}"
    return name.title()

# Devuelve un diccionario con los datos de una persona
def build_person(first_name, last_name, age = None):
    person = {'first': first_name, 'last': last_name, 'age': age}
    return person

"""
print("\n")
musico = format_name("jimi", "hendrix")
print(musico)

musico = format_name("Carlos", "Garcia", "Javier")
print(musico)


diccionario = build_person("jimi", "hendrix")

for clave, valor in diccionario.items():
    if valor:
        print("-", valor)
"""

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = format_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")