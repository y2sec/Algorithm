# 1976 여행 가자

def find(a):
    if parent[a] == a:
        return a

    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    A = find(a)
    B = find(b)

    parent[B] = A


N = int(input())
M = int(input())
parent = [x for x in range(N)]

for i in range(N):
    j = list(map(int, input().split()))
    for x in range(len(j)):
        if j[x]:
            union(i, x)

route = list(map(int, input().split()))

isAvailable = True

for i in range(M-1):
    if find(route[i]-1) != find(route[i+1]-1):
        isAvailable = False
        break

print('YES' if isAvailable else 'NO')
