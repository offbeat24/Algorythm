from collections import deque


n, m = map(int, input().split())

maze = list()

for _ in range(n):
    maze.append(list(map(int, input())))

dq = deque()
dq.append([0, 0])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
while dq:
    x, y = dq.popleft()
    for i in range(4):
        if x+dx[i] in range(0, n) and y+dy[i] in range(0, m):
            if maze[x+dx[i]][y+dy[i]] == 1:
                maze[x+dx[i]][y+dy[i]] = maze[x][y] + 1
                dq.append([x+dx[i], y+dy[i]])

print(maze[n-1][m-1])
