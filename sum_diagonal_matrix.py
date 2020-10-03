from random import random
row=3
matrix=[]
sum_diag1=0
sum_diag2=0
for i in range(row):
    myrow=[]
    for j in range(row):
        myrow.append(int(random()*10))
    matrix.append(myrow)
for i in range(row):
    for j in range(row):
        print(matrix[i][j],end=" ")
    print()
for i in range(row):
    sum_diag1 +=matrix[i][i]
    sum_diag2 += matrix[i][row-i-1]
print(sum_diag1)
print(sum_diag2)

