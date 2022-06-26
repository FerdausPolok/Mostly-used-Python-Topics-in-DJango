#for loop

#for i in tuple, range, dictionary, list

myTpl= ("a","b","c","d")
for x in myTpl:
    print(x)

myLst=[("a",1),("b",2),("c",3)] #list of tuples
for x,y in myLst:
    print(f"{x},{y}")

myLst=[("a",1,"BDT"),("b",2,"INR"),("c",3,"USD")] #list of tuples
for x,y,z in myLst: #this works like unpacking
    print(f"{x},{y},{z}")

#dict

myDict={
    "name": "Polok",
    "age": 25,
    "Country": "Bangladesh"
}
for key, value in myDict.items():
    print(f"{key} -> {value}")

#String
myStr= "Ferdaus Zaman Polok"
for char in myStr:
    print(char)

#set

mySet={"BDT", "USD", "CAD"}
for currency in mySet:
    print(currency)