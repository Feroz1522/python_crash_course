#exercise 3.8
bc_lst = ["europe","america","india","mongolia","china","saudi arabia"]
print("\n normal list   :")
print(bc_lst)
print("\n sorted list   :")
print(sorted(bc_lst))
print("\n actual list   :")
print(bc_lst)
print("\n again sorted  :")
print(sorted(bc_lst,reverse = True))
print("\n Original list :")
print(bc_lst)
print("\n reversed orginal list :")
bc_lst.reverse()
print(bc_lst)
print("\n again reversing the orginal list : ")
bc_lst.reverse()
print(bc_lst)
print("\n sorting the list :")
bc_lst.sort()
print(bc_lst)
print("\n list has been reversed")
bc_lst.sort(reverse=True)
print(bc_lst)
print("\n number of cities i had planned for going in my bucket list")
print(len(bc_lst))
