import random
x=20
y=[]
for i in range(x):
	y.append(int(random.random()*100)-30)
print(y)
positive=[]
negative=[]
for i in y:
#	print(i)
	if i>0:
#		print("p",i)
		positive.append(i)
	elif i<0:
#		print("n",i)
		negative.append(i)
print("Positive Number = ",positive)
print("Negative Number = ",negative)

