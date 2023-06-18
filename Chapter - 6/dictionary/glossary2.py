#exercise 6-3

meaning = {
        'print':'used for printing',
        'if':'used for choosing two dicitions',
        'for':'used for looping process',
        'dictionaries':'for dictionary',
        }
meaning['or'] = 'used to store choose the two condition'
meaning['and'] = 'both condition needed to be true'
meaning['jones'] = 'he is a good boy'
        
for key,values in meaning.items():
    print("\n key :",key)
    print("values :",values)

print('\n print = ',meaning['print'])
