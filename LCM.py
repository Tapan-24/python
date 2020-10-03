def lcm(x,y):
    z=x*y
    while x!=0 and y!=0:
        if x>y:
            x%=y
        else:
            y%=x
    return z//(x+y)
a=int(input("insert Value of 1st number: "))
b=int(input("Insert value of 2nd number: "))
print(lcm(a,b))