w=int(input())
a=1000
for i in range(0,20):
    if pow(2,i)<=w:
        x = abs(pow(2, i) - w1)
        if x < a: a = x
print(a)
