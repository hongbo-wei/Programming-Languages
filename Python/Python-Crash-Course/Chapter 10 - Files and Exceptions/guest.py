# 10-4 Guest (Write text to a file)

from pathlib import Path

guest = input('Enter your name: ')

path = Path('guest.txt')
path.write_text(guest)

