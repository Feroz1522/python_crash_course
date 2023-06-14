#Exercise 5-1

#method_1
car = ['bmw','ford','tata','supra','mercedes','audi']
input_data = 'rollsroyce'

if input_data in car :
    print('your car is in our collection')
if input_data not in car :
    print('your car is not in our collection ')

#method_2
bikes = 'ducati'

print( bikes == 'ducati')
print( bikes == 'kawasaki')

#method_3
animals = ['tiger','cheetah','leopard','lion']

print('tiger' in animals)
print('rat'not in animals)

#method_4
if 'leopard' in animals :
    print("yeah! leopard is from cat family")
if 'racoon' not in animals :
    print("this is not from cat family")

