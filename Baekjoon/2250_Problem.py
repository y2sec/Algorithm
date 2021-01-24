# 2250 트리의 높이와 너비

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def findLevel(node):
    level = 1
    while node != parent[node]:
        level += 1
        node = parent[node]
    return level


def inorder(node):
    global row
    if tree[node].left != -1:
        inorder(tree[node].left)

    level_rows[findLevel(node)].append(row)
    row += 1

    if tree[node].right != -1:
        inorder(tree[node].right)


tree = dict()
n = int(input())
parent = [x for x in range(n + 1)]
row = 1
for _ in range(n):
    data, left, right = map(int, input().split())
    if left != -1:
        parent[left] = data
    if right != -1:
        parent[right] = data
    tree[data] = Node(data, left, right)

max_level = 0
start = 0

for data in range(1, n + 1):
    level = findLevel(data)
    if level == 1:
        start = data
    max_level = max(max_level, level)

level_rows = [[] for _ in range(max_level + 1)]
inorder(start)
result_level = 0
result_width = 0
for level in range(1, len(level_rows)):
    width = max(level_rows[level]) - min(level_rows[level]) + 1
    if result_width < width:
        result_width = width
        result_level = level

print(result_level, result_width)
