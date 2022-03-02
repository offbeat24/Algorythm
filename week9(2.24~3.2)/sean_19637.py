import sys


n, m = map(int, sys.stdin.readline().split())

title_ = list()
scale_ = list()

for _ in range(n):
    name, num = sys.stdin.readline().split()
    title_.append(name)
    scale_.append(int(num))


def level(target):
    l = 0
    r = n-1

    while l <= r:
        mid = (l+r) // 2

        if scale_[mid] < target:
            l = mid + 1
            mid = l
        else:
            r = mid - 1

    return mid


for _ in range(m):
    ap = int(sys.stdin.readline())

    print(title_[level(ap)])
