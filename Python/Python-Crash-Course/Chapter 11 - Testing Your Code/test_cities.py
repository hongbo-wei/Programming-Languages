from city_functions import call_city_country


def test_city_country():
    """Does cities like Santiago, Chile work?"""
    formatted_city = call_city_country('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'


def test_city_country_population():
    """Does adding third parameter work?"""
    formatted_population = call_city_country('santiago', 'chile', '5000000')
    assert formatted_population == 'Santiago, Chile - population 5000000'
