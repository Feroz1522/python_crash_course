#exercise 6-7
user_1 ={
    'firstname':"mari",
    'lastname':"muthu",
    'age' :45,
    'city':'chennai'
     }
user_2 = {
        'firstname':"anwar",
        'lastname':"basha",
        'age':"20",
        'city':"chennai"
        }
user_3 = {
        'firstname':"danyal",
        'lastname':"raja",
        'age':"21",
        'city':'pondy'
        }

#list
people = [user_1,user_2,user_3]

for person in people:
    print(f"the person name is { person['firstname'] } { person['lastname']}")
    print("\t age is ",person['age'])
    print('\t city is ',person['city'])
    
