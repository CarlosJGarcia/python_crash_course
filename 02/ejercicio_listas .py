# Ejercicio de listas, pag 41 02/Jun/2025

invitados = ["Juan de la cierva", "Nigel Mansell", "Juan Rulfo"]

print()
print (f"Hola {invitados[0]}, le invito a cenar a casa.")
print (f"Hi {invitados[1]}, I invite you to dinner at home.")
print (f"Hola {invitados[2]}, le invito a cenar a casa.")
print()
print (f"{invitados[0]} no puede venir a cenar.")
invitados[0]="Peter Parker"
print (f"Hola {invitados[0]}, le invito a cenar a casa.")
print (f"Hi {invitados[1]}, I invite you to dinner at home.")
print (f"Hola {invitados[2]}, le invito a cenar a casa.")
print()
print("He comprado una mesa más grande, así que podemos aumentar el número de invitados")
invitados.insert(0, "Godzilla")
invitados.insert(2, "Rana Gustavo")
invitados.append("Andrés Castillo")
print (f"Hola {invitados[0]}, te invito a cenar a casa.")
print (f"Hola {invitados[1]}, le invito a cenar a casa.")
print (f"Hi {invitados[2]}, I invite you to dinner at home.")
print (f"Hola {invitados[3]}, le invito a cenar a casa.")
print (f"Hola {invitados[4]}, te invito a cenar a casa.")
print (f"Hola {invitados[5]}, te invito a cenar a casa.")
print()
print("Lamentablemente, solo hay espacio para dos invitados")
print(f"{invitados.pop()}, lamento cancelar la invitación ")
print(f"{invitados.pop()}, lamento cancelar la invitación ")
print(f"{invitados.pop()}, lamento cancelar la invitación ")
print(f"{invitados.pop()}, lamento cancelar la invitación ")
print (f"Hola {invitados[0]}, sigues invitado a cenar en casa.")
print (f"Hola {invitados[1]}, sigue invitado a cenar en casa.")
print()
del invitados[1]
del invitados[0]
print("Lista:", invitados)
print()

