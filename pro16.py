a=int(input())
b=list(map(int,input().split()))
x=[1]*a
for i in range(a):
    if i==0:
        if b[i]>b[i+1]:
            x[i]=x[i]+x[i+1]
    elif i>0:
        if b[i]>b[i-1]:
            x[i]=x[i]+x[i-1]
print(sum(x))
