from math import ceil
import sys;rl=sys.stdin.readline

N,K = map(int,rl().split())
An = list(map(int,rl().split()))
ans = []

def merge(leftList:list,rightList:list):
    rtnList = []
    leftIter = 0
    rightIter = 0
    while leftIter < len(leftList) and rightIter < len(rightList):
        if leftList[leftIter] < rightList[rightIter]:
            rtnList.append(leftList[leftIter])
            ans.append(leftList[leftIter])
            leftIter+=1
        else:
            rtnList.append(rightList[rightIter])
            ans.append(rightList[rightIter])
            rightIter+=1
    while leftIter < len(leftList):
        rtnList.append(leftList[leftIter])
        ans.append(leftList[leftIter])
        leftIter+=1
    while rightIter < len(rightList):
        rtnList.append(rightList[rightIter])
        ans.append(rightList[rightIter])
        rightIter+=1
    return rtnList

def merge_sort(List:list):
    if len(List) == 1:
        return List
    mid = int(ceil(len(List)/2))
    leftList = merge_sort(List[:mid])
    rightList = merge_sort(List[mid:])
    return merge(leftList,rightList)

merge_sort(An)
if K>=len(ans):
    print(-1)
else:
    print(ans[K-1])