import sys

num = int(sys.stdin.readline())

stairs = list(int(sys.stdin.readline()) for _ in range(num))

table = [[0,0] for _ in range(num)] # table : [[a,b]] a는 전 계단을 밞은 상태
                                    #   b는 전 계단을 안밟은 상태
table[0][0] = table[0][1] = stairs[0]
table[1][0] = stairs[0] + stairs[1]
table[1][1] = stairs[1]

for i in range(2, num):
  if(num - i) % 3 == 1:
    table[i][0] = table[i-1][1] + stairs[i]
    table[i][1] = max(table[i-2]) + stairs[i] ##헷갈린다?
  if(num - i) % 3 == 2:
    table[i][0] = 0
    table[i][1] = max(table[i-2]) + stairs[i] ##헷갈린다?
  if(num - i) % 3 == 0:
    table[i][0] = table[i-1][1] + stairs[i]
    table[i][1] = max(table[i-2]) + stairs[i] ##헷갈린다?

print(table)
print(max(table[num-1]))

"""
memo = [0] * num
memo[0] = stairs[0]
memo[1] = stairs[0] + stairs[1]
memo[2] = max(stairs[0], stairs[1]) + stairs[2]
for i in range(3, num):
  #memo[i] = max(stairs[i-1], stairs[i-2]) + stairs[i]
  if (num - i) % 3 == 1:
    memo[i] = max(memo[i-1], memo[i-2]) + stairs[i]
    #memo[i] = memo[i-2] + stairs[i]
  if (num - i) % 3 == 2:
    memo[i] = memo[i-2] + stairs[i]
  if (num - i) % 3 == 0:
    memo[i] = max(memo[i-1], memo[i-2]) + stairs[i]

print(memo)  #[10,30,35,55,65,75]
print(memo[num-1])
"""
