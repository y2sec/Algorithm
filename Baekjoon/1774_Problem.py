# 1774 우주신과의 교감

import math


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    else:
        parent[x] = y
    return True


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
graph = []
arr = [0]
result = 0
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

for i in range(1, n):
    for j in range(i + 1, n + 1):
        weight = math.sqrt(pow((arr[i][0] - arr[j][0]), 2) + pow((arr[i][1] - arr[j][1]), 2))
        graph.append((i, j, weight))
graph = sorted(graph, key=lambda x: x[2])

for x, y, weight in graph:
    if union(x, y):
        result += weight
print('%.2f' % result)
