#exercise 6-9
favorite_places = {
    'feroz':['goa','turkey','korea'],
    'anwar':['america','france','italy'],
    'arjun':['india','germany','asia']
    }

for name,places in favorite_places.items() :
    print(f"\nHi! i am {name}")
    print("your favorite places are :")
    for place in places :
        print("\t -"+place)

