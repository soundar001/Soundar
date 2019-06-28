li=[]
N=int(input())
for i in range (0,N):
    a=int(input())
    li.append(a)
li.sort()
for i in range(0,len(li)):
    print(li[i],end=" ")
