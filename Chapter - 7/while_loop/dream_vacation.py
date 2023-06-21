responded ={}
polling = True
while polling:
    name = input(" your name ")
    responses = input(" your dream place ")
    responded[name] = responses
    print("For responding more polling \n enter y/n ")
    get = input(">> ")
    if get.lower() == "n":
        polling = False
for name,responses in responded.items() :
    print(f"{name} willing to go to his dream place {responses}") 


