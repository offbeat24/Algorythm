import sys

T = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(T)]

arr = [0] * 10
arr[0] = 1
arr[1] = 2
arr[2] = 4
for i in range(3, 10):
  arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

for num in nums:
  print(arr[num-1])
