str = input("Insert Different String: ")
first = str.split()
len_str = len(first)
longest = 0
for i in range(len_str-1):
    if len(first[longest])< len(first[i]):
        longest = i
print(first[longest])
      