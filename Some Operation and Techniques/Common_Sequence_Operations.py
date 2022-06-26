#list, tuple, range
#list -> Mutable
#tuple -> Immutable


myTpl = ("Polok", "Zaman", 25)
myLst= ["Polok", "Zaman", 25]
myRange= range(0,51)

#some common operations among them

#in
print("Polok" in myTpl)
print("Zaman" in myLst)
print(100 in myRange)

#same goes for not in

print("Polok" not in myTpl)
print("Zaman" not in myLst)
print(100 not in myRange)

#concat
myTpl2  = ("Ferdaus",)
result = myTpl + myTpl2
print(result)

#indexing
print(myTpl2[0])

#length
print(len(myLst))