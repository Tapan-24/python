str = input("Insert Different String: ")
first = str.split()
len_str = len(first)
for i in range(len_str-1):
    for j in range(len_str-1-i):
        if len(first[j])>len(first[j+1]):
            first[j],first[j+1] = first[j+1],first[j]
print(" ".join(first))

