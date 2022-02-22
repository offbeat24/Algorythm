
def two_pointer():
    global arr
    ans = n + 1
    l = 0
    r = 0
    sum = arr[0]
    while l < len(arr) and r < len(arr):
        if sum >= s:
            sum -= arr[l]
            ans = min(ans, r-l+1)
            l += 1
        else:
            r += 1
            try:
                sum += arr[r]
            except:
                break
    if ans == n+1:
        print(0)
    else:
        print(ans)


n, s = map(int, input().split())

arr = list(map(int, input().split()))

two_pointer()
