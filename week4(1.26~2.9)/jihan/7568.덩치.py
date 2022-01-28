n = int(input())
list = []
for i in range(0,n):
    a,b = map(int,input().split())
    list.append([a,b])

for i in range(0,n):
    cnt = 1
    for j in range(0,n):
        if i != j:
            if list[i][0] < list[j][0] and list[i][1] < list[j][1]:
                cnt+=1
    print(cnt)