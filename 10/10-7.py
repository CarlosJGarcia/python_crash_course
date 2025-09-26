
condicion = True

while condicion:
    a = input("Dime un número o 'q' para salir: ")
    if a == "q":
        condicion = False
        break

    b = input("Dime otro número o 'q' para salir: ")
    if b == 'q':
        condicion = False
        break

    try: 
        a = int(a)
        b = int(b)
    except ValueError:
        print("Solo valores numéricos!")
    else:
        print(f"La suma es {a + b}")