a=int(input())
b=int(input())
if(a%2==0):
  for i in range (a,b):
    if(a%2==1):
      print(i)
else:
  for i in range (a+1,b):
    if(a%2==1):
      print(i)
