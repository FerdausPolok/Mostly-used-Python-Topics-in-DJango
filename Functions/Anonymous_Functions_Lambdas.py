#function
def add(x,y):
    return x+y

#lamda function
add2= lambda x,y: x+y
print(add2(10, 15))

#calling without storing

print((lambda x, y: x*y)(10,2))

#it's called anonymous cause we can do IIFE  (Immediately Invoked Function Expression)

