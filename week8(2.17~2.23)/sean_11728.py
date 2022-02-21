n, m = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

a_point = 0

b_point = 0

answer = list()

while a_point < len(a) and b_point < len(b):
    if a[a_point] < b[b_point]:
        answer.append(a[a_point])
        a_point += 1
    else:
        answer.append(b[b_point])
        b_point += 1

answer += a[a_point:]
answer += b[b_point:]

for i in answer:
    print(i, end=' ')
