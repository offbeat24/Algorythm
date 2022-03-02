from collections import deque

class Node():
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)
n9 = Node(90)

class BinaryTree():
    def __init__(self):
        self.root = None
    #전위 순회 
    def preorder(self, n):
        if n != None:
            print(n.item, "", end = '')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
    #후위순회
    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(n.item, "", end = '')
    #중위 순회
    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(n.item, "", end="")
            if n.right:
                self.inorder(n.right)
    #레벨 순회
    def levelorder(self, n):
        if n != None:
            queue = deque()
            queue.append(n)
            while queue:
                tmpNode = queue.popleft()
                if tmpNode != None:
                    print(tmpNode.item, "", end="")
                    queue.append(tmpNode.left)
                    queue.append(tmpNode.right)

tree = BinaryTree()
tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8

tree.preorder(tree.root)
tree.postorder(tree.root)
tree.inorder(tree.root)
tree.levelorder(tree.root)