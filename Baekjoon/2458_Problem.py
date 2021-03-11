# 2458 키 순서

def dfs(s, student):
    stack = [s]
    visited = [0 for _ in range(N + 1)]
    visited[s] = 1
    while stack:
        cur = stack.pop()
        for n in student[cur]:
            if not visited[n]:
                adj[n][0] += 1
                adj[s][1] += 1
                visited[n] = 1
                stack.append(n)


N, M = map(int, input().split())
student = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    student[a].append(b)

adj = [[0, 0] for _ in range(N + 1)]

for i in range(1, N + 1):
    dfs(i, student)

res = 0
for i in range(1, N + 1):
    if sum(adj[i]) == N - 1:
        res += 1

print(res)
