"""
# Defino dos listas
confirmed_users = []
unconfirmed_users = ['alice', 'brian', 'pedrito']

# Revisa cada usuario y lo mueve a la lista de confirmados
while unconfirmed_users:
    user = unconfirmed_users.pop()

    print(f"Verifying user: {user.title()}")
    confirmed_users.append(user)

# Muestro la lista de usuario confirmados
for user in confirmed_users:
    print(f"User: {user.title()}")



pets = ['dog', 'cat', 'dog', 'pez dorado', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

"""

# Defino un diccionario vacío
responses = {}

polling_active = True
while polling_active: 

    # Prompt for the person's name and response
    name = input("\nWhat is your name?: ")
    response = input("Which mountain would you like to climb someday?: ")

    # Store the response in the dictonary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Whould you like to let anyone alse to respond? (yes/no): ")
    if repeat == "no":
        polling_active = False

# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")