#exercise 5-6
print("enter your age:")
age = int(input(">>"))

if (age < 2):
    print("you are a baby")
elif (age < 4):
    print("you are a toddler")
elif (age < 13):
    print("you are a kid")
elif (age < 20):
    print("you are a teenager")
elif (age < 65):
    print("you are a adult")
else: 
    print("thank you for checking here ")
