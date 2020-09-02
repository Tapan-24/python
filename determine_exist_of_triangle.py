print("Enter proposed length of triangle")
x=float(input("x= "))
y=float(input("y= "))
z=float(input("z= "))
if x+y>z and x+z>y and y+z>x:
    print("Triangle exist")
else:
    print("Triangle does not exist")
