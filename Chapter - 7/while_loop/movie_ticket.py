print("enter your age")
while True:
    age = int(input(">> "))
    if age <3:
        print("your ticket is free")
    elif age <= 12:
        print("the cost of the ticket is $10")
    elif age >12:
        print("the cost of the ticket is $15")