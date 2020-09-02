import math
x=float(input("Insert Point x: "))
y=float(input("Insert Point y: "))
r=float(input("Insert Radius length "))
hypotenuse = math.sqrt(pow(x,2)+pow(y,2))
if hypotenuse < r:
    print("Point is in Circle ")
elif hypotenuse == r:
    print("Point is on Circle ")
else:
    print('Point Does not belong to circle ')
