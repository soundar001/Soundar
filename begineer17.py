a=input()
a=int(a)
sum=0
temp=a
while(temp>0):
  i=temp%10
  sum=sum+i**3
  temp=temp//10
if(a==sum):
  print('yes')
else:
  print('no')
