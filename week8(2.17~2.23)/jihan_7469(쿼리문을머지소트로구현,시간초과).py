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

#1번노드부터 시작하여 원하는 범위가 노드에 노드가 가리키는 범위가 포함되는가를 검사하여 병합/반환.
def getSegment(nodeIndex,start,end):
    Segment = []
    left = MST[nodeIndex][0]
    right = MST[nodeIndex][1]
    if left > end or right < start:
        return Segment
    elif start<=left and right<=end:
        Segment = merge(Segment,MST[nodeIndex][2])
    else:
        Segment = merge(Segment,getSegment(nodeIndex*2,start,end))
        Segment = merge(Segment,getSegment(nodeIndex*2+1,start,end))
    return Segment

for _ in range(m):
    i,j,k = map(int,rl().split())
    print(getSegment(1,i,j)[k-1])