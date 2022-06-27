# Keyword argument pass / default value pass
def fun2(fname="Ferdaus", lname="Polok"):
    print(f"Full name: {fname} {lname}")

fun2()
fun2("Zaman", "Polok")
fun2("Yo")


#Arbitrary keywords Arguments dynamically

def fun3(**kwargs): #dict akare save hobe
    print(kwargs)

fun3(fanme= "AAAA", lname="hhhfhf", age=105)

def fun4(*args, **kwargs):
    print(args, kwargs)

fun4("Ferdaus", "Polok", fanme= "AAAA", lname="hhhfhf", age=105)


#*args -> used for unseen pass which will store on a tupple
#**kwargs -> we can pass using keyword while calling the function which will be stored as a dict inside the fun
