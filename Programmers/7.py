# 길 찾기 게임

import sys
sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.head = None

    def __add__(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else:
            currNode = self.head
            node = Node(data)
            while currNode is not None:
                if currNode.data[0] > data[0]:
                    if currNode.left is None:
                        currNode.left = node
                        break
                    else:
                        currNode = currNode.left
                else:
                    if currNode.right is None:
                        currNode.right = node
                        break
                    else:
                        currNode = currNode.right


def preorder(node, lst):
    currNode = node
    if node is None:
        return
    lst.append(currNode.data[2])
    preorder(currNode.left, lst)
    preorder(currNode.right, lst)


def postorder(node, lst):
    currNode = node
    if node is None:
        return
    postorder(currNode.left, lst)
    postorder(currNode.right, lst)
    lst.append(currNode.data[2])


def solution(nodeinfo):
    answer = [[], []]
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    tree = Tree()
    for node in nodeinfo:
        tree.__add__(node)
    preorder(tree.head, answer[0])
    postorder(tree.head, answer[1])

    return answer


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
