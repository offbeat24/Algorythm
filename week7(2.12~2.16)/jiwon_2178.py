from collections import deque
import sys
N,M = map(int, sys.stdin.readline().split())

maze = list(list(sys.stdin.readline().rstrip()) for _ in range(N))

maze[0][0] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque(list([[0, 0]]))

while queue:
  x, y = queue[0][0], queue[0][1]

  queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 0 and ny >= 0 and nx < N and ny < M:
      if maze[nx][ny] == "1":
        maze[nx][ny] = maze[x][y] + 1
        queue.append([nx,ny])

print(maze[N-1][M-1])
