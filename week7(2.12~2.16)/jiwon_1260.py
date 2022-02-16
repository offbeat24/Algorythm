from collections import deque
import sys
N,M,V = map(int, sys.stdin.readline().split())

arr = list(list(map(int,sys.stdin.readline().split())) for _ in range(M))

graph = [[0] * N for _ in range(N)]

for point in arr:
  graph[point[0] - 1][point[1] - 1] = 1
  graph[point[1] - 1][point[0] - 1] = 1


def DFS(V):
  print(V,end=' ')
  DFSvisited.append(V-1)
  for p in range(len(graph[V-1])):
    if graph[V-1][p] == 1 and not p in DFSvisited:
      DFS(p + 1)


def BFS(V):
  queue = deque([V - 1])
  BFSvisited.append(V - 1)

  while queue:
    temp = queue.popleft()
    print(temp+1, end=' ')
    for p in range(len(graph[temp])):
      if graph[temp][p] == 1 and not p in BFSvisited:
        queue.append(p)
        BFSvisited.append(p)

DFSvisited = []
BFSvisited = []
DFS(V)
print()
BFS(V)
