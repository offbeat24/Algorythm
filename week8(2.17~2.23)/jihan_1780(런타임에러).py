import sys
sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())
ansm1=0
ans0=0
ans1=0
paper = []
for _ in range(N):
    paper+=list(map(int,sys.stdin.readline().split()))

def confirm(c_paper,value):
    if len(set(c_paper)) == 1 and c_paper[0] == value:
        return True

def sol(s_paper,length):
    if confirm(s_paper,-1):
        global ansm1
        ansm1+=1
    elif confirm(s_paper,0):
        global ans0
        ans0+=1
    elif confirm(s_paper,1):
        global ans1
        ans1+=1
    else:
        for i in range(9):
            leng = length//3
            idx = 3*leng*((i+1)//3)+leng*(i%3)
            cutted = []
            for j in range(leng):
                cutted+=s_paper[idx+j*3*leng:idx+leng+j*3*leng]
            sol(cutted,leng)

sol(paper,N)
print(ansm1)
print(ans0)
print(ans1)