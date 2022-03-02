import sys;rl=sys.stdin.readline

N,M = map(int,rl().split())

grade = []
for _ in range(N):
    name, edge = rl().rstrip().split()
    edge = int(edge)
    if grade and edge == grade[-1][1]:
        continue
    grade.append([name, edge])

def getIndex(num):
    left = 0
    right = len(grade)-1
    while left<=right:
        mid = (left+right)//2
        if grade[mid][1] < num:
            left = mid + 1
        else:
            right = mid - 1
    return grade[right+1][0]

for char in range(M):
    tmp = int(rl())
    print(getIndex(tmp))