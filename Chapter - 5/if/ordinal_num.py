#exercise  5-11:
ordinal_nums = [ordinal_nums for ordinal_nums in range(1,10)]
print(type(ordinal_nums))
for ordinal_num in ordinal_nums:
    if ordinal_num == 1:
        print("\n 1st ")
    elif ordinal_num == 2:
        print("\n 2nd ")
    elif ordinal_num == 3:
        print("\n 3rd ")
    elif ordinal_num :
        print("\n",ordinal_num, "th")


