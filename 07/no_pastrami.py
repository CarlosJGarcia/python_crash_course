
# Defino dos listas
finished_sandwiches = []
sandwich_orders = ['club', 'pastrami', 'mixto', 'pastrami', 'emparedado', 'pastrami', 'atún con tomate']

print("Warning: The deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the list of sandwich orders
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("\nLista de todos los sandwiches que hemos hecho:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")
