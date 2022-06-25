#list - > Mutable / changeable
#tuple - > immutable / non changeable

tp = ("Polok", 25, "Dhaka")
tp =((3,4),"Polok", 25, "Dhaka")

#tp[1] = "Zaman" can't be done

#list inside tupple
tp =([1,2,3], (3,4),"Polok", 25, "Dhaka")

#now we can change the mutable item of the list

tp[0][0]= "Zaman"


print(tp)


