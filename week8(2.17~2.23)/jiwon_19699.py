import copy
import sys
n=9000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False


N,M = map(int,sys.stdin.readline().split())
weights = list(map(int, sys.stdin.readline().split()))
weights.sort()

results = []

def search(depth, sum, visited):
  if depth == M:
    if sum in primes:
      if sum not in results:
        results.append(sum)
    return

  else:
    for i in range(N):
      if not visited[i]:
        newVisited = copy.deepcopy(visited)
        newVisited[i] = True
        search(depth + 1, sum+weights[i] , newVisited)

for i in range(N):
  v = [False] * N
  v[i] = True
  search(1,weights[i], v)

if len(results) == 0:
  print(-1)

else:
  results.sort()
  print(" ".join(map(str, results)))
