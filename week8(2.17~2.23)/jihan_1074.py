import sys
N,r,c = list(map(int,sys.stdin.readline().split()))

length = 2**N
ans = 0

def sol(x,y,start_x,start_y,length):
    global ans
    if start_x == x and start_y == y:
        return
    if start_x<=x<=start_x+length//2-1 and start_y<=y<=start_y+length//2-1: #1사분면일 경우
        sol(x,y,start_x,start_y,length//2)
    if start_x+length//2<=x<=start_x+length-1 and start_y<=y<=start_y+length//2-1: #2사분면일 경우
        ans+=(length//2)**2
        sol(x,y,start_x+length//2,start_y,length//2)
    if start_x<=x<=start_x+length//2-1 and start_y+length//2<=y<=start_y+length-1: #3사분면일 경우
        ans+=((length//2)**2)*2
        sol(x,y,start_x,start_y+length//2,length//2)
    if start_x+length//2<=x<=start_x+length-1 and start_y+length//2<=y<=start_y+length-1: #4사분면일 경우
        ans+=((length//2)**2)*3
        sol(x,y,start_x+length//2,start_y+length//2,length//2)

sol(c,r,0,0,length)
print(ans)