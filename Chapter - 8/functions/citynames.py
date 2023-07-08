def city_country(city,country):
    """ Combining the city and country names """
    combo = '"' + city + ' , ' + country +'"'
    return combo

dm_1 = city_country('chennai','india')
dm_2 = city_country('madurai','india')
dm_3 = city_country('delhi','india')

# it will print the the return values
print(dm_1 + ',' + dm_2 + ',' + dm_3)

