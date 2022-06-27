#Higher order function-> Accepts functions as argument or returns functions

def myFunc():
    def hello():
        print("Hello world")

    return hello

f= myFunc()
f()

#wrapper function - helps to reuse code

def myWrapper(fn):
    def test():
        print("Iam from test function! Before")
        fn()
        print("Im from test function! After")

    return test

def greet():
    print("Hello world")

greet = myWrapper(greet)
greet()

#Decorators - Makes wrapper function simple
@myWrapper
def hello():
    print("Hello world")

hello()
