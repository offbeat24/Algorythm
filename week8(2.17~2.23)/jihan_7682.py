import sys; rl = sys.stdin.readline
input = ''

board = [0 for _ in range(9)] #0은 비어있음, 1은 'X', 2는 'O'
flag = 0
win = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

def gameover():
    for case in win:
        if board[case[0]-1] != 0 and board[case[1]-1] != 0 and board[case[2]-1] != 0:
            if board[case[0]-1] == board[case[1]-1] == board[case[2]-1]:
                return True
    return False

def tictactoe(string,num,cnt_piece):
    global flag
    if num == cnt_piece:
        if gameover() or cnt_piece==9:
            flag = 1
            return
        else:
            flag = 0
            return
    if gameover():
        return
    for i in range(9):
        if string[i] == 'X' and num%2 == 0 and board[i] == 0:
            board[i] = 1
            tictactoe(string,num+1,cnt_piece)
            if flag == 1: return 'valid'
            board[i] = 0
        elif string[i] == 'O' and num%2 == 1 and board[i] == 0:
            board[i] = 2
            tictactoe(string,num+1,cnt_piece)
            if flag == 1: return 'valid'
            board[i] = 0
    return 'invalid'
        
def sol(string):
    cntO, cntX = 0, 0
    for i in string:
        if i == 'O': cntO+=1
        elif i == 'X': cntX+=1
    if cntO<=cntX<=cntO+1 and 0<=cntO<=4 and 0<=cntX<=5:
        return tictactoe(string,0,cntO+cntX)
    else:
        return 'invalid'
    
while 1:
    input = rl().rstrip()
    board = [0 for _ in range(9)]
    if input == 'end':
        break
    flag = 0
    print(sol(input))