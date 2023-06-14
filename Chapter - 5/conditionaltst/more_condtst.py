#string test
a = "hi i'm jack"

print( a == "hi i'm jack")
print( a != "hi i'm jack")

#test using lower()
x = 'Supra'

print( x == 'supra')
print( x.lower() == 'supra')

#test using numerical values
age = 16

if (age < 18):
    print("you are not eligible for voting")
print( 10 > age )

#testing using list
family = ['mom','dad','son','grandma','grandpa']

print('\n first if')
if 'mom' in family:
    print("yeah they were our family")

a = 10
b = 43
if  a and b  <30 :
    print("the value is lesser than 30 ")
else:
    print("your value is smaller")

#test using list
list = ['hi','see you ','thankyou']
n_usr = input('>')

if n_usr in list:
    print("user is already")
else: 
    list.append(n_usr)  
    print("account has been created successfully")
print(list)

if "hi" in list:
    print("\n hi is in the list")
if "hello" not in list:
    print("\n hello is not in the list")
