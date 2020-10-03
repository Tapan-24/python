row=int(input("Enter Number of Rows"))
col=int(input("Enter Number Of Columns"))
matrix=[]
for i in range(row):
    myrow=[]
    for j in range(col):
        k=(int(input()))
        myrow.append(k)
    matrix.append(myrow)
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=' ')
    print()
