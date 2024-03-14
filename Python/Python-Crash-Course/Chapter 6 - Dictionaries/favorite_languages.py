# 6-6 polling

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

poll_list = ['hongbo', 'sarah', 'lewis']

for person in poll_list:
    if person in favorite_languages.keys():
        print(f'Thank {person.title()} for taking the poll')
    else:
        print(f'{person.title()} please take the poll')

# knowledge about 'set' unique value
people = {'hongbo', 'hongbo', 'lewis'}
# = {'hongbo', 'lewis'}
print(people)
