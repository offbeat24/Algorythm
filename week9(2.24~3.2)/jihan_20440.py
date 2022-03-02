import sys
rl = sys.stdin.readline
N = int(rl())
mosIn = []
mosOut = []    
for _ in range(N):
    In,Out = map(int,rl().split())
    mosIn.append(In)
    mosOut.append(Out)

mosIn.sort()
mosOut.sort()
ranges = []

inIter = outIter = rangeStart = rangeEnd = 0
preCnt = nowCnt = maxCnt = 0

while inIter < N:
    if mosIn[inIter] < mosOut[outIter]:
        preCnt = nowCnt
        nowCnt +=1
        rangeStart = rangeEnd
        rangeEnd = mosIn[inIter]
        inIter+=1
    elif mosIn[inIter] > mosOut[outIter]:
        preCnt = nowCnt
        nowCnt -=1
        rangeStart = rangeEnd
        rangeEnd = mosOut[outIter]
        outIter+=1
    else:
        inIter+=1
        outIter+=1
        continue
    maxCnt = max(maxCnt,nowCnt)
    ranges.append([rangeStart,rangeEnd,preCnt])

while outIter < N:
    preCnt = nowCnt
    nowCnt -=1
    rangeStart = rangeEnd
    rangeEnd = mosOut[outIter]
    outIter+=1
    ranges.append([rangeStart,rangeEnd,preCnt])

for node in ranges:
    start,end,cnt = node
    if cnt == maxCnt:
        print(cnt)
        print(start,end)
        break