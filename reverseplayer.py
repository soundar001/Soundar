N=int(input())
reverse=0
while(N!=0):
  temp=N%10
  reverse=reverse*10+temp
  N=int(N/10)
print(reverse)
