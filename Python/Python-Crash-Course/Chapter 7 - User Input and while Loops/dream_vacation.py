# 7-10 Dream Vacation

dream_vacation = {}
while True:
    name = input('\nEnter your name: ')
    vacation = input('What is your dream vacation: ')

    dream_vacation[name] = vacation

    repeat = input('Would you like another record of dream vacation? (yes/no) ')
    if repeat == 'no':
        break

print('\n--- Poll Results ---')
for name, vacation in dream_vacation.items():
    print(f"{name} would like to {vacation}")