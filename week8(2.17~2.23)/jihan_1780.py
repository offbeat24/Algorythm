import sys
ansm1 = 0
ans0 = 0
ans1 = 0
N = int(sys.stdin.readline())
paper = []
for _ in range(N):
    paper.append(list(map(int,sys.stdin.readline().split())))

def confirm(start_x,start_y,end_x,end_y):
    global paper
    tmp = []
    for i in range(start_y,end_y+1):
        tmp+=paper[i][start_x:end_x+1]
    if len(set(tmp)) == 1:
        if tmp[0] == -1:
            return -1
        if tmp[0] == 0:
            return 0
        if tmp[0] == 1:
            return 1
    else:
        return 2

start = [[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]
end = [[1,1],[2,1],[3,1],[1,2],[2,2],[3,2],[1,3],[2,3],[3,3]]

def sol(start_x,start_y,end_x,end_y,s_length):
    tmp = confirm(start_x,start_y,end_x,end_y)
    if tmp == -1:
        global ansm1
        ansm1+=1
    elif tmp == 0:
        global ans0
        ans0+=1
    elif tmp == 1:
        global ans1
        ans1+=1
    else:
        length = int(s_length//3)
        for i in range(9):
            sol(start_x+start[i][0]*length,start_y+start[i][1]*length,start_x+end[i][0]*length-1,start_y+end[i][1]*length-1,length)

sol(0,0,N-1,N-1,N)
print(ansm1)
print(ans0)
print(ans1)