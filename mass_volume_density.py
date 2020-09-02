mdv = input("choose one to calculate (m,d,v) : ")
if mdv == "m":
    d=float(input("Density: "))
    v=float(input("Volume: "))
    result=d*v
    #print("Mass Is:",m)
elif mdv == "d":
    m=float(input("Mass: "))
    v=float(input("Volume: "))
    result=m/v
    #print("Density Is:",d)
elif mdv == "v":
    m=float(input("Mass: "))
    d=float(input("Density: "))
    result=m/d
    #print("Volume Is:",v)
print("%0.2f" % result)
