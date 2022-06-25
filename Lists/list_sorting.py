myList = ["Bhutan", "Nepal", "Bangladesh", "France", "Austria", "Denmark", "Brazil",  "Argentina", "UK", "Norway", "dubai"]

print(myList)
myList.sort(key=str.lower, reverse=True) #key=str.lower helps us to sort upper and lowers at the same time

print(myList)
myList.reverse()
print(myList)

