# SRM452D2 Hamilton Path

def dfs(road, visit):
    visit[road] = True
    for i in range(N):
        if roads[road][i] == 'Y' and not visit[i]:
            dfs(i, visit)


def countPaths():
    count = []
    visit = [False for _ in range(N)]

    free = 0
    group = 0

    ans = 1

    for road in roads:
        count.append(road.count('Y'))
        if count[-1] > 2:
            return 0

    for i in range(N):
        if count[i] == 0:
            visit[i] = True
            free += 1
        elif count[i] == 1 and not visit[i]:
            dfs(i, visit)

    for v in visit:
        if not v:
            return 0

    for i in range(2, group+free):
        ans *= i

    ans *= (2 * group)

    return ans % 1000000007


N = 3
roads = [input() for _ in range(N)]



