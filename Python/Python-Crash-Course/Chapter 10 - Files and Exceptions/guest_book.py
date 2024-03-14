# 10-5 Guest Book

from pathlib import Path

guests = ''
while True:
    guest = input('Enter your name or press enter to quit: ')
    if len(guest) < 1:
        break

    guests += guest + '\n'


path = Path('guest_book.txt')
path.write_text(guests)

