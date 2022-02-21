from copy import deepcopy
import sys; rl = sys.stdin.readline

X = rl().rstrip()
full_cnt = [0 for _ in range(10)]
cnt = [0 for _ in range(10)]
for i in range(len(X)):
    full_cnt[int(X[i])]+=1

K = len(X)
ans = []
tmp = []
def dfs(num):
    if num == K:
        ans.append(int(''.join(map(str,tmp))))
        return
    for i in range(10):
        if full_cnt[i] > cnt[i]:
            cnt[i]+=1
            tmp.append(i)
            dfs(num+1)
            cnt[i]-=1
            tmp.pop()

dfs(0)
for i in range(len(ans)):
    if i == len(ans)-1:
        print(0)
    elif ans[i] == int(X):
        print(ans[i+1])
        break