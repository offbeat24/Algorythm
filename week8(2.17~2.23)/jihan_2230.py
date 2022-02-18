import sys;rl=sys.stdin.readline

N,M = map(int,rl().split())
An = []
for _ in range(N):
    An.append(int(rl()))
An.sort()

for i in range(N):
    if An[i] - An[0] >= M:
        ans = An[i] - An[0]
        rightp = i
        break

for i in range(1,N):
    diff = An[rightp] - An[i]
    breaker = 0
    while rightp < N:
        if diff >= M:
            ans = min(ans,diff)
            break
        elif rightp == N-1:
            breaker = 1
            break
        else:
            rightp+=1
            diff = An[rightp] - An[i]
    if breaker == 1:
        break

print(ans)