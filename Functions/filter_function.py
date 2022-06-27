#filter function
#based on condition returns

l = [1,3,4,6,77,88,3]

#we will choose only odd nums from this list

def fun(n):
    return n%2==1

newL= list(filter(fun, l))
print(newL)

#then function which will be used inside filter needs to return true or false

#same thing using lambda
newL = list(filter(lambda n: n%2==1, l))
print(newL)

#same thing using comprehension
newL2 = [i for i in l if i%2!=0]
print(newL2)
