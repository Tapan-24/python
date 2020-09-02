import random
x=20
y=[]
for i in range(x):
	y.append(int(random.random()*100))
print(y)
even=odd=0
for i in y:
	if i%2==0:
		even+=1
	else:
		odd+=1
print("The Number of Even =",even)
print("The Number of Odd = ",odd)
