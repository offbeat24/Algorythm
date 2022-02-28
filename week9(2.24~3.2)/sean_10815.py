import copy


n = int(input())

cards = list(map(int, input().split()))

m = int(input())

test_ = list(map(int, input().split()))

data = copy.deepcopy(cards)

data.sort()


def binary_search(target):

    l = 0
    r = n - 1

    while l <= r:
        mid = (l+r) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return 0


for num in test_:
    print(binary_search(num), end=' ')
