# 4-13 Buffet

buffet_menu = ('bacon', 'spaghetti', 'milk', 'fried rice', 'eggs')

print('The initial menu contains:')
for food in buffet_menu:
    print(food)

# If you try to assign a new value to one of tuple's element, you get an error:
# "'tuple' object does not support item assignment"
# buffet_menu[0] = ['pizza']

buffet_menu = ('steak', 'spaghetti', 'milk', 'salad', 'eggs')

print('\nThe revised menu contains:')
for food in buffet_menu:
    print(food)