# 1939 중량제한

# BFS로 연결이 가능한지 탐색
def bfs(weight, bridges, start_node, end_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop(0)
        if node == end_node:
            return True
        if node not in visited:
            visited.append(node)
            for key, value in bridges[node].items():
                if value >= weight:
                    need_visit.append(key)
    return False


n, m = map(int, input().split())
bridges = dict()
min_weight = 1000000000
max_weight = 1

for _ in range(m):
    s, e, w = map(int, input().split())
    if s not in bridges:
        bridges[s] = dict()
        bridges[s][e] = w
    else:
        if e in bridges[s]:
            bridges[s][e] = max(bridges[s][e], w)
        else:
            bridges[s][e] = w

    if e not in bridges:
        bridges[e] = dict()
        bridges[e][s] = w
    else:
        if s in bridges[e]:
            bridges[e][s] = max(bridges[e][s], w)
        else:
            bridges[e][s] = w

    min_weight = min(min_weight, w)
    max_weight = max(max_weight, w)

# 이진 탐색을 통해 건널 수 있는 최대 값을 구함
start, end = map(int, input().split())
result = min_weight
while min_weight <= max_weight:
    mid = (max_weight + min_weight) // 2

    if bfs(mid, bridges, start, end):
        min_weight = mid + 1
        result = mid
    else:
        max_weight = mid - 1

print(result)
