a,b=map(str,input().split())
l1=0
if len(a)>len(b):
  a,b=b,a
i=0
while i<len(a):
  l1+=(ord(b[i])-ord(a[i]))
  i+=1
for i in range(i,len(b)):
  l1+=ord(b[i])-ord('a')+1
print(l1)
