import json
from pathlib import Path


numbers = [2, 3, 5, 7, 11, 13]

file = Path('numbers.json')
contents = json.dumps(numbers)
file.write_text(contents)


