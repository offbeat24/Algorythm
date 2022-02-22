import math
import sys


n, k = map(int, input().split())


isNotSorted = list(map(int, input().split()))
count = 0
count_answer = 0


def merge_sort(arr):
    global count
    global count_answer
    if len(arr) < 2:
        return arr
    mid = math.ceil(len(arr) / 2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    temp_arr = list()

    l = r = 0
    while l < len(left) and r < len(right):
        tmp = 0
        if left[l] < right[r]:
            tmp = left[l]
            count += 1
            l += 1
        else:
            tmp = right[r]
            count += 1
            r += 1
        temp_arr.append(tmp)
        if count == k:
            print(tmp)
            sys.exit()

    temp_arr += left[l:]
    count += len(left[l:])
    temp_arr += right[r:]
    count += len(right[r:])

    if count >= k:
        print(temp_arr[len(temp_arr)-(count-k)-1])
        sys.exit()
    return temp_arr


merge_sort(isNotSorted)

print(-1)
