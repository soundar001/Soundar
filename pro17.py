m,s=map(int,input().split())
array=list(map(int,input().split()))
r=0
for i in range(len(array)):
	for j in range(i+1,len(array)):
		if (array[i]+array[j]==s):
			r+=1
			break
if(r):
	print("yes")
else:
	print("no")
