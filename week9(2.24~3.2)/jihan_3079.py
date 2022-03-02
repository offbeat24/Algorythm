import sys;rl=sys.stdin.readline
N,M = map(int,rl().split())
imigration = []
for _ in range(N):
    imigration.append(int(rl()))
imigration.sort()

# 각 검사대의 필요시간으로 전체 시간을 나누면 그 몫이 '해당 검사대가 전체 시간동안 검사할 수 있는 인원의 수'가 된다. 모든 검사대에 대해 그 값을 더해주면, '전체 검사대가 전체 시간동안 검사할 수 있는 인원의 수'가 된다.
def complete(num):
    cnt = 0
    for i in range(N):
        cnt+=num//imigration[i]
    return cnt

left = min(imigration)
right = max(imigration) * M
while left<=right:
    mid = (left+right)//2
    if complete(mid) >= M:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)