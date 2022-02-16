from collections import Counter

list = []

for i in range(int(input())):
    list.append(int(input()))

list.sort()

print(round(sum(list)/len(list)))

print(list[len(list)//2])

cnt = Counter(list).most_common(2)
if len(cnt)>1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(list) - min(list))