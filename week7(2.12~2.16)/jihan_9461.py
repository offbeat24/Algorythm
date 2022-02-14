import sys
import math

T = int(sys.stdin.readline())
li_N = []

for i in range(T):
    li_N.append(int(sys.stdin.readline()))

li = [1,1,1,2,2]
max_of_N = max(li_N)

if max_of_N>5:
    for i in range(5,max_of_N):
        li.append(li[i-1]+ li[i-5])

for i in li_N:
    print(li[i-1])