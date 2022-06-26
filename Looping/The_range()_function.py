#range(starting,ending-1,steps)

myLst = list(range(1,10))
print(myLst)

for i in range(1,10):
    print(i)

for i in range(0,51,5):
    print(i)

myLst=["English", "Bangla", "Spanish"]

for i in range(len(myLst)):
    print("Language:",myLst[i])