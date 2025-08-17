def get_city_country(city, country, population=0):
    if population:
        city_country = f'{city.title()}, {country.title()} - population {population}'
    else:
        city_country = f'{city.title()}, {country.title()}'
    return city_country
