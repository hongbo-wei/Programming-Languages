# 10-1 Learning Python

from pathlib import Path

path = Path('learning_python.txt')
lines = path.read_text().splitlines()

sentences = []
for line in lines:
    print(line)
    for sentence in sentences:
        if line == sentence:
            print('\nThis sentence appears twice in the file:')
            print(f'{sentence}')

    # Make sure we only append a sentence once.
    # If the same sentence appears, we don't append it to sentences.
    if line not in sentences:
        sentences.append(line)
