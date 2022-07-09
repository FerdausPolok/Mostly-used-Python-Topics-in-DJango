#Meta class is the class of class
#EVERYTHING IS OBJ IN PYTHON


#example that everything in python is class-obj

myStr= "Polok"
myNum= 10
myDict={"name": "Zaman"}
myList=[1,2,1,2]

print(type(myStr)) #obj of str class
print(type(myNum)) #obj of int class
print(type(myDict)) #obj of dict class
print(type(myList)) #obj of list class

class A:
    pass

obj = A()

print(type(obj)) #A class er obj
print(type(A)) #type class er obj, therefore here type is the meta class

