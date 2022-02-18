from re import I
import sys;rl=sys.stdin.readline

N,K = map(int,rl().split())
An = list(map(int,rl().split()))

Sum = 0
end = -1
ans = 100005
for start in range(N):
  if start != 0:
    Sum-=An[start-1]
  while Sum<K and end<N:
    end+=1
    if end<N:
      Sum+=An[end]
  if end == N: break
  ans = min(ans,end-start+1)

if ans == 100005:
  print(0)
else:
  print(ans)