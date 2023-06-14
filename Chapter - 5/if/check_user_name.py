#exercise 5-10
#list:
current_users = ["mark","rinald","joe","feroz","anwar"]
new_users = ["jones","ashwanth","Rinald", "anwar","dani"]

current_users_lower = [current_users_lower.lower() for current_users_lower in current_users]

if new_users :
    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print("Sorry to say user name has been taken ",new_user)
        else:
            print("user name is valid",new_user)
else:
    print("time to get new user ")

