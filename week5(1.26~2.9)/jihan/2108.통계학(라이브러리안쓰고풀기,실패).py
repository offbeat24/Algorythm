from collections import Counter

def average(list):
    tmp = 0
    for i in range(0,len(list)):
       tmp+=list[i]
    tmp/=len(list)
    if tmp<0:
        return int(tmp)-1
    else:
        return int(tmp)

def middle_value(list):
    tmp_list = sorted(list)
    mid = int(len(list)/2)
    tmp = 0
    if len(list)%2==0: #리스트 길이가 짝수일 경우
        tmp = tmp_list[mid] + tmp_list[mid+1]
        tmp/=2
    else: #리스트 길이가 홀수일 경우
        tmp = tmp_list[mid]
    return tmp

def mode(list):
    cnt_list = [0 for i in range(8001)]
    for i in list:
        cnt_list[i+4000]+=1
    max = 0
    for i in cnt_list:
        if i>max:
            max = i
    tmp_list = []
    for i in range(0,8001):
        if cnt_list[i] == max:
            tmp_list.append(i-4000)
    
    if len(tmp_list)<2:
        return tmp_list[0]
    else:
        tmp_list.sort()
        return tmp_list[1]

def interval(list):
    min = 4000
    max = -4000
    tmp = 0
    for i in range(0,len(list)):
        if list[i] > max :
            max = list[i]
        if list[i] < min :
            min = list[i]
    
    tmp = max - min
    return tmp

n = int(input())
list = []
for i in range(n):
    list.append(int(input()))

print(average(list))
print(middle_value(list))
print(mode(list))
print(interval(list))