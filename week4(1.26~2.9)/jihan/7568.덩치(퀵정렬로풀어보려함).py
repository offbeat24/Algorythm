def quick_sort(array, index, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left][index] <= array[pivot][index]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right][index] >= array[pivot][index]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, index, start, right - 1)
    quick_sort(array, index, right + 1, end)

n = int(input())
list = []
for i in range(0,n):
    a,b = map(int,input().split())
    list.append([i+1,a,b])

quick_sort(list,1,0,n-1)
list[0].append(0)

for i in range(0,n):
    cnt = 0
    if i != 0:
        for j in range(0,i):
            if list[i][2] < list[j][2]:
                cnt+=1
    list[i].append(cnt)
    

# quick_sort(list,0,0,n-1)

print(list)