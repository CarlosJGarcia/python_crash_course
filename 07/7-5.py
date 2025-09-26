prompt = "\nEnter your age and I'll tell you the ticket price. "
prompt += "Enter 'quit' to end: "

while True:
    age = input(prompt)

    if age == 'quit':
        print("Fin del programa.\n")
        break
    else:
        age = int(age)
        if age <= 3:
            print (f"For {age} years old, entrance is free!")
        elif age <= 12:
            print (f"For {age} years old, entrance is $10")
        else:
            print (f"For {age} years old, entrance is $12")
    