#exercise 5-9
users = []
if users :
    for user in users :
        if user == "admin":
            print("hello admin ! have a check on daily report ")
        elif user == "False":
            print("time to get new user ")
        else:
            print("hello ",user + " thank you for logging in again ")
else:
    print("time to get new user's ")
