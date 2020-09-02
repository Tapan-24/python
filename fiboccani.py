x= int(input("Insert Number Of elements of Fiboccani series: "))
a=1
b=1
print(a,b,end=" ")
for i in range(x-2):
    print(a+b,end=" ")
    a,b=b,a+b
