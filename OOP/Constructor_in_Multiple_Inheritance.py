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
    def __init__(self, name, job):
        A.__init__(self, name)
        B.__init__(self, job)

    def hello(self):
        #A.hello(self)
        super().hello() #mro follow kore anbe
        B.hello(self)
        print(f"{self.name} is a {self.job}")


obj = C("Polok","Student")
obj.hello()



