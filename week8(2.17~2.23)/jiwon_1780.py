import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
  tempArr = list(map(int, sys.stdin.readline().split()))
  arr.append(tempArr)

cnt = [0,0,0]

def cut(x,y,len):
  temp = arr[x][y]
  flag = True

  if len == 1:
    cnt[temp + 1] += 1
    return

  for i in range(len):
    if not flag:
      break
    for j in range(len):
      #print(x,i,y,j)
      if temp != arr[x + i][y + j]:
        flag = False

  if flag:
    cnt[temp + 1] += 1

  else:
    nextLen = int(len / 3)
    for i in range(3):
      for j in range(3):
        #print(x + nextLen * i, y + nextLen * j, nextLen)
        cut(x + nextLen * i, y + nextLen * j, nextLen)

cut(0,0,N)
for i in range(3):
  print(cnt[i])
