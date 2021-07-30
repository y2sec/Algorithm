# 모두 0으로 만들기
import collections
import sys


sys.setrecursionlimit(300000)
answer = 0


def solution(a, edges):
    global answer
    if sum(a) != 0:
        return -1

    graph = collections.defaultdict(list)

    for A, B in edges:
        graph[A].append(B)
        graph[B].append(A)

    visited = [False for _ in range(len(a))]

    def dfs(curr):
        global answer

        if visited[curr]:
            return 0

        visited[curr] = True

        for nxt in graph[curr]:
            if visited[nxt]:
                continue
            value = dfs(nxt)
            answer += abs(value)
            a[curr] += value

        return a[curr]

    for s in range(len(a)):
        if visited[s]:
            continue

        dfs(s)

    return answer


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
print(solution([0, 1, 0], [[0, 1], [1, 2]]))
