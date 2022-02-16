import sys
from collections import Counter

for i in range(int(sys.stdin.readline())):
    N, M = map(int,sys.stdin.readline().split())
    data = list(map(int,sys.stdin.readline().strip().split()))
    max_value = max(data)
    cnt = 0
    cntlist = Counter(data)
    breaker = 0

    for i in range(max_value,0,-1):
        while cntlist[i]!=0:
            if data[0] != i:
                data.append(data.pop(0))
                M = (M-1+len(data))%len(data)
            else:
                if M == 0:
                    cnt+=1
                    breaker = 1
                    break
                else:
                    cnt+=1
                    del data[0]
                    cntlist[i]-=1
                    M-=1
        if breaker == 1 : break
    
    print(cnt)
