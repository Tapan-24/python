str1= input("Inesert Starting letter Of String: ")
str2= input("Insert Ending letter Of string: ")
while str1 <= str2:
    print(str1,end=" ")
    str1 = chr(ord(str1)+1)
print()