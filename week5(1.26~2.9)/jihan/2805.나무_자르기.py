import sys
N, M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

def get_rmd(trees,height):
    tmp = list(map(lambda x:x-height,trees))
    sum = 0
    for i in tmp:
        if i>0:
            sum+=i
    return sum

high = max(trees)
low = 1

while low<=high:
    mid = (high+low)//2
    rmd = get_rmd(trees,mid)

    if rmd >= M:
        low = mid + 1
    else:
        high = mid - 1

print(high)