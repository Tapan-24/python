x=  abs(int(input("Enter 1st Number: ")))
y=  abs(int(input("Enter 2nd Number: ")))
i=1
if x>y:
    for i in range(1,x)and range(1,y):
        if x%i==0 and y%i==0:
            gcd=i
            #print("Common factors are ",i)
print("Greatest common factor is ",gcd)


        
