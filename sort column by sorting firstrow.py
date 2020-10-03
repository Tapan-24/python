from random import randint
row=4
col=4
matrix=[]
for i in range(row):
    myrow=[]
    for i in range(col):
        myrow.append(randint(0,20))
    matrix.append(myrow)
print("unsorted")
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()
n=col-1
while n!=0:
    z=0
    for j in range(1,n+1):
        if matrix[0][j]>matrix[0][z]:
            z=j
    for i in range(row):
        y=matrix[i][z]
        matrix[i][z]=matrix[i][n]
        matrix[i][n]=y
    n-=1
print("sorted")
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()