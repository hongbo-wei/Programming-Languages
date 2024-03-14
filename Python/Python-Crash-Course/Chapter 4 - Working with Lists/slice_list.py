# 4-10 Slice
pizzas = ['pizza capricciosa', 'Pizza Margherita', 'Hawaiian Pizza', 'Pepperoni Pizza', 'Seafood Pizza']
print('The first three items in the lists are: ')
for pizza in pizzas[:3]:
    print(pizza)

print('\nThree items from the middle of the list are: ')
for pizza in pizzas[1:4]:
    print(pizza)

print('\nThe last three items in the lists are: ')
for pizza in pizzas[-3:]:
    print(pizza)

# 4-11 Your Pizzas, My Pizzas
friend_pizzas = pizzas[:]
pizzas.append('Beef Pizza')
friend_pizzas.append('Mushroom Pizza')
print('\nMy favorite pizzas are: ')
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)