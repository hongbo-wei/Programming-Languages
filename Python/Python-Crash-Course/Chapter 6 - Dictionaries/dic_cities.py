# 6-11 Cities

cities = {
    'Guiyang': {
        'country': 'China',
        'population': '10 million',
        'fact': 'cool in summer',
    },
    'London': {
        'country': 'the UK',
        'population': '100 million',
        'fact': 'where money and beauty gathers'
    },
    'Los Angels': {
        'country': 'the US',
        'population': '99 million',
        'fact': 'where most celebrities live in'
    }
}

for city, city_info in cities.items():
    print(city)
    for info, detail in city_info.items():
        print(f'\t{info.title()}: {detail}')

# 6-12 Extensions
cities['Hangzhou'] = {
    'country': 'China',
    'population': '88 million',
    'fact': 'where poets love'
}

for city, city_info in cities.items():
    print(f"\n{city} is in {city_info['country']},"
          f"has about {city_info['population']} people,"
          f"and is {city_info['fact']}")
