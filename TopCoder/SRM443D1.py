# SRM443D1 BinaryFlip

def bfs():
    if A == 0:
        return 0
    if K > A + B:
        return -1
    state = [(x, K-x) for x in range(K+1)]
    visited = [False for _ in range(A+B+1)]
    need_visit = [(A, B, 0)]

    while need_visit:
        x, y, cnt = need_visit.pop(0)
        if y == A+B:
            return cnt

        if x < 0 or y < 0:
            continue

        for i in range(K+1):
            if x >= state[i][0] and y >= state[i][1] and not visited[y + (state[i][0] - state[i][1])]:
                visited[y + (state[i][0] - state[i][1])] = True
                need_visit.append((x + (state[i][1] - state[i][0]), y + (state[i][0] - state[i][1]), cnt+1))

    return -1


A, B, K = map(int, input().split())

print(bfs())
