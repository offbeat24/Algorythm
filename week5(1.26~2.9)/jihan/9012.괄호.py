n = int(input())
list = []

for i in range(n):
  list.append(input())

def isVPS(string):
  queue = []
  for i in string:
    if len(queue)==0:
      if i == '(':
        queue.append(i)
      else:
        return False
    else:
      if queue[len(queue)-1]=='(':
        if i == ')':
          del queue[len(queue)-1]
        else:
          queue.append(i)
  if len(queue) == 0:
    return True
  else:
    return False

for i in list:
  if isVPS(i):
    print('YES')
  else:
    print('NO')