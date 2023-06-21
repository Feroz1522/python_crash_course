print("enter your age\n 'quit' for exiting the ticket session")

while True:
    age = input(">> ")
    if age =="quit":
        break
    elif int(age) <3:
        print("your ticket is free")
    elif int(age) <= 12:
        print("the cost of the ticket is $10")
    elif int(age)>12:
        print("the cost of the ticket is $15")
