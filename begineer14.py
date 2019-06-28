a,b=map(int,input().split())
if (a%2==0):
  for i in range (a,b):
     if(i%2==1):
         print(i,end=" ")
else:
    for i in range (a+1,b):
        if(i%2==1):
            print(i,end=" ")
