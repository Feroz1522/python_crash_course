rivers = {'nile':'egypt',
        'amazon river':'brazil',
        'brahmaputra':'china'
        }

for river,country in rivers.items():
    print(river + " through "+country)

for river in rivers.keys():
    print('the one of the major river is ',river)

for country in rivers.values():
    print("the major country of the river flow is ",country)
