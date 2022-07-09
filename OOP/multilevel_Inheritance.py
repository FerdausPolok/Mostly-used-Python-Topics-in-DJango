class A: #paren class
    def __init__(self, name):
        self.name=name

    def hello(self):
        print("Hello from class a")


class B(A): #child class


    def __init__(self,name, job):
        super().__init__(name)
        self.job=job


    def hello(self):
        print(f"{self.name} is a {self.job}") #overriding

class C(B):
    pass



obj = C("Polok","Student")
print(dir(obj)) #object er shob available method and attribute dekhabe
obj.hello() #jake inherit korbe tar ta pabe


