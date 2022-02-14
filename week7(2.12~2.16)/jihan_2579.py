#DP 중 굉장히 어려운 문제...였읍니다..
#D[i][j] = 현재까지 j개의 계단을 연속해서 밟고 i번째 계단까지 올라섰을 때 점수 합의 최댓값, 단 i번째 계단은 반드시 밟아야 함.
#https://blog.encrypted.gg/974
import sys
N = int(sys.stdin.readline())
stair = []
for _ in range(N):
    stair.append(int(sys.stdin.readline()))

if N == 1:
    print(stair[0])

else:
    D = [[stair[0],stair[0]],[stair[1],stair[0]+stair[1]]]

    for i in range(2,N):
        D.append([max((D[i-2][0],D[i-2][1]))+stair[i],D[i-1][0]+stair[i]])

    print(max(D[N-1][0],D[N-1][1]))