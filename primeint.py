a,c=input().split()
d=[]
f=''
for i in range(int(a),int(c)+1):
    b=1
    e=0
    while b<=i:
        if(i%b==0):
            e=e+1
        b+=1
    if(e==2):
        d.append(i)
for i in range(len(d)-1):
    f+=str(d[i])+" "
print(f+str(d[-1]))
