from pathlib import Path

''' 10-3 Simpler Code: Remove temporary variables '''

for line in Path('learning_python.txt').read_text().splitlines():
    print(line)
