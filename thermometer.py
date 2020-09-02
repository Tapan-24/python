x=input("Insert Temperature In 'C' or 'F' : ")
unit= x[-1]
print(unit)
x=int(x[0:-1]) #convert all input from str to int
if unit == 'C' or unit == 'c':
    x=round(x*(9/5)+32)
    print(str(x)+'F')
elif unit == 'F' or unit =="f":
    x=round((x-32)*(5/9))
    print(str(x)+'C')
