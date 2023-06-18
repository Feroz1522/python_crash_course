#exercise 6-10
fav_num = {
        'anwar':['19','16','17'],
        'feroz':['5','10','3'],
        'dani':['45','35','7'],
        'kathir':['67','55','87']
        }
for favorite,nums in fav_num.items():
    print(f" \n the user name is {favorite} favorite number for {favorite} is :")
    for num in nums:
        print("\t- "+ num)
