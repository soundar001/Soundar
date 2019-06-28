li=[]
N=int(input())
for i in range (0,N):
    a=int(input())
    li.append(a)
li.sort()
b=len(li)//2
print (li[b])
