import sys

n = int(sys.stdin.readline())
commans = []
for i in range(n):
    commans.append(sys.stdin.readline().split())
deque = []


def push_back(deque, num):
    deque.append(int(num))


def push_front(deque, num):
    deque.insert(0, int(num))


def pop_front(deque):
    if len(deque) == 0:
        return -1
    else:
        return deque.pop(0)


def pop_back(deque):
    if len(deque) == 0:
        return -1
    else:
        return deque.pop(len(deque) - 1)


def size(deque):
    return len(deque)


def empty(deque):
    if len(deque) == 0:
        return 1
    else:
        return 0

def back(deque):
    if len(deque) == 0:
        return -1
    else:
        return deque[len(deque) - 1]


def front(deque):
    if len(deque) == 0:
        return -1
    else:
        return deque[0]


for i in range(0, len(commans)):
    if commans[i][0] == 'push_front':
        push_front(deque,commans[i][1])
    elif commans[i][0] == 'push_back':
        push_back(deque,commans[i][1])
    elif commans[i][0] == 'pop_front':
        print(pop_front(deque))
    elif commans[i][0] == 'pop_back':
        print(pop_back(deque))
    elif commans[i][0] == 'size':
        print(size(deque))
    elif commans[i][0] == 'empty':
        print(empty(deque))
    elif commans[i][0] == 'front':
        print(front(deque))
    elif commans[i][0] == 'back':
        print(back(deque))
