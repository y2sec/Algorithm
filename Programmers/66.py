# 순위

def solution(n, results):
    answer = 0

    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for A, B in results:
        graph[A][B] = 1
        graph[B][A] = -1

    for p in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][p] == -1 and graph[p][j] == -1:
                    graph[i][j] = -1
                elif graph[i][p] == 1 and graph[p][j] == 1:
                    graph[i][j] = 1

    for A in range(1, n + 1):
        notKnow = 0
        for B in range(1, n + 1):
            if graph[A][B] == 0:
                notKnow += 1

        if notKnow == 1:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5, 6], [6, 7]]), 4)
print(solution(6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]), 6)
print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)
print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]), 1)
print(solution(3, [[1, 2], [1, 3]]), 1)
print(solution(6, [[1, 6], [2, 6], [3, 6], [4, 6]]), 0)
print(solution(8, [[1, 2], [3, 4], [5, 6], [7, 8]]), 0)
print(solution(9, [[1, 2], [1, 3], [1, 4], [1, 5], [6, 1], [7, 1], [8, 1], [9, 1]]), 1)
print(solution(6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [2, 4], [2, 6]]), 6)
print(solution(4, [[4, 3], [4, 2], [3, 2], [3, 1], [4, 1], [2, 1]]), 4)
print(solution(3, [[3, 2], [3, 1]]), 1)
print(solution(4, [[1, 2], [1, 3], [3, 4]]), 1)
