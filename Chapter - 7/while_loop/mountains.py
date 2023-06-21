responses = {}
polling = True
while polling:
    name = input(" enter your name ")
    response = input(" which mountain  would like to climb ")

    responses[name] = response
    
    repeat = input("would you like to add another member for adding this poll\n\t y / n :")
    if repeat =="n":
        polling = False
print(responses)
for nam,response in responses.items():
    print(f"i'm {nam} i would like to climb in {response}")


