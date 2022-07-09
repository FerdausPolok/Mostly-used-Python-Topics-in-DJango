class A: #paren class
    def __init__(self, name):
        self.name=name

    def hello(self):
        print("Hello from class a")


class B(A): #child class

    #a er property b te ante chai
    def __init__(self,name, job):
        #A.__init__(self, name)
        super().__init__(name) #super use korle parent class er nam na janleo hobe
        self.job=job


    def hello(self):
        print(f"{self.name} is a {self.job}") #overriding


obj = B("Polok","Student")
obj.hello()
