# 7-8 Deli (abbreviation for delicatessen)

sandwich_orders = ['tuna', 'bacon', 'roasted beef', 'pepperoni']
finished_sandwiches = []

while sandwich_orders:
    finished = sandwich_orders.pop()
    finished_sandwiches.append(finished)
    print(f'I have made you a {finished} sandwich')

print('\nThe following sandwiches have been made:')
for sandwich in finished_sandwiches:
    print(sandwich)


# 7-9 No Pastrami (clear solution, better one)

sandwich_orders = ['tuna', 'pastrami', 'bacon', 'pastrami', 'roasted beef',
                   'pepperoni', 'pastrami']

print('\n(7-9) We, Deli, have run out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print('\nThe following sandwiches have been made:')
for sandwich in sandwich_orders:
    print(sandwich)


# 7-9 long solution
sandwich_orders = ['tuna', 'pastrami', 'bacon', 'pastrami', 'roasted beef',
                   'pepperoni', 'pastrami']
finished_sandwiches = []

print('\nWe, Deli, have run out of pastrami')
while sandwich_orders:
    finished = sandwich_orders.pop()
    if finished == 'pastrami':
        continue

    finished_sandwiches.append(finished)

print('\nThe following sandwiches have been made:')
for sandwich in finished_sandwiches:
    print(sandwich)