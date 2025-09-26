# Ejercicio de listas
# 10/Jun/2025

"""
lista = []

for n in range(8):
    print(f"2^{n}={2**n}")
    lista.append(2**n)
print("lista:", lista)
print("Menor valor en la lista:", min(lista))
print("Mayor valor en la lista:", max(lista))
print("Sumatorio de los valores:", sum(lista))

# Mismo código con "list comprehension"
potencias = [2**n for n in range(8)]
print("lista:", potencias)
"""

"""
lista_diezmillon = []
top = 10000000
for n in range (1, top+1):
    # print(n)
    lista_diezmillon.append(n)
# print(lista_diezmillon)
print("\nMax:", max(lista_diezmillon))
print("\nMin:", min(lista_diezmillon))
print("\nSuma:", sum(lista_diezmillon))
"""

"""
# Impares del 1 al 20
for n in range(3, 30+1, 3):
    print(n)
"""

for n in range (1, 11):
    print(f"{n}^3 = {n**3}")


lista = []
for n in range (1, 11):
    lista.append(n**3)
print(lista)

lista = [n**3 for n in range(1,11)]
print(lista)