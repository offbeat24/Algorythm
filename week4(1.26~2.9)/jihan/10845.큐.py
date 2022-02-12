import sys

n = int(sys.stdin.readline())
commans = []
for i in range(n):
    commans.append(sys.stdin.readline().split())
queue = []


def push(queue, num):
    queue.append(int(num))


def pop(queue):
    if len(queue) == 0:
        return -1
    else:
        return queue.pop(0)


def size(queue):
    return len(queue)


def empty(queue):
    if len(queue) == 0:
        return 1
    else:
        return 0


def back(queue):
    if len(queue) == 0:
        return -1
    else:
        return queue[len(queue) - 1]
      
def front(queue):
    if len(queue) == 0:
        return -1
    else:
        return queue[0]


for i in range(0, len(commans)):
    if commans[i][0] == 'push':
        push(queue, commans[i][1])
    elif commans[i][0] == 'pop':
        print(pop(queue))
    elif commans[i][0] == 'size':
        print(size(queue))
    elif commans[i][0] == 'empty':
        print(empty(queue))
    elif commans[i][0] == 'front':
        print(front(queue))
    elif commans[i][0] == 'back':
        print(back(queue))
