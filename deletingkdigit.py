from itertools import combinations
N,K=map(int, input().split())
L=len(str(N))
i=list(combinations(str(N),L-K))
i=sorted(i)
print("".join(i[0]))
