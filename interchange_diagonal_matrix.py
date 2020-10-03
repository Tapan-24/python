from random import randint
row=3
col=3
matrix=[]
for i in range(row):
    myrow=[]
    for j in range(col):
        myrow.append(randint(0,20))
    matrix.append(myrow)
print("Befor Interchange")
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()
n=col-1
for i in range(row):
    for j in range(col):
        if i==j:
            temp=matrix[i][j]
            matrix[i][j]=matrix[i][n]
            matrix[i][n]=temp
            n=n-1
print("After Interchamge")
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()
