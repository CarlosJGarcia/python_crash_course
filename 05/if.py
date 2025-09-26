# Ejercicios con if/elif/else
# 18/Jun/2025
# Ejecutar en VSCode para mac con ctrl+F5. En algunos teclados, para que funcione F5 hay que pulsar fn también

age = 56
alien_color = 'red'
# alien_color = 'green'
# alien_color = 'yellow'
favorite_fruits = ['apple', 'grapes', 'banana', 'peach', 'melon']

print("Exercise 3.")
if alien_color == 'green':
    print("Condition type 1: The player has earned 5 points.")
if alien_color != 'red' and alien_color !='yellow':
    print("Condition type 2: The player has earned 5 points.")

print("Exercise 4.")
if alien_color == 'green':
    print("Condition type 1: The player has earned 5 points.")
else:
    print("Condition type 1: The player has earned 10 points.")
if alien_color != 'red' and alien_color !='yellow':
    print("Condition type 2: The player has earned 5 points.")
else:
    print("Condition type 2: The player has earned 10 points.")

print("Exercise 5.")
if alien_color == 'green':
    print("Condition type 1: The player has earned 5 points.")
if alien_color == 'yellow':
    print("Condition type 1: The player has earned 10 points.")
if alien_color == 'red':
    print("Condition type 1: The player has earned 15 points.")
if alien_color != 'red' and alien_color !='yellow':
    print("Condition type 2: The player has earned 5 points.")
if alien_color != 'red' and alien_color !='green':
    print("Condition type 2: The player has earned 10 points.")
if alien_color != 'green' and alien_color !='yellow':
    print("Condition type 2: The player has earned 15 points.")
if alien_color == 'green':
    print("Condition type 3: The player has earned 5 points.")
elif alien_color == 'yellow':
    print("Condition type 3: The player has earned 10 points.")
elif alien_color == 'red':
    print("Condition type 3: The player has earned 15 points.")

print("Exercise 6.")
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
elif age >= 65:
    print("The person is an elder.")

print("Exercise 7.")
if favorite_fruits:
    for fruit in favorite_fruits:
        print(f"Checking {fruit}")
        if fruit == 'apple':
            print ("You really like apples!")
        if fruit == 'banana':
            print ("You really like bananas!")
        if fruit == 'peach':
            print ("You really like peaches!")
else:
    print("No me gusta la fruta.")

print("Fin del programa.\n")
