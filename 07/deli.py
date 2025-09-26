
# Defino dos listas
finished_sandwiches = []
sandwich_orders = ['club', 'mixto', 'emparedado', 'atún con tomate']

# Loop through the list of sandwich orders
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("\nLista de todos los sandwiches que hemos hecho:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")
