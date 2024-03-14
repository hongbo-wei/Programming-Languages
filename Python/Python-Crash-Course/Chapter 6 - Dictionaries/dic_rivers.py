# 6-5

rivers = {'nile': 'egypt', 'river thames': 'England', 'river bei tang': 'China'}

print('6-5.1')
for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')
    print(f'The river is {river.title()}')
    print(f'The country is {country.title()}')

print('\n6-5.2')
for river in rivers: # also river.keys()
    print(f'The river is {river.title()}')

print('\n6-5.3')
for country in rivers.values():
    print(f'The country is {country.title()}')