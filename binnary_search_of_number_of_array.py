from random import random
N=20
array=[]
for x in range(N):
    array.append(int(random()*10))
array.sort()
print(array)
number = int(input("search for any number in array: "))
mini = 0
maxi = N-1
while mini<=maxi:
    mid = (mini+maxi)//2
    if number < array[mid]:
        maxi = mid-1
    elif number > array[mid]:
        mini = mid+1
    else:
        print("Number is located at ",mid)
        break
else:
    print("There is no number")

