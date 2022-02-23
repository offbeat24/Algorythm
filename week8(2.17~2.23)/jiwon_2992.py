import sys, copy

X = sys.stdin.readline().rstrip()
arr = [x for x in X]
res = []

def find(S, visited):
  #print(S)
  #Bprint("visited: ", visited)
  if len(S) == len(X):
    if int(S) not in res:
      res.append(int(S))
    return

  for i in range(len(X)):
    if not visited[i]:
      newVisited = copy.deepcopy(visited)
      newVisited[i] = True
      find(S + arr[i], newVisited)
  return

for i in range(len(arr)):
  visited = [False] * len(X)
  visited[i] = True
  find(arr[i], visited)

res.sort()

if res[len(res) - 1] == int(X):
  print(0)
else:
  for i in range(len(res) - 1):
    if res[i] == int(X):
      print(res[i+1])
      break
