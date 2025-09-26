import json
from pathlib import Path

file = Path('username.json')
contents = file.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}")
