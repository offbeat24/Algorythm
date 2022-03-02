import sys;rl=sys.stdin.readline
class Node():
    def __init__(self,item:int,childList:list,parent:int):
        self.item = item
        self.child = childList
        self.parent = parent

class Tree():
    def __init__(self,root):
        self.root = root
    def getLeafCnt(self,n:Node):
        if n!= None:
            if len(n.child)==0:
                return 1
            else:
                return sum(list(map(lambda x: self.getLeafCnt(nodes[x]),n.child)))
    def deleteNode(self,n:Node):
        if n!= None:
            del nodes[n.parent].child[nodes[n.parent].child.index(n.item)]

N = int(rl())
parents = list(map(int,rl().split()))

nodes = [Node(i,[],parents[i]) for i in range(N)]

for i in range(N):
    if parents[i] == -1:
        tree = Tree(i)
    else:
        nodes[parents[i]].child.append(i)

delete = int(rl())
if delete == tree.root:
    print(0)
else:
    tree.deleteNode(nodes[delete])
    if len(nodes[tree.root].child) == 0:
        print(1)
    else:
        print(tree.getLeafCnt(nodes[tree.root]))