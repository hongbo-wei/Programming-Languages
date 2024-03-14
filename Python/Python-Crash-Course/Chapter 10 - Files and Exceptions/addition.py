# 10-6
# 10-7 Wrap 10-6 in a while loop

while True:
    print('\nEnter two number, and I will add them. Or quit:')
    number_1 = input('Enter the first number: ')
    if number_1 == 'quit': break
    try:
        value_1 = float(number_1)

    except ValueError:
        print('Input value is not a number')

    number_2 = input('Enter the second number: ')
    if number_2 == 'quit': break

    try:
        value_2 = float(number_2)

    except ValueError:
        print('Input value is not a number')

    else:
        sum = value_1 + value_2
        print(sum)
