# 네트워크

def find(a, parent):
    if a == parent[a]:
        return a

    parent[a] = find(parent[a], parent)
    return parent[a]


def union(a, b, parent):
    A = find(a, parent)
    B = find(b, parent)

    if A == B:
        return False

    parent[A] = B
    return True


def solution(n, computers):
    answer = n

    parent = [x for x in range(n)]

    for a in range(n):
        for b in range(n):
            if a == b:
                continue

            if not computers[a][b]:
                continue

            if union(a, b, parent):
                answer -= 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))