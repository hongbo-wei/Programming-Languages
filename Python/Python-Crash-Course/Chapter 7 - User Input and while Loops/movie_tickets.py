# 7-5 Movie Tickets
# 7-6.3 Three Exits

while True:
    age = input('Enter your age or Enter quit: ')

    if age == 'quit':
        break

    if int(age) < 3:
        cost = 'free'

    elif int(age) >= 3 and int(age) <= 12:
        cost = '$10'

    elif int(age) > 12:
        cost = '$15'

    print(f'The cost of your movie ticket: {cost}')
