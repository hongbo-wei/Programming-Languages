# 6-1

dic_person = {
    'first name':'Lewis',
    'last name': 'Jones',
    'age': '26',
    'city': 'Zurich'
    }

# How to print one line when writing multiple lines in print() function.
print(f"{dic_person['first name']} {dic_person['last name']} is a "
      f"{dic_person['age']}-year-old male doing a PhD "
      f"programme in {dic_person['city']}")

# Add new key-value pairs
dic_person['hobby'] = 'music'
print(dic_person)

# Modify value:
dic_person['hobby'] = 'hiking'
print(dic_person)

# Delete key-value pairs
del dic_person['hobby']
print(dic_person)

# 6-7 People

dic_boxer = {
    'Canelo': 'Mexican',
    'Pacquiao': 'Filipino',
    'Mayweather': 'American',
    'Ali': 'African',
}

dic_coach = {
    'Sainaa': 'Mongolian',
    'Nonoy': 'Filipino',
    'Rob': 'Filipino',
    'Yuan': 'Chinese',
}

list_people = [dic_coach, dic_boxer, dic_person]
print('6-7')
for group in list_people:
    if group == dic_person:
        print(f"{dic_person['first name']} {dic_person['last name']} is a "
              f"{dic_person['age']}-year-old male doing a PhD "
              f"programme in {dic_person['city']}")
    else:
        for guy in group:
            print(f"{guy} is {group[guy]}")
