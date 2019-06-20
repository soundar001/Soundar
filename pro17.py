m1,s1=map(int,input().split())
array1=list(map(int,input().split()))
r1=0
for i in range(len(array1)):
	for j in range(i+1,len(array1)):
		if (array1[i]+array1[j]==s1):
			r1+=1
			break
if(r1):
	print("yes")
else:
	print("no")
