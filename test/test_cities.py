from module.city_functions import get_city_country


def test_city_country_population():
    city_country = get_city_country('santiago', 'chile', '5000000')
    assert city_country == 'Santiago, Chile - population 5000000'
