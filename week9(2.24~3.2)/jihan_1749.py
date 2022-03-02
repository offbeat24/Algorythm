import sys;rl=sys.stdin.readline
N,M = list(map(int,rl().split()))
field = [list(map(int,rl().split())) for _ in range(N)]
sumField = [[0 for _ in range(M+1)] for _ in range(N+1)]
#누적합 필드의 인덱스를 원래 필드보다 1씩 키워서 참조 예외처리를 줄임.

for row in range(N):
    for col in range(M):
        sumField[row+1][col+1] = field[row][col] + sumField[row+1][col] + sumField[row][col+1] - sumField[row][col]

def getSum(row1,col1,row2,col2):
    return sumField[row2+1][col2+1] - sumField[row2+1][col1] - sumField[row1][col2+1] + sumField[row1][col1]

Max = -10001

for row2 in range(N):
    for col2 in range(M):
        for row1 in range(row2+1):
            for col1 in range(col2+1):
                Max = max(Max,getSum(row1,col1,row2,col2))

print(Max)