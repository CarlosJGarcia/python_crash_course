import json
from pathlib import Path

"""
Write a program that prompts for the user's favorite number.
Use json.dumps() to store this number in a file
"""

file = Path('10-11.json')

number = input("Please enter your favorite number: ")
contents = json.dumps(number)
file.write_text(contents)