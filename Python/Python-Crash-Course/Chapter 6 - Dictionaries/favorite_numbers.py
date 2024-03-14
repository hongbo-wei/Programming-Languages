# 6-2

favorite_number = {
    'Hongbo': 4,
    'Dragon': 9,
    'Hao': 3,
    'Bin': 1,
    'Ruyi': 6,
    }

print(f"Hongbo's favorite number is {favorite_number['Hongbo']}")
print(f"Dragon's favorite number is {favorite_number['Dragon']}")
print(f"Hao's favorite number is {favorite_number['Hao']}")
print(f"Bin's favorite number is {favorite_number['Bin']}")
print(f"Ruyi's favorite number is {favorite_number['Ruyi']}")

# 6-10 Favorite Numbers

favorite_number = {
    'Hongbo': [4, 6, 7, 9],
    'Hao': [3],
    'Bin': [1, 3],
    'Ruyi': [6, 8],
    }

for guy, numbers in favorite_number.items():
    if guy != 'Hao':
        print(f"\n{guy}'s favorite numbers are: ")
    else:
        print(f"\n{guy}'s favorite number is: ")
    for number in numbers:
        print(f'\t{number}')

