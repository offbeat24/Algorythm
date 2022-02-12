import sys

N, M, B = map(int,sys.stdin.readline().split())
maps = []
for i in range(N):
    maps.append(list(map(int,sys.stdin.readline().split())))
min = 999999999999999999
min_i = 0

for i in range(0,257):
    up = 0
    down = 0
    for j in maps:
        for k in j:
            if k > i:
                down+=(k-i)
            elif k < i:
                up+=(i-k)
    bag = B + down - up
    time = (down*2) + up
    if bag >= 0:
        if min>=time:
            min = time
            min_i = i

print(min,min_i)