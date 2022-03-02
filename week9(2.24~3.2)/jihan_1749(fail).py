import sys;rl=sys.stdin.readline

N,M = map(int,rl().split())
field = []
for _ in range(N):
    field.append(list(map(int,rl().split())))

PSfield = [[0 for _ in range(M)] for _ in range(N)]
for row in range(N):
    for col in range(M):
        if row == 0 and col == 0:
            PSfield[row][col] = field[row][col]
        elif row == 0:
            PSfield[row][col] = field[row][col] + PSfield[row][col-1]
        elif col == 0:
            PSfield[row][col] = field[row][col] + PSfield[row-1][col]
        else:
            PSfield[row][col] = field[row][col] + PSfield[row-1][col] + PSfield[row][col-1] - PSfield[row-1][col-1]

def getSum(row1,col1,row2,col2):
    if row1 == 0 and col1 == 0:
        return PSfield[row2][col2]
    elif row1 == 0:
        return PSfield[row2][col2] - PSfield[row1][col1-1]
    elif col1 == 0:
        return PSfield[row2][col2] - PSfield[row1-1][col1]
    else:
        return PSfield[row2][col2] - PSfield[row1][col1-1] - PSfield[row1-1][col1] + PSfield[row1-1][col1-1]

Max = -10001
for row2 in range(N):
    for col2 in range(M):
        for row1 in range(row2):
            for col1 in range(col2):
                Max = max(getSum(row1,col1,row2,col2),Max)
print(Max)