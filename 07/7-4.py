prompt = "\nEnter the name of any pizza topping you want to have "
prompt += "and enter 'quit' to end: "


# Versión sencilla
"""
while True:
    topping = input(prompt)

    if topping == 'quit':
        print("Fin del programa.\n")
        break

    print (f"Añadido {topping}")
"""

# Versión con flag
active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        print("Fin del programa.\n")
        active = False
    else:
        print (f"Añadido {topping}")
