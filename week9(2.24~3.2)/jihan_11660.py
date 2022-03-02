import sys
rl = sys.stdin.readline
N, M = map(int, rl().split())
field = []
for _ in range(N):
    field.append(list(map(int, rl().split())))
coords = []
for _ in range(M):
    coords.append(list(map(int, rl().split())))

sum_field = [[0 for _ in range(N)]for _ in range(N)]

sum_field[0][0] = field[0][0]


def get_sum(y, x):
    a = field[y][x]
    b = sum_field[y][x-1]
    c = sum_field[y-1][x]
    d = sum_field[y-1][x-1]
    if x == 0:
        b = 0
        d = 0
    if y == 0:
        c = 0
        d = 0
    return a + b + c - d


for i in range(N):
    for j in range(N):
        sum_field[i][j] = get_sum(i, j)


def sol(x1, y1, x2, y2):
    a = sum_field[y2][x2]
    b = sum_field[y2][x1-1]
    c = sum_field[y1-1][x2]
    d = sum_field[y1-1][x1-1]
    if x2 == 0 or x1 == 0:
        b = 0
        d = 0
    if y2 == 0 or y1 == 0:
        c = 0
        d = 0
    return a - b - c + d


for i in coords:
    print(sol(i[1]-1, i[0]-1, i[3]-1, i[2]-1))
