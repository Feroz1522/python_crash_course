#exercise 6-12
cities = { 
    'chennai':{'country':'india','fact':'famous for information technology','population':'1234567'},
    'bangalore':{'country':'india','fact':'electronic city of india ','population':'14654564654'},
    'delhi':{'country':'india','fact':'tajmahal  has been constructed there ','population':'1654564'}
    }

for city,info in cities.items():
    print(f'\nwe gonna see about {city} ')
    
    coun_try = info['country']
    f_ct = info['fact']
    pop = info['population']

    print(f"this city is located in the country {coun_try}")
    print(f"current population of this city is { pop}")
    print(f"this city is famous for {f_ct}")
