#파라메트릭서치,머지소트트리,세그먼트트리
from math import ceil, log2
import sys;rl = sys.stdin.readline
n,m = map(int,rl().split())
An = list(map(int,rl().split()))
leafLevel = int(log2(n))+1

#왼쪽리스트와 오른쪽리스트를 입력하면 머지소트된 리스트를 반환하는 함수
def merge(leftList:list,rightList:list):
    rtnList = []
    leftIter = 0
    rightIter = 0
    while leftIter < len(leftList) and rightIter < len(rightList):
        if leftList[leftIter] < rightList[rightIter]:
            rtnList.append(leftList[leftIter])
            leftIter+=1
        else:
            rtnList.append(rightList[rightIter])
            rightIter+=1
    rtnList+=leftList[leftIter:]
    rtnList+=rightList[rightIter:]
    return rtnList

#입력 리스트를 리프노드 레벨에 초기화시킨 후 부모를 따라가면서 노드를 채워주는 형태
#리프노드의 n번째 이후 노드가 구간값을 가질 수 있도록 설정해야함에 주의.
def init():
    for i in range(2**leafLevel):
        MST[(2**leafLevel)+i][0] = MST[(2**leafLevel)+i][1] = i+1
    for i in range(n):
        MST[(2**leafLevel)+i][2].append(An[i])
    level = leafLevel-1
    while level>=0:
        for i in range(2**level,2**(level+1)):
            MST[i][0] = MST[i*2][0]
            MST[i][1] = MST[i*2+1][1]
            MST[i][2] = merge(MST[i*2][2],MST[i*2+1][2])
        level-=1
MST = [[0,0,[]] for _ in range(2**(leafLevel+1))]
#MST의 노드는 [구간시작,구간끝,[자식노드 머지한 리스트]] 형태.
MST[0] = None
init()

#노드에서 x보다 큰 원소가 나오는 첫 번째 위치를 반환.
def upperBound(x,nodeIndex):
    left = 0
    right = len(MST[nodeIndex][2])-1
    mid = 0
    while left<right:
        if MST[nodeIndex][2][mid]<=x:
            left = mid + 1
        else:
            right = mid
        mid = (left+right)//2
        if mid == right:
            if MST[nodeIndex][2][mid] <= x:
                return len(MST[nodeIndex][2])
            else:
                return right
    if MST[nodeIndex][2][left] > x:
        return 0
    return left + 1

#목표가 (start~end), 노드의 구간이 (left~right)
#start부터 end까지의 구간에서 x라는 수보다 작은 수의 개수가 몇 개인가요?
#라는 질의를 1번 노드부터 재귀하여 리턴함.
#만약에 노드의 구간이 목표의 구간에 포함된다면, 노드의 리스트에서
#x보다 큰 가장 작은 수의 인덱스를 리턴함(upperBound). 이는 리스트 안의 인덱스이므로
#x보다 작은 수의 개수라고 할 수 있음.
#그리고 이를 모두 더하면, 목표 구간에 포함되는 모든 노드 내에서의 x보다 작은 수의 개수가 됨.
def query(x,start,end,nodeIndex): 
    left = MST[nodeIndex][0]
    right = MST[nodeIndex][1]
    if left > end or right < start:
        return 0
    elif start<=left and right<=end:
        return upperBound(x,nodeIndex)
    return query(x,start,end,nodeIndex*2)+query(x,start,end,nodeIndex*2+1)

#목표 구간에 포함되는 모든 노드의 리스트 내에서의 x보다 작은 수의 개수가 k-1개가 됐을 때,
#x값이 목표 구간 안에서 k번째 수의 값이 됨. 비교연산에 따라 start가 그 값이 되면,
#start는 더 이상 증가하지 않고 end만 감소하다가 start와 end의 대소가 역전되고 while문 탈출.
for _ in range(m):
    i,j,k = map(int,rl().split())
    start = -(10**9)
    end = 10**9
    while start<=end:
        mid = (start+end)//2
        result = query(mid,i,j,1)
        if result<k:
            start = mid + 1
        else:
            end = mid - 1
    print(start)
    