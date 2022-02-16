n = int(input())

stair = [0] * 300
for i in range(n) :
    stair[i] = (int(input()))
    
dscore = [0] * 300
dscore[0] = (stair[0])
dscore[1] = (stair[0] + stair[1])
dscore[2] = max(stair[0] + stair[2], stair[1] + stair[2])
for i in range(3, n) :
    dscore[i] = max(dscore[i-2], dscore[i-3] + stair[i-1]) + stair[i]
    
print(dscore[n-1])