import sys  #DP, 일반항 dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
import math

n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))

casecnt = [1,2,4]

for i in range(3,max(li)):
    casecnt.append(casecnt[i-1]+casecnt[i-2]+casecnt[i-3])

for i in li:
    print(casecnt[i-1])