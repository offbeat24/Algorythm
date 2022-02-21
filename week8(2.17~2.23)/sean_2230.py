n, m = map(int, input().split())

arr = list()
for _ in range(n):
    arr.append(int(input()))

arr.sort()
l = 0
r = 1
ans = float('inf')

while r < n:
    if arr[r] - arr[l] < m:
        r += 1
    else:
        ans = min(ans, arr[r] - arr[l])
        l += 1

print(ans)
