#matrix
# 0 1 2 3
# 0 1 2 3
# 0 1 2 3

myMatrix = [[0,1,2,3], [0,1,2,3], [0,1,2,3]]
print(myMatrix[0][2])

#uisng loop
loopMatrix = []

for i in range(3):
    loopMatrix.append([])
    for j in range(4):
        loopMatrix[i].append(j)

print(loopMatrix)

#using comprehension
#bairer ta sheshe handle korbo

compMatrix = [ [j for j in range(4)] for i in range(3)]

print(compMatrix)

#flating the matrix using comprehension
#proti list er 1st element niye list

flatList = [ i[0] for i in myMatrix]

print(flatList)