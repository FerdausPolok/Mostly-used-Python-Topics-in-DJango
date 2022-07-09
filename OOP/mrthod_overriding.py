class A:
    def __init__(self, name):
        self.name=name

    def hello(self):
        print("Hello from class a")


class B(A):

    def __init__(self): #overriding constructor
        pass

    def hello(self):
        print("Hello from class b") #overriding


obj = B()
obj.hello()
