from math import sqrt
x=float(input("Insert x= "))
y=float(input("Insert y= "))
z=float(input("Insert z= "))
d=y*y-4*x*z
if d>0:
    x1=(-y+sqrt(d))/(2*x)
    x2=(-y-sqrt(d))/(2*x)
    print("x1 = %.2f : x2 = %.2f" %(x1,x2))
elif d==0:
    x1 = -y/(2*x)
    x2 = -y/(2*x)
    print("x1 = %.2f : x2 = %.2f" %(x1,x2))
else:
    print("No roots exist")
