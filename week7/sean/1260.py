from collections import deque


n, m, v = map(int, input().split())


g = [[0] * (n+1) for i in range(n+1)]
visit = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = g[b][a] = 1


def dfs(v):
    visit[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if g[v][i] == 1 and visit[i] == 0:
            dfs(i)


def bfs(v):
    dq = deque()
    dq.append(v)
    visit[v] = 1
    while dq:
        p = dq.popleft()
        print(p, end=' ')
        for i in range(1, n+1):
            if g[p][i] == 1 and visit[i] == 0:
                dq.append(i)
                visit[i] = 1


dfs(v)
visit = [0] * (n+1)
print()
bfs(v)
