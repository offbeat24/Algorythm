def two_point():
    global arr
    l = 0
    r = 0
    m = 0
    cnt = [0] * (max(arr) + 1)
    while l < len(arr) and r < len(arr):
        if cnt[arr[r]] >= k:
            cnt[arr[l]] -= 1
            l += 1
        else:
            cnt[arr[r]] += 1
            r += 1
        m = max(m, r - l)
    return m


n, k = map(int, input().split())

arr = list(map(int, input().split()))

print(two_point())
