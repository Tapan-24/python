from random import randint
row=5
col=10
matrix=[]
for i in range(row):
    myrow=[]
    for j in range(col):
        myrow.append(randint(0,100))
    matrix.append(myrow)
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=' ')
    print()
num=int(input("enter number to find"))
print("Rows: ",end=' ')
for i in range(row):
    if num in matrix[i]:
        print(i,end=" ")
print()
print("Column: ",end=" ")
for j in range(col):
    for i in range(row):
       if matrix[i][j]==num: 
            print(j,end=' ')
            break
print()