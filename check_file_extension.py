exe=('gif','png','jpeg','jpg','txt')
filename=input("Inser File with extension").split('.')
if len(filename)>=2:
	ext=filename(-1).lower()
	if ext in exe:
		print("File extension Exist")
	else:
		print("File Extension does not exist")
else:
	print("File Does not have extension")
