def hello(fname, lname): #perameter -> received values
    print(f"Full name: {fname} {lname}")

hello("Ferdaus", "Polok") #Arguments -> Passed values

#When we do not know the correct arg numbers
#Arbitrary Arguments

def fun1(*args): #ja ja ashbe shob pack kore tuple a dibe
    print(args)
    print(args[2])

fun1("Ferdaus", "Zaman", "Polok", 25)





