# 14889 스타트와 링크

import itertools


def linkT(team):
    link = []
    for i in range(N):
        if i not in team:
            link.append(i)
    return link


def ability(team):
    ab = 0
    combination = itertools.permutations(team, 2)
    for i, j in combination:
        ab += abilitys[i][j]

    return ab


def startT(team, prev):
    global ans
    if len(team) == N / 2:
        start = ability(team)
        link = ability(linkT(team))
        ans = min(ans, abs(start - link))
        return

    for i in range(prev+1, N):
        if i not in team:
            team.append(i)
            startT(team, i)
            team.pop()


ans = float('inf')
N = int(input())
abilitys = [list(map(int, input().split())) for _ in range(N)]
startT([], -1)
print(ans)
