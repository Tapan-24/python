x= int(input("Enter few numbers without space: "))
eve = 0
odd = 0
while x>0:
    if x%2==0:
        eve += 1
    else:
        odd += 1
    x = x//10
print("Even numbers are %d and odd numbers are %d"%(eve,odd))
