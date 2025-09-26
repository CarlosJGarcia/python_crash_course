from pathlib import Path

path = Path('cats.txt')
try:
    content = path.read_text()
except FileNotFoundError:
    pass
else:
    print(content)

path = Path('dogs.txt')
try:
    content = path.read_text()
except FileNotFoundError:
    pass
else:
    print(content)