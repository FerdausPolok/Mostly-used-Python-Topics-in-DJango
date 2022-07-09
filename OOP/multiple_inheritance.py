class A:
    def __init__(self, name):
        self.name=name

    def hello1(self):
        print("Hello from class a")


class B:

    def __init__(self, job):
        self.job=job


    def hello2(self):
        print(f"{self.name} is a {self.job}") #overriding

class C(A,B): #Multiple inheritance
    pass



obj = C("Polok") #A er contructor age hit hobe
#same goes for same named function; jeta age inherit korbe shetar function call hobe


