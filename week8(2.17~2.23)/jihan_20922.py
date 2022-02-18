import sys; rl = sys.stdin.readline

N,K = map(int,rl().split())
An = list(map(int,rl().split()))
start,end,Max = 0,0,0
counter = [0 for _ in range(max(An)+1)]

while end < N:
    if counter[An[end]] < K:
        counter[An[end]]+=1
        end+=1
    else:
        counter[An[start]]-=1
        start+=1
    Max = max(Max, end - start)

print(Max)