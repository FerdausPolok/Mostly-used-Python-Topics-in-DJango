#Comprehension can be  applied into any iterable item
#like: List, tuple, dictionary, set, range
#can create as return: list, dictionary, set

#FROM LIST

#list from another list
myLst = [1,2,3,4,5,6]
newLst = [i+1 for i in myLst]

print(myLst)
print(newLst)

#dict from list
newDict={i: i*i for i in myLst}
print(newDict)

#set from list
newSet={i**3 for i in myLst}
print(newSet)

#tuple from list
newTple = tuple(i+2 for i in myLst)
print(newTple)

#tuple list from list

newTplelst= [(i, i**2, i+3) for i in myLst]
print(newTplelst)

#FROM DICTIONARY

myDict={"name": "Polok", "address": "Dhaka", "age": 25}

#list from dict
newLst = [value for key, value in myDict.items()]
print(newLst)

#tple list from dict
newtlist = [(key, value) for key, value in myDict.items()]
print(newtlist)

#dict from dict
newDict = {key+"yo": value for key, value in myDict.items()}
print(newDict)