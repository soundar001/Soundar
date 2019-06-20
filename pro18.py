n1,m1=map(int,input().split())
t=[]
x=0
for i in range(n1):
    t.append(list(map(int,input().split())))   
for i in range(n1):
    for j in range(m1-1):
        for k in range(j+1,m1+1):
            if t[i][j:k]==[1]*len(t[i][j:k]):
                 if all(t[p+i][j:k]==[1]*len(t[p+i][j:k]) for p in range(len(t[i][j:k])-1)):
                     if len(t[i][j:k])>x:
                        x=len(t[i][j:k])
if len(t)==1 and len(t[0])==1 and t[0][0]==1:
    print(1)
for i in range(x):
    print(*[1]*x)
