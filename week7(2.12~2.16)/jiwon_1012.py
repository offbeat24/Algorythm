import sys
from collections import deque
T = int(sys.stdin.readline())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(T):
  M,N,K = map(int, sys.stdin.readline().split())

  field = [[0] * M for _ in range(N)]
  x = y = 0
  for _ in range(K):
    x,y = map(int,sys.stdin.readline().split())
    field[y][x] = 1


  cnt = 0
  for a in range(N):
    for b in range(M):
      if field[a][b] == 1:
        queue = deque([(a,b)])
        cnt += 1
        field[a][b] = 0
        while queue:
          x, y = queue.popleft()

          for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < N and ny < M:
              if field[nx][ny] == 1:
                field[nx][ny] = 0
                queue.append((nx,ny))
  print(cnt)

"""
for _ in range(T):
  M,N,K = map(int, sys.stdin.readline().split())
  arr=[]
  for _ in range(K):
    arr.append(list(map(int,sys.stdin.readline().split())))

  queue = deque()
  cnt = 0
  while arr:
    queue.append(arr[0])
    cnt += 1
    while queue:
      temp = queue.popleft()
      x = temp[0]
      y = temp[1]

      if temp in arr:
        arr.remove(temp)

      if [x-1,y] in arr:
        queue.append([x-1,y])
      if [x+1,y] in arr:
        queue.append([x+1,y])
      if [x,y-1] in arr:
        queue.append([x,y-1])
      if [x,y+1] in arr:
        queue.append([x,y+1])

  print(cnt)
"""

"""
def solve(M,N):
  cnt = 0
  for x in range(N):
    for y in range(M):
      if field[x][y] == 1:  #1을 찾는다
        cnt += 1

        queue = deque([[x,y]])
        while queue:  #1의 인근 1을 0으로 바꿈
          x = queue[0][0]
          y = queue[0][1]
          field[x][y] = 0
          queue.popleft()

          if x > 0:
            if field[x - 1][y] == 1:
              queue.append([x-1,y])
          if y > 0:
            if field[x][y - 1] == 1:
              queue.append([x,y-1])
          if x < N - 1:
            if field[x + 1][y] == 1:
              queue.append([x + 1,y])
          if y < M - 1:
            if field[x][y + 1] == 1:
              queue.append([x,y + 1])
  return cnt

for _ in range(T):
  M,N,K = map(int, sys.stdin.readline().split())
  arr = []
  for _ in range(K):
    arr.append(list(map(int,sys.stdin.readline().split())))

  field = [[0] * M for _ in range(N)]
  for point in arr:
    field[point[1]][point[0]] = 1

  print(solve(M,N))
"""
