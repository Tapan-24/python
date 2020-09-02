print("zerp terminates program!")
while True:
    o = input("Choose Operator(+, -, *, /): ")
    if o == '0':
        break
    if o in ('+','-','*','/'):
        x= float(input("Enter value of 1st operand: "))
        y=float(input("Enter value of 2nd operand: "))
        if o == '+':
            print("%.2f" % (x+y))
        elif o=='-':
            print("%.2f" % (x-y))
        elif o == '*':
            print("%.2f" % (x*y))
        elif o =='/':
            if y!=0:
                print("%.2f" % (x//y))
            else:
                print("Error! Division by zero...")
        else:
            print("Invalid operator")


