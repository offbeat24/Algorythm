import sys

T = int(sys.stdin.readline())
Ns = list(int(sys.stdin.readline()) for _ in range(T))

arr = [0 for _ in range(max(Ns))]
arr[0] = arr[1] = arr[2] = 1
arr[3] = arr[4] = 2

for i in range(5, len(arr)):
  arr[i] = arr[i-1] + arr[i-5]

for n in Ns:
  print(arr[n - 1])
