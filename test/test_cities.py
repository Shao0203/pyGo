from module.city_functions import get_city_country


def test_city_country():
    city_country = get_city_country('dalian', 'china')
    assert city_country == 'Dalian, China'


def test_city_country_population():
    cc_pop = get_city_country('santiago', 'chile', 5000000)
    assert cc_pop == 'Santiago, Chile - population 5000000'
