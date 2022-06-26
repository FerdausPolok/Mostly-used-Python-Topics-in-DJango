myLst=["Apple", "Orange", "Banana","Jackfruit"]

for fruit in myLst:
    print(fruit)

#getting value with index using enumerate

for index, value in enumerate(myLst):
    print(f"{index}: {value}")

#perallary looping two diff lists using zip

myLst2 = [1,2,3,4]

for i, j in zip(myLst2,myLst):
    print(i, j)

#sorting and accessing any sequence

for fruit in sorted(myLst):
    print(fruit)

#sorting (reverse) and accessing any sequence

for fruit in reversed(sorted(myLst)):
    print(fruit)