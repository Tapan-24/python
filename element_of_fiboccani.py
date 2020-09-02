x=abs(int(input("Insert Number To find value in fibonnaci series: ")))
a=b=1
y=2
while y < x:
    a,b = b,a+b
    y+=1
print("%d element of fibonnaci element is %d" %(x,b))