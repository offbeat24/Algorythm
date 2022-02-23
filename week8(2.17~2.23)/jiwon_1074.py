import sys

N,r,c = map(int, sys.stdin.readline().split())
cnt = 0
flag = False

def countZ(x,y,len):
  global cnt, r, c
  if x == r and y == c:
    print(cnt)
    return
  nextLen = int(len / 2)

  for i in range(2):
    for j in range(2):
      nextX = x + i * nextLen
      nextY = y + j * nextLen
      if nextX <= r and r < nextX + nextLen and nextY <= c and c < nextY + nextLen:
        countZ(nextX, nextY, nextLen)
      else:
        cnt += nextLen * nextLen
  return

countZ(0,0,1 << N)

"""
def countZ(x,y,len):
  global cnt, flag
  if flag or len < 1:
    return

  nextLen = int(len / 2)

  for i in range(2):
    for j in range(2):
      nextX = x + i * nextLen
      nextY = y + j * nextLen
      if len == 2:
        cnt += 1
        #print(nextX, nextY, cnt)
        if nextX == r and nextY == c:
          print(cnt)
          flag = not flag
      #print(nextX, nextY, nextLen)
      if not flag:
        countZ(nextX, nextY, nextLen)

countZ(0,0,1 << N)
"""
