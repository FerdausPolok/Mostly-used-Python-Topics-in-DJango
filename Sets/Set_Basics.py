#No duplicate data in set

mySet ={"A", "B", "B", 1,1,2}
print(mySet)

#We use set to remove duplicates

emplty_set = {} #it will be a dict

print(emplty_set)
print(type(emplty_set))

#so to declare empty set we need to call the set fun
emplty_set = set()
print(emplty_set)
print(type(emplty_set))

#covert a string into a set

set1 = set("abcdefgh")

print(set1) #no sequence maintain in set

#thats why we will not use set for sorting

