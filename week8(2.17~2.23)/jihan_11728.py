import sys;rl=sys.stdin.readline
N,M = map(int,rl().split())

li1 = list(map(int,rl().split())) + [10**9+1]
li2 = list(map(int,rl().split())) + [10**9+1]
ptr1 = 0
ptr2 = 0
ans = []

for _ in range(N+M):
  x1 = li1[ptr1]
  x2 = li2[ptr2]
  if x1 < x2:
    ans.append(str(x1))
    ptr1+=1
  else:
    ans.append(str(x2))
    ptr2+=1

print(' '.join(ans))