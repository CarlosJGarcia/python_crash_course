import json
from pathlib import Path

"""
The remember_me.py example only stores one piece of information, the username.
Expand the example by asking for two more pieces of information about the user,
then store all the information you collect in a dictionary.
Write this dictionary to a file using json.dumps() and read it back using json.loads().
Print a summary showing exactly what your program remembers about the user.
"""

def greet_stored_username(file):
    """Get stored username if available."""
    if file.exists():
        contents = file.read_text()
        user = json.loads(contents)
        username = user['name']
        usercity = user['city']
        userage = user['age']
        return username, usercity, userage
    else:
        return None, None, None
    
def get_new_userdata(file):
    """Prompt for a new username."""
    username = input("What is your name?: ")
    usercity = input("Where do you live?: ")
    userage = input("How old are you?: ") 
    user = {'name': username, 'city': usercity, 'age': userage}
    contents = json.dumps(user)
    file.write_text(contents)
    return username, usercity, userage

def greet_user():
    """Greet the user by name."""
    file = Path('userdata.json')
    username, usercity, userage = greet_stored_username(file)
    
    if username:

        rep = input(f"Hello. Are you {username}? (y/n):")
        if rep == 'y':
            print(f"Welcome back, {username}!")
            print(f"You live in {usercity} and you are {userage} years old.")
        else:
            get_new_userdata(file)
    else:
        username, usercity, userage = get_new_userdata(file)
        print(f"We'll remember you when you come back, {username}")

greet_user()
