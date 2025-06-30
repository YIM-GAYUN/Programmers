from collections import deque

# 노드 클래스 정의
class Node:
    def __init__(self, info, num, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right
        self.num = num
        
    def has_left(self):
        return self.left is not None
    
    def has_right(self):
        return self.right is not None
    
# 이진 트리 구축
def make_BT(nodeinfo):
    nodes = [i for i in range(1, len(nodeinfo) + 1)]
    nodes.sort(key=lambda x: (nodeinfo[x - 1][1], -nodeinfo[x - 1][0]), reverse=True)
    root = None
    for i in range(len(nodes)):
        if root is None:
            root = Node(nodeinfo[nodes[0] - 1], nodes[0])
        else:
            parent = root
            node = Node(nodeinfo[nodes[i] - 1], nodes[i])
            while True:
                if node.info[0] < parent.info[0]: # 왼쪽으로
                    if parent.has_left():
                        parent = parent.left
                        continue
                    parent.left = node
                    break
                else: # 오른쪽으로
                    if parent.has_right():
                        parent = parent.right
                        continue
                    parent.right = node
                    break
    return root

# preorder
def preorder(root, answer):
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        answer[0].append(node.num)
        stack.append(node.right)
        stack.append(node.left)
        
# postorder
def postorder(root, answer):
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if visited:
            answer[1].append(node.num)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
            
def solution(nodeinfo):
    answer = [[], []]
    root = make_BT(nodeinfo)
    preorder(root, answer)
    postorder(root, answer)
    return answer