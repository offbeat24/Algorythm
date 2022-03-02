from collections import defaultdict, deque
import copy


class Node:
    def __init__(self, item):
        self.item = item
        self.child = list()

    def __str__(self):
        return str(self.data)

class binary_tree() :
    def __init__(self) :
        self.root = None
    
def find_child(node) :
    global node_arr
    child_node_arr = node.child
    children = deque()
    for i in child_node_arr :
        for key, value in node_arr.items() :
            if value == i :
                children.append(key)
                break
            
        
    return children
        
        

def dfs(start_num) :
        visited = list()
        need_visited = deque()
        need_visited.append(start_num)
        global node_arr
        while need_visited :
            start_node = need_visited.popleft()
            if start_node not in visited :
                visited.append(start_node)
                need_visited.extend(find_child(node_arr[start_node]))
                
        return visited
        

input_case = list()
case = deque()
answer = list()
while True:
    branch_ = list(map(int, input().rstrip().split()))
    input_case += branch_

    if input_case[-1] < 0:
        input_case.pop()
        input_case.pop()
        break


def tree_pot():
    tmp_case = deque()
    for i in range(0, len(input_case)-1, 2):
        if input_case[i] != 0 and input_case[i+1] != 0:
            tmp_case.append(input_case[i])
            tmp_case.append(input_case[i+1])
        else:
            tmp_case.append(input_case[i])
            tmp_case.append(input_case[i+1])
            case.append(copy.deepcopy(tmp_case))
            tmp_case.clear()


tree_pot()
case_cnt = 0

while case:
    test_case = case.popleft()
    if test_case == deque([0, 0]):
        answer.append(True)
        continue
    else :
        test_case.pop()
        test_case.pop()
    test_case_set = set(test_case)
    node_arr = dict()
    for i in test_case_set:
        node_arr[i] = Node(i)

    while test_case:
        node_arr[test_case.popleft()].child.append(
            node_arr[test_case.popleft()])

    tmp = list()
    for num in test_case_set:
        flag = 0
        for node_ in node_arr.values():
            if node_arr[num] in node_.child:
                flag += 1
                if flag > 1:
                    tmp.append(False)
                    tmp.append(False)
                    break
        if not flag:
            tmp.append(num)
    if len(tmp) != 1:
        answer.append(False)
        continue
    else:
        tree_ = binary_tree()
        r = tmp.pop()
        tree_.root = node_arr[r]
        visited = dfs(r)
        for i in test_case_set :
            if i not in visited :
                answer.append(False)
                break
        else:
            answer.append(True)
        


for i in range(len(answer)):
    if answer[i]:
        print("Case", i+1, "is a tree.", sep=" ")
    else:
        print("Case", i+1, "is not a tree.", sep=" ")
