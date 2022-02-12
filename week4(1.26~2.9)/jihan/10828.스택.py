import sys
n = int(sys.stdin.readline())
commans = []
for i in range(n):
  commans.append(sys.stdin.readline().split())
stack = []

def push(stack, num):
  stack.append(int(num))

def pop(stack):
  if len(stack)==0:
    return -1
  else:
    return stack.pop(len(stack)-1)

def size(stack):
  return len(stack)

def empty(stack):
  if len(stack)==0:
    return 1
  else:
    return 0

def top(stack):
  if len(stack)==0:
    return -1
  else:
    return stack[len(stack)-1]

for i in range(0,len(commans)):
  if commans[i][0] == 'push':
    push(stack, commans[i][1])
  elif commans[i][0] == 'pop':
    print(pop(stack))
  elif commans[i][0] == 'size':
    print(size(stack))
  elif commans[i][0] == 'empty':
    print(empty(stack))
  elif commans[i][0] == 'top':
    print(top(stack))