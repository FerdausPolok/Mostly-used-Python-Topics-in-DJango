class A:
    def __init__(self, name):
        self.name=name

    def hello(self):
        print("Hello from class a")

class B:

    def __init__(self, job):
        self.job=job

    def hello(self):
        print("Hello from class B")

class C(A,B):
    def __init__(self):
        pass

    def hello(self):
        print("Hello from class C")


obj = C()
obj.hello() #jeta age pabe sheta call hocche

print(C.__mro__) #mainly exicuting serial

#function er name same hole mro follow kore kaj korbe


