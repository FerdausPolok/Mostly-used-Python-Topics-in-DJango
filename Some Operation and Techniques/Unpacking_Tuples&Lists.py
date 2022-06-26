myTpl=("Bangladesh", "India", "Pakistan")

#assign after unpacking
c1, c2, c3 = myTpl

print(f"{c1}, {c2}, {c3}")

#same goes for list

myLst=["Bangladesh", "India", "Pakistan"]

#assign after unpacking
c1, c2, c3 = myLst

print(f"{c1}, {c2}, {c3}")

#nested loop/ tuple unpacking

myLst=["Bangladesh", "India", "USA", [1,2,3]]

c1, c2, c3, c4 = myLst
print(f"{c1}, {c2}, {c3}, {c4}")

c1, c2, c3, [c4,c5,c6] = myLst
print(f"{c1}, {c2}, {c3}, {c4}, {c5}, {c6}")

#same goes for tuple

#if num of variable and num of element inside tuple or list are not same:

myLst2 = myLst=["Bangladesh", "India", "USA"]
c1, *c2 = myLst2
print(f"{c1}, {c2}")

c1, c2, *c3 = myLst2
print(f"{c1}, {c2}, {c3}")
