# 7-4 Pizza Toppings
# 7-6.1 Three Exits

pizza_toppings = []

active = True
while active:
    topping = input('Enter a pizza topping or quit: ')

    if topping == 'quit':
        active = False
        continue

    pizza_toppings.append(topping)
    print(f'{topping} has been added to your pizza\n')

print(pizza_toppings)

# 7-6.2 Three Exits
pizza_toppings = []

times = 0
while times < 4:
    topping = input('Enter a pizza topping or quit: ')
    pizza_toppings.append(topping)
    print(f'{topping} has been added to your pizza\n')
    times += 1

print(pizza_toppings)