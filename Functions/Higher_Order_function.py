#Higher order function can accept another function as arguments like: filter

def hof(fn):
    print(fn.__name__)
    fn()

def greet():
    print("Hello World")

def hello():
    print("Hello Polok")

hof(greet)

li=[1,2,3,4,5,6]
li2 = list(filter(lambda x: x%2==1, li))
print(li2)

def myFilter(fn, l):
    newL= []
    for i in l:
        if fn(i):
            newL.append(i)
    return newL

li=[1,2,3,4,5,6]
li2 = myFilter(lambda x: x%2==1, li)
print(li2)