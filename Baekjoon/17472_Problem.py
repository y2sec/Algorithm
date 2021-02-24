# 17472 다리 만들기 2

import heapq


def island(x, y, n):
    queue = [[x, y]]

    while queue:
        cx, cy = queue.pop(0)
        if 0 > cx or N <= cx or 0 > cy or M <= cy:
            continue
        if not visited[cx][cy] and m[cx][cy] == 1:
            visited[cx][cy] = True
            m[cx][cy] = n
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                queue.append([cx + dx, cy + dy])


def bridge(x, y):
    for dx in range(x+1, N):
        if m[x][y] == m[dx][y]:
            break
        if m[dx][y] != 0 and m[x][y] != m[dx][y]:
            weight = abs(x - dx) - 1
            if weight >= 2:
                heapq.heappush(queue, [weight, m[x][y], m[dx][y]])
            break

    for dx in range(x-1, -1, -1):
        if m[x][y] == m[dx][y]:
            break
        if m[dx][y] != 0 and m[x][y] != m[dx][y]:
            weight = abs(x - dx) - 1
            if weight >= 2:
                heapq.heappush(queue, [weight, m[x][y], m[dx][y]])
            break

    for dy in range(y+1, M):
        if m[x][y] == m[x][dy]:
            break
        if m[x][dy] != 0 and m[x][y] != m[x][dy]:
            weight = abs(y - dy) - 1
            if weight >= 2:
                heapq.heappush(queue, [weight, m[x][y], m[x][dy]])
            break

    for dy in range(y-1, -1, -1):
        if m[x][y] == m[x][dy]:
            break
        if m[x][dy] != 0 and m[x][y] != m[x][dy]:
            weight = abs(y - dy) - 1
            if weight >= 2:
                heapq.heappush(queue, [weight, m[x][y], m[x][dy]])
            break



def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    A = find(a)
    B = find(b)

    if A == B:
        return False
    parent[A] = B
    return True


def mst(q):
    weight = 0
    while q:
        w, a, b = heapq.heappop(q)
        if union(a, b):
            weight += w

    return weight


N, M = map(int, input().split())

m = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

cnt = 1
for i in range(N):
    for j in range(M):
        if not visited[i][j] and m[i][j] == 1:
            island(i, j, cnt)
            cnt += 1

queue = []
for i in range(N):
    for j in range(M):
        if m[i][j] != 0:
            bridge(i, j)

parent = [x for x in range(cnt)]

weight = mst(queue)

isConnect = True
for i in range(1, cnt):
    if find(i) != find(1):
        isConnect = False
        break
print(weight if isConnect else -1)
