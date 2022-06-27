from functools import reduce as rd

li= [1,2,5,2,1,85,1,8,2,854,5,]

#recude function do something to a list and returns only one value
#like we need the sum of all elements of li

def func(x,y):
    return x+y

sum = rd(func, li)
print(sum)

#same with lambda

sum = rd(lambda x,y: x+y, li)
print(sum)
