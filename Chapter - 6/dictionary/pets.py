#exercise 6-8
#list:
pets = []

#dictionary:
tommy = {
        'category':'cat',
        'owner':'ahmed',
        }
timmy = {
        'category':'cat',
        'owner':'feroz'
        }
orange = {
        'category':'cat',
        'owner':'rinald'
        }
#appending to list:
pets.append(tommy)
pets.append(timmy)
pets.append(orange)

for pet in pets:
    print("\ni am having ",pet["category"])
    print(f"the owner of the { pet['category']} is {pet['owner']}")
