#exercise 3.10
bucketlst = ["audi r8","a own house","financial freedom","helping a charity","making a change in someone's life"]
print(" \n my bucket list are " , bucketlst)
bucketlst.insert(0,"making mom and dad retire ")
bucketlst.append("full filling their needs and keeping them happy ")
print(bucketlst)
print(f"\n i think in my life i should need to my {bucketlst[1]}")
bucketlst.remove("financial freedom")
del bucketlst[2]
print (bucketlst)
x = bucketlst.pop(4)
print(x)
sorted(bucketlst,reverse = True)
print(bucketlst)
