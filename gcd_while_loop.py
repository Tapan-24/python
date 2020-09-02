x=int(input("Insert 1st Number To Find GCD: "))
y=int(input("Insert 2nd Number To Find GCD: "))
while x!=y:
    if x>y:
        x-=y
    else:
        y-=x
print("GCD is: ",x)