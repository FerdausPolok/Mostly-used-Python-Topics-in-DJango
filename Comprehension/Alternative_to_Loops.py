#Comprehension
myLst= [1,2,4,65,2]

#create a list using myList which will store square values of myList
myLst2 =[]
for i in myLst:
    myLst2.append(i*i)

print("Old list",myLst)
print("New list",myLst2)

#same result with more compact code

comList = [i*i for i in myLst] #[return value + iterating loop]
print("Comprehension List",comList)

#list of the square of the odd numbers of myLst

comList2 = [i*i for i in myLst if i%2==1] #[return value + iterating loop + condition]

print("Comprehension List 2",comList2)