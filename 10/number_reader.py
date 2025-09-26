import json
from pathlib import Path



file = Path('numbers.json')
contents = file.read_text()
numbers = json.loads(contents)
for number in numbers:
	print(f"- {number}")


