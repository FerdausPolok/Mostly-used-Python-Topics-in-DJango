class A:
    def __init__(self, name):
        self.name= name

    def hello(self):
        print("Hello from Class A")

obj = A("Polok")
obj.hello()

#Applying Inheritance

class B(A):
    pass

obj2 = B("Zaman")

obj2.hello()