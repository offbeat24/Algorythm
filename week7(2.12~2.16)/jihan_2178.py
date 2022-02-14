import sys
from collections import deque

N,M = list(map(int,sys.stdin.readline().split()))
miro = []

for _ in range(N):
    miro.append(sys.stdin.readline().rstrip())

#queue의 값은 [행,열,이동횟수]
visited = [[False for _ in range(M)] for _ in range(N)]
queue = deque()
queue.append([0,0,1])
sol_list = []

while queue:
    node = queue.popleft()
    if node[0]>=N or node[0]<0 or node[1]>=M or node[1]<0 or miro[node[0]][node[1]] == '0':
        continue
    elif node[0] == N-1 and node[1] == M-1:
        break
    elif visited[node[0]][node[1]] == False:
        visited[node[0]][node[1]] = True
        queue.append([node[0]+1,node[1],node[2]+1])
        queue.append([node[0]-1,node[1],node[2]+1])
        queue.append([node[0],node[1]+1,node[2]+1])
        queue.append([node[0],node[1]-1,node[2]+1])


print(node[2])