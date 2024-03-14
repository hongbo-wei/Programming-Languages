# 10-2 Learning C

from pathlib import Path

path = Path('learning_python.txt')
lines = path.read_text().splitlines()

sentences = []
for line in lines:
    sentences.append(line.replace('Python', 'C'))
    # The function 'replace()' will not modify the original file but store the modification in memory
    print(line)

print('')
for sentence in sentences:
    print(sentence)

