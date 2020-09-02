x=int(input("Insert 1st Number "))
y=int(input("Insert 2nd Number "))
z=int(input("Insert 3rd Number "))
print("The Maximum Number is: ",end="")
if y<= x >= z:
    print(x)
elif x<= y >= z:
    print(y)
else:
    print(z)
