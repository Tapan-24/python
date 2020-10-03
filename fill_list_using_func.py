from random import randint
def list_fill(first,qyt,mini,maxi):
    for i in range(qyt):
        first.append(randint(mini,maxi))
minimum=int(input("Insert Minimum value: "))
maximum=int(input("Insert Maximum value: "))
num=int(input("Number of Elements:"))
x=[]
list_fill(x,num,minimum,maximum)
print(x)