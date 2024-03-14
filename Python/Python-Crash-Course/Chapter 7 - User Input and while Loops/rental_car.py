# Rental Car

prompt = 'Enter a car you would like to rent: '
car = ''
while car != 'quit':
    car = input(prompt)

    if car != 'quit':
        print(f'Let me see if I can find you a {car}')