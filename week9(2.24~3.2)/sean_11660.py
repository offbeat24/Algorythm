from collections import deque
import sys


n, m = map(int, sys.stdin.readline().split())

table = list()
for _ in range(n) :
    row_dq = deque(map(int, sys.stdin.readline().split()))
    sum = 0
    row = [0]
    while row_dq :
        sum += row_dq.popleft()
        row.append(sum)
    table.append(row)

for _ in range(m) :
    x_1, y_1, x_2, y_2 = map(int, sys.stdin.readline().split())
    sum =0
    for i in range(x_1 -1, x_2) :
        sum += (table[i][y_2] - table[i][y_1 - 1])
    
    print(sum)
        

