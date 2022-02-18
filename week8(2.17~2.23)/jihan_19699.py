import sys; rl = sys.stdin.readline

N,M = map(int,rl().split())
weight = list(map(int,rl().split()))

def isPrime(Num):
    if Num < 2:
        return False
    for i in range(2,Num):
        if Num%i == 0:
            return False
    return True

selected = [False for _ in range(N)]
ans = []

def dfs(Num,Sum):
    if Num == M:
        if not Sum in ans:
            if isPrime(Sum):
                ans.append(Sum)
        return
    for i in range(N):
        if selected[i] == False:
            selected[i] = True
            dfs(Num+1,Sum+weight[i])
            selected[i] = False

dfs(0,0)
if len(ans) == 0:
    print(-1)
else:
    ans = list(set(ans))
    ans.sort()
    print(' '.join(map(str,ans)))