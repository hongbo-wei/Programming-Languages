# 11-1 City, Country
# 11-2 Population (add population to city_country)


def call_city_country(city, country, population=''):
    city, country = city.title(), country.title()
    if population:
        call = f"{city}, {country} - population {population}"
    else:
        call = f"{city}, {country}"
    return call
