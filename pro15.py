a=int(input())
b=list(map(int,input().split()))
n=s=[]
for i in range(0,a):
    n=list(bin(b[i]))
    n=n[2:]
    s.append(n)
s=sorted(s)
s=s[::-1]
for i in range(0,a):
    y=1
    z=0
    for j in range(len(s[i])-1,-1,-1):
        z=z+(int(s[i][j])*y)
        y=y*2
    print(z)
