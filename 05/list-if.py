# Ejercicios con listas y if/elif/else
# 20/Jun/2025
# Ejecutar en VSCode para mac con ctrl+F5. En algunos teclados, para que funcione F5 hay que pulsar fn también

users = ['admin', 'cgarcia', 'eva', 'ali', 'best']
users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hola {user.title()}!")
else:
    print("We need to find some users!")


current_users = ['admin', 'cgarcia', 'eva', 'ali', 'best']
new_users = ['laura', 'pepe', 'Eva', 'Ali', 'jorge']

current_users_low = []
for current in current_users:
    current_users_low.append(current.lower())

#Loop through new_users to check if the user ids have been used
for new in new_users:
    if new.lower() in current_users_low:
        print(f"- The person {new} will have to enter a new username")
    else:
        print(f"- {new} is available")

numbers = []

for n in range(1,10):
    numbers.append(n)

for n in numbers:
    if n == 1:
        print(f"{n}st")
    elif n == 2:
        print(f"{n}nd")
    elif n == 3:
        print(f"{n}rd")
    else:
        print(f"{n}th")