#sliping a lis - means cutting lists

myList = ["Bhutan", "Nepal", "Bangladesh", "France", "Austria", "Denmark", "Brazil",  "Argentina", "UK", "Norway"]

#getting the complete list
newList = myList[:]

#: left is starting point and : right is ending point
newList = myList[2:] #starts from- joto dibo toto theke
newList = myList[:3] #upto - 5 er ag porjonto
newList = myList[1:3]



#stepping ::
newList = myList[::] #shows full list
newList = myList[::1] #shows full list
newList = myList[::2] #Skips 1 - every 2nd member
newList = myList[::3] #Skips 1 - every 2nd and 3rd member

newList = myList[0:5:2]  #starting: ending+1 : skipping step -1
newList = myList[-5:-1:2]
print(newList)


#slicing a string with same technique

str = "FerdausZamanPolok"
newStr = str[-5:-1:2]

print(newStr)