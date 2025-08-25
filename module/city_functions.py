def get_city_country(city, country, population=0):
    city_country = f'{city}, {country}'.title()
    if population:
        return f'{city_country} - population {population}'
    else:
        return city_country
