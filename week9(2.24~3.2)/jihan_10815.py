import sys;rl=sys.stdin.readline

N = int(rl())
have = list(map(int,rl().split()))
M =int(rl())
find = list(map(int,rl().split()))
ans = []

def binarySearch(num):
  left = 0
  right = N-1
  mid = (left + right) // 2
  while left < right:
    if have[mid] < num:
      left = mid + 1
    elif have[mid] > num:
      right = mid - 1
    else: break
    mid = (left+right)//2
  if have[mid] == num:
    return True
  return False
  
have.sort()

for target in find:
  if binarySearch(target):
    ans.append("1")
  else:
    ans.append("0")

print(' '.join(ans))