str= input("insert Some String of uppercase and lowercase characters: ")
print(str)
len_str=len(str)
upper=lower=0
for i in str:
	if 'a'<=i<='z':
		lower +=1
	elif 'A'<=i<="Z":
		upper +=1
print("Percentage of uppercase: %0.2f %%"%(upper/len_str*100))
print("Precentage of lowercase: %0.2f %%"%(lower/len_str*100))
