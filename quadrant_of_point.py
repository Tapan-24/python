x=float(input("Insert coordinate of point x: "))
y=float(input("Insert Coordinate of point y: "))
if x>0 and y>0:
    print("Point is in 1st quadrant ")
elif x<0 and y>0:
    print("Point is in 2nd quadrant ")
elif x<0 and y<0:
    print("Point is in 3rd quadrant ")
elif x>0 and y< 0:
    print("Point is in 4th quadrant ")
elif x==0 and y==0:
    print("Point of Origin ")
elif x==0 and y!=0:
    print("Point is on x axis ")
elif x!=0 and y==0:
    print("point is on y axis ")
else:
    print("invalid input")
