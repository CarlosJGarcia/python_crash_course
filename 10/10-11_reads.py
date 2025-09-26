import json
from pathlib import Path

"""
Write a program that prompts for the user's favorite number.
Use json.dumps() to store this number in a file
"""

file = Path('10-11.json')
contents = file.read_text()
number = json.loads(contents)
print(f"I know your favorite number. It is {number}.")