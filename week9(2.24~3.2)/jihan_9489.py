import sys;rl=sys.stdin.readline

class Node():
    def __init__(self,item:int,parent):
        self.item = item
        self.parent = parent
        self.child = []

class Tree():
    def __init__(self,root):
        self.root = root

while 1:
    inputLine = list(map(int,rl().split()))
    if inputLine == [0,0]:
        break
    else:
        n,k = inputLine
        items = list(map(int,rl().split()))
        #노드가 1개 밖에 없는 경우 예외처리
        if n == 1:
            print(0)
            continue
        nodes = [Node(items[0],-1)]
        tmp = [items[1]]
        tree = Tree(nodes[0]) # 첫 번째 노드를 루트로 하는 트리 생성
        NonChildNodeIndex = 0
        for i in range(2,n):
            # i번째 노드가 앞의 노드와 연속되지 않았다면, 모아놓은 형제집합을 자식이 없는 노드의 자식으로 배정하고, 새로운 형제집합 수집
            if items[i] > items[i-1]+1:
                nodes[NonChildNodeIndex].child = tmp
                for childItem in tmp:
                    nodes.append(Node(childItem,nodes[NonChildNodeIndex]))
                    tmp = []
                NonChildNodeIndex+=1
            tmp.append(items[i])
        #마지막 아이템까지 확인한 뒤, tmp를 한 번 더 비워줌.
        nodes[NonChildNodeIndex].child = tmp
        for childItem in tmp:
            nodes.append(Node(childItem,nodes[NonChildNodeIndex]))
        
        #TEST PRINT
        #for node in nodes:
        #    print('nodeItem: ',node.item,'nodeParent: ',node.parent,'nodeChild: ',node.child)
        
        cntCousin = 0
        targetIndex = items.index(k)
        target = nodes[targetIndex]
        try:
            # 타겟 node의 parent의 parent의 child의 item 리스트를 가져옴
            targetGrandsChildren = ((target.parent).parent).child
            # item리스트를 순회하며, 타겟 node의 parent와 item이 같지 않으면(형제이면) 그 node의 자식들의 수를 카운트하여 출력 (해당 과정에서 index함수를 사용하지 않도록 구현하였으면 시간을 많이 절약할 수 있을 것 같음.)
            for targetGrandsChild in targetGrandsChildren:
                if targetGrandsChild != (target.parent).item:
                    childIndex = items.index(targetGrandsChild)
                    cntCousin+=len(nodes[childIndex].child)
            print(cntCousin)
        except:
            print(0)