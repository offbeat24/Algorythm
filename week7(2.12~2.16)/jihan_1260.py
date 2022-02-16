import sys
from collections import deque

N,M,V = list(map(int,sys.stdin.readline().split()))
lines = [[] for i in range(0,N+1)]
visited = [False for i in range(0,N+1)]
dfs_str = []
bfs_str = []

for _ in range(M):
    a,b = list(map(int,sys.stdin.readline().split()))
    lines[a].append(b)
    lines[b].append(a)

depth = 0

def dfs(point):
    if visited[point] == False:
        visited[point] = True
        global dfs_str
        dfs_str.append(str(point))
        for i in sorted(lines[point]):
            dfs(i)
    else:
        return 0

dfs(V)
print(' '.join(dfs_str))

visited = [False for i in range(0,N+1)]

def bfs(point):
    queue = deque()
    queue.append(point)
    visited[point] = True
    bfs_str.append(str(point))

    while queue:
        tmp = queue.popleft()
        if visited[tmp] == False:
            visited[tmp] = True
            bfs_str.append(str(tmp))
        for i in sorted(lines[tmp]):
            if visited[i] == False:
                queue.append(i)

bfs(V)
print(' '.join(bfs_str))
    