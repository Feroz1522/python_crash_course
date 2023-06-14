#exercise 3.7
guests = ['anwar basha', 'soundar','vishal','arjun']
print(f'hi i {guests[0]} would like to invite you to dinner... waiting for your @ bismillah')
print(f'i would like to invite you {guests[1]}')
print(f'hello buddy {guests[2]}')

#new members
print(f'arigatho buddy i wont get see a person as you in my life {guests[3]}')
guests.insert(0," jones")
guests.insert(2," ziya")
guests.append(" shanmuga shundram")
print(f"i am glad to inviting you to my house for party  {guests[0]}")
print(f" a person who is acted as a friend and my relative {guests[2]}")
print(f" a old man  {guests[6]} who is a friend for our clg Friend lol :) ")

#NEWINVITATION
print(" _______________________________________ NEW INVITATION___________________________________")
print("in our sleep over , we having more than 5 people once again i like to tell their name " + guests[0]+" "+guests[1]+" "+guests[2]+" " +guests[3]+" "+guests[4]+" "+guests[5]+" "+guests[6])
print("============================================xxxx====================================================")
print("you can invite only two people for dinner ")

#only two people can access table
x = guests.pop(2)
print("Sorry to tell you about this " + guests.pop(2)+ " there is no room ")
print("Sorry to say ... " + guests.pop(2)+"there is no room")
print("Sorry to say ... " + guests.pop(2)+ "there is no room ")
print("no comments simply waste " +guests.pop(2)+ "there is no room")

#inviting the balance members for food
print(f"comeon guyz{guests[0]} ! dinner has been ready")
print(f"should i need to call you once again ...{guests[1]}")

#deleting the balance members
del guests[0]
del guests[0]

#checking the balance list
#print(guests[0])
