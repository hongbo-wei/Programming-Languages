# 10-8
# 10-9 Silent Cats and Dogs: make 10-8 fail silently

from pathlib import Path

path_cats = Path('cats.txt')
# Absolute Path: D:/Users/Champ/PycharmProjects/pythonProject/python_work/dogs.txt
path_dogs = Path('dogs.txt')

try:
    contents_cats = path_cats.read_text()
    contents_dogs = path_dogs.read_text()

except FileNotFoundError:
    # print('Please double-check the location of the file')
    pass

else:
    for cat in contents_cats.splitlines():
        print(cat)

    for dog in contents_dogs.splitlines():
        print(dog)