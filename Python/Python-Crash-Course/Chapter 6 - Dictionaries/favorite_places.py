# 6-9 Favorite Places

favorite_places = {
    'Hongbo': {
        'country': 'UK',
        'city': 'Scarborough',
        'type': 'costal city',
    },
    'Lewis': {
        'country': 'Switzerland',
        'city': 'Zurich',
        'type': 'mountainous area'
    },
    'Joey': {
        'country': 'US',
        'city': 'Los Angels',
        'type': 'costal city'
    }
}

for guy, place in favorite_places.items():
    print(f"\n{guy}'s favorite place is: ")
    print(f"\tCountry: {place['country']}")
    print(f"\tCity: {place['city']}")
    print(f"\tType: {place['type'].title()}")
