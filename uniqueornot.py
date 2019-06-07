
n=int(input())
a=[int(a) for a in input().split()]
e=[]
for i in range(0,n-1):
    for j in range(i+1,n):
        if(a[i]==a[j]):
            e.append(a[i])
            
d=list(set(sorted(e)))
if len(d)==0:
    print("unique")
else:
    for i in range(0,len(d)):
        print(d[i],end=" ")
