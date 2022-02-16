from collections import deque


num = int(input())

for _ in range(num):
    m, n, k = map(int, input().split())
    cab = list()
    xdq = deque()
    ydq = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for _ in range(k):
        cab.append(list(map(int, input().split())))

    bug = 0
    while cab:
        xdq.append(cab[0][0])
        ydq.append(cab[0][1])
        del cab[0]
        while xdq:
            for i in range(4):
                if [xdq[0]+dx[i], ydq[0]+dy[i]] in cab:
                    xdq.append(xdq[0]+dx[i])
                    ydq.append(ydq[0]+dy[i])
                    cab.remove([xdq[0]+dx[i], ydq[0]+dy[i]])
                    continue
            xdq.popleft()
            ydq.popleft()
        bug += 1
    print(bug)
