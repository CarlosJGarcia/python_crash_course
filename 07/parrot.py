prompt = "\nTell me something and I will repeat it back to you "
prompt += "or enter 'quit' to end the program: "

# Flag del buble principal
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        print("End of the program.\n")
        active = False
    else:
        print(message)    
