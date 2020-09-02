x=int(input("Insert Number To Reverse" ))
y = 0
while x != 0:
    digit = x%10
    x=x//10
    y=(y*10)+digit
print("reverse Of Number is",y)