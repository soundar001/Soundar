a=int(input())
b=[int i for in input().split()]
c=0
for i in range(a):
  for j in range (i):
    if b[j]<b[i]:
      c+=b[j]
print(c)
