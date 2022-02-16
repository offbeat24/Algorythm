from collections import Counter

n = int(input())
target = list(map(int,input().split()))
m = int(input())
finding = list(map(int,input().split()))

ans = ''
cnt = Counter(target)
for i in finding:
  if i in cnt:
    ans += str(cnt[i]) + ' '
  else:
    ans += '0 '

print(ans)