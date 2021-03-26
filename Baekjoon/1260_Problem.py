# 1260 DFS와 BFS

def DFS(graph, start):
    visited = list()
    need_visit = list()
    need_visit.append(start)
    while need_visit:
        node = need_visit.pop()
        if not node in visited:
            visited.append(node)
            if node in graph:
                need_visit.extend(graph[node])
    return visited


def BFS(graph, start):
    visited = list()
    need_visit = list()
    need_visit.append(start)
    while need_visit:
        node = need_visit.pop(0)
        if not node in visited:
            visited.append(node)
            if node in graph:
                need_visit.extend(graph[node])
    return visited


N, M, V = map(int, input().split())

graph = dict()

for _ in range(M):
    parent, child = map(int, input().split())
    if parent in graph:
        graph[parent].append(child)
    else:
        graph[parent] = list()
        graph[parent].append(child)

    if child in graph:
        graph[child].append(parent)
    else:
        graph[child] = list()
        graph[child].append(parent)

for key in graph.keys():
    graph[key].sort()
bfs = BFS(graph, V)
for key in graph.keys():
    graph[key].sort(reverse=True)
dfs = DFS(graph, V)

for node in dfs:
    print(node, end=' ')
print()

for node in bfs:
    print(node, end=' ')
