prompt = "\nPlease enter the name of a city you have visited "
prompt += "or enter 'quit' to end the program: "

# Bucle infinito, uso break para salir
while True:
    city = input(prompt)

    if city == 'quit':
        print("End of the program.\n")
        break
    else:
        print(f"I'd love to go to {city.title()}")