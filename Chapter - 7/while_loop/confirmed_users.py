unconfirmed_users = ['jones','anwar','srinath']
confirmed_users = []

#for moving unverified users to verified users
while unconfirmed_users:
    verified_users = unconfirmed_users.pop()
    confirmed_users.append(verified_users)
#for displaying all verified users
for confirmed_user in confirmed_users:
    print(f"\n{confirmed_user} this user has been verified")

