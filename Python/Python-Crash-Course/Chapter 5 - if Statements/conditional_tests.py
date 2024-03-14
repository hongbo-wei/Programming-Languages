# 5-1 Test whether the dream is boxing
# 5-1.1
dream = 'boxing'
print("Is dream equal to 'boxing'? I predict True.")
print(dream == 'boxing')
# 5-1.2
print("Is dream equal to 'working in Google'? I predict False.")
print(dream == 'working in Google')
# 5-1.3
print("Is dream equal to 'working in Microsoft'? I predict False.")
print(dream == 'working in Microsoft')
# 5-1.4
print("Is dream equal to 'working in Tesla'? I predict False.")
print(dream == 'working in Tesla')
# 5-1.5
dream = 'working in Space X'
print("Is dream equal to 'working in Space X'? I predict True.")
print(dream == 'working in Space X')
# 5-1.6
print("Is dream equal to 'working in Twitter'? I predict False.")
print(dream == 'working in Twitter')
# 5-1.7
print("Is dream equal to 'working in the G5 universities'? I predict False.")
print(dream == 'working in the G5 universities')
# 5-1.8
dream = 'make a living in the UK'
print("Is dream equal to 'make a living in the UK'? I predict True.")
print(dream == 'make a living in the UK')
# 5-1.9
dream = 'find a pretty blonde girlfriend'
print("Is dream equal to 'find a pretty blonde girlfriend'? I predict True.")
print(dream == 'find a pretty blonde girlfriend')
# 5-1.10
dream = 'be an excellent AI engineer'
print("Is dream equal to 'be an excellent AI engineer'? I predict True.")
print(dream == 'be an excellent AI engineer')
print('')

# 5-2 More Conditional Tests (for equality and inequality with strings)
print('5-2')
lover = 'blonde'
print(lover == 'blonde')
print(lover == 'black')
print('')
# Tests using the lower.() method
car = 'Lamborghini'
print(car.lower() == 'lamborghini')
print(car.lower() == 'audi')
print('')
# Numerical Tests
number = 1
print(number == 1)
print(number != 1)
print(number > 0)
print(number < 1)
print(number >= 1)
print(number <= 0)
print('')
# Tests using the and keyword and the or keyword
gender, age = 1, 19
print(gender == 1 and age == 19)
print(gender == 1 and age == 17)

print(gender == 1 or age == 17)
print(gender == 0 and age == 17)
print('')
# Test whether an item is in a list
boxing_punches = ['jab', 'overhand', 'hook', 'uppercut']
if 'kick' in boxing_punches:
    print(True)
else:
    print(False)

if 'uppercut' in boxing_punches:
    print(True)
print('')
# Test whether an item is not in a list
blonde = ['British', 'European', 'American']
print('Chinese' not in blonde)
print('British' not in blonde)
