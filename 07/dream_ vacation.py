# Defino un diccionario vacío
responses = {}

polling_active = True
while polling_active: 

    # Prompt for the person's name and response
    name = input("\nWhat is your name?: ")
    response = input("If you could visit one place in the world, where would you go?: ")

    # Store the response in the dictonary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Whould you like to let anyone alse to respond? (yes/no): ")
    if repeat == "no":
        polling_active = False

# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to go to {response}")