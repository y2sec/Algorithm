# 1991 트리 순회

# 전위 순회
def preorder(tree, node):
    print(node, end="")

    if tree[node][0] != '.':
        preorder(tree, tree[node][0])

    if tree[node][1] != '.':
        preorder(tree, tree[node][1])


# 중위 순회
def inorder(tree, node):
    if tree[node][0] != '.':
        inorder(tree, tree[node][0])

    print(node, end="")

    if tree[node][1] != '.':
        inorder(tree, tree[node][1])


# 후위 순회
def postorder(tree, node):
    if tree[node][0] != '.':
        postorder(tree, tree[node][0])

    if tree[node][1] != '.':
        postorder(tree, tree[node][1])

    print(node, end="")


tree = dict()

n = int(input())

for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = (left, right)

preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')
