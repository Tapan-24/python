list_item=[2,5,8,-10,-4,10,0,57,13,-17,7,0,16]
print(list_item)
for i in range(len(list_item)):
	if list_item[i]>0:
		list_item[i]=1
	elif list_item[i]==0:
		list_item[i]=0
	elif list_item[i]<0:
		list_item[i]=-1
print(list_item)
