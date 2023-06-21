welcome = "\n welcome to our pizza shop "
welcome += "\n which type of topings do you need "
print(welcome)
while True:
    toppings = input(">> ")
    if toppings =="quit":
        break
    else:
        print(f"we added {toppings} in your pizza ")

print("your order will be in 15 minutes")
