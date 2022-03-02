class Node:
    def __init__(self, item):
        self.item = item
        self.child = None

    def __str__(self):
        return str(self.data)


class BinaryTree():
    def __init__(self):
        self.root = None

    def make_child(self, node, kid):
        if node.child == None:
            node.child = [kid]
        else:
            node.child.append(kid)

    def leaf(self, node):
        leaves = 0
        if node.child == None:
            return 1
        else:
            for green in node.child:
                leaves += self.leaf(green)
        return leaves

    def cut_leaf(self, node):
        node_dict[fam[cut]].child.remove(node_dict[cut])
        if len(node_dict[fam[cut]].child) == 0:
            node_dict[fam[cut]].child = None


tree = BinaryTree()

n = int(input())
fam = list(map(int, input().split()))
cut = int(input())
node_dict = dict()
answer = 0

for i in range(n):
    node_dict[i] = Node(i)

tree.root = node_dict[fam.index(-1)]

for i in range(n):
    if fam[i] != -1:
        tree.make_child(node_dict[fam[i]], node_dict[i])

if n == 1 or tree.root.item == cut:
    print(0)
else:
    tree.cut_leaf(node_dict[cut])
    answer += tree.leaf(tree.root)
    print(answer)
