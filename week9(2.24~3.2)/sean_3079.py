import sys


n, m = map(int, sys.stdin.readline().split())

mig = list()


for _ in range(n):
    mig.append(int(sys.stdin.readline()))


l = 0
r = max(mig) * m
while l <= r:

    mid = (l+r) // 2

    eff = 0
    for t in mig:
        eff += mid // t

    if eff < m:
        l = mid + 1
    else:
        answer = mid
        r = mid - 1

print(answer)
