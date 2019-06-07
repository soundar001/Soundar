    
b=int(input())
n=b//2
d=0
for x in range(2,n+1):
    if b%x==0:
        d=1 
if d==0:
    print('yes')
else:print('no')
