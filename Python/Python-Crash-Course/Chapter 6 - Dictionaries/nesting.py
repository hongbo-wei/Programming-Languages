# 6-8 Pets

dog = {
    'name': 'Dingding',
    'kind': 'dog',
    'owner': 'Hongbo',
}

cat = {
    'name': 'Panther',
    'kind': 'cat',
    'owner': 'Tyson',
}

bird = {
    'name': 'Phill',
    'kind': 'phenix',
    'owner': 'Jesus',
}

pets = [dog, cat, bird]

for pet in pets:
    print(f"{pet['owner']} has a {pet['kind']} called {pet['name']}")
