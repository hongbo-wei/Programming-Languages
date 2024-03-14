# 10-11
# 10-12 Favorite Number Remembered

import json
from pathlib import Path

path = Path('favorite_numbers.json')
if path.exists():
    content = path.read_text()
    print(json.loads(content))

else:
    favorite_number = input('Enter your favorite number: ')
    content = json.dumps(favorite_number)

    path = Path('favorite_numbers.json')
    path.write_text(content)


