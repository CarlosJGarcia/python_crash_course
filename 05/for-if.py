# Ejercicio de imprimir una lista + uso de if/then
# 16/Jun/2025

coches = ["audi", "bmw", "Volkswagen", "renault"]

print("\nInicio del programa.")
for coche in coches:
    
    if coche == "bmw":
        print(coche.upper())
    else:
        print(coche.title())
print()

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

print("Fin del programa.\n")
