#map function -> we can run any function in any iterable item like list

def fun(n):
    return n**3

l = [3,4,1,0,6]

newL = list(map(fun, l))
print(newL)
newL = tuple(map(fun, l))
print(newL)

#using lambda with map
newL = list(map(lambda n: n**3, l))
print(newL)

#same thing using comprehension
newL2 = [i**3 for i in l]
print(newL2)


#map example 2
l2 = ["Polok", "Zaman", "Dhaka"]

l3= list(map(list, l2))
print(l3)


