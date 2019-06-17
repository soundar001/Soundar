m,n=map(int,input().split())
for i in range (m+1,n):
  z=0
  t=i
  while(t>0):
    x=t%10
    t=t//10
    y=x**3
    z=z+y
  if(i==z):
      print(z,end=' ')
