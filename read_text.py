text=[]
for i in open("D:/un_sorted/tapan.txt"):
    text.append(i)
#print(text)
for i in range(len(text)):
    if text[i][-1]=='\n':
        text[i]=text[i][:-1]
print(text)