r,s=map(int,input().split())
l=list(map(int,input().split()))
r=[]

l.insert(0,0)
for x in range(s):
     q=[]
     summ=0
     c,d=map(int,input().split())
     for i in range(c,d+1):
         
         summ^=l[i]
     
     r.append(summ)
for x in r:
    print(x)
