class A: #paren class
    def __init__(self, name):
        self.name=name

    def hello(self):
        print("Hello from class a")


class B(A): #child class

    #a er property b te ante chai
    def __init__(self):
        pass

    def hello(self):
        print("Hello from class b") #overriding


obj = B()
obj.hello()
