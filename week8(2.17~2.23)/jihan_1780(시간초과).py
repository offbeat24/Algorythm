import sys
import math
N = int(sys.stdin.readline())
ansm1 = 0
ans0 = 0
ans1 = 0
paper = []
for _ in range(N):
    paper.append(list(map(int,sys.stdin.readline().split())))

def confirm(c_paper,c_leng):
    tmp = [[-1 for _ in range(c_leng)]for _ in range(c_leng)]
    if c_paper == tmp:
        return -1
    tmp = [[0 for _ in range(c_leng)]for _ in range(c_leng)]
    if c_paper == tmp:
        return 0
    tmp = [[1 for _ in range(c_leng)]for _ in range(c_leng)]
    if c_paper == tmp:
        return 1
    return 2

start = [[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]
end = [[1,1],[2,1],[3,1],[1,2],[2,2],[3,2],[1,3],[2,3],[3,3]]

def sol(paper):
    leng = len(paper[0])
    paper_value = confirm(paper,leng)
    if paper_value == -1 :
        global ansm1
        ansm1+=1
    elif paper_value == 0 :
        global ans0
        ans0+=1
    elif paper_value == 1 :
        global ans1
        ans1+=1
    else:
        leng = int(leng/3)
        for i in range(9):
            tmp_paper = []
            start_x,start_y = int(start[i][0]*leng),int(start[i][1]*leng)
            end_x,end_y = int(end[i][0]*leng-1),int(end[i][1]*leng-1)
            for i in range(start_y,end_y+1):
                 tmp_paper.append(paper[i][start_x:end_x+1])
            sol(tmp_paper)

sol(paper)
print(ansm1)
print(ans0)
print(ans1)