n = int(input())
list = []

for i in range(0,n):
    tmp = input().split(' ')
    if any(list): #list가 비어있지않다면
        for j in range(0,len(list)):
            if int(list[len(list)-j-1][0])<=int(tmp[0]):
                list.insert(len(list)-j,tmp)
                break
            elif j == len(list)-1:
                list.insert(0,tmp)
                break
    else: #list가 비어있다면
        list.append(tmp)

print(list)