# 9205 맥주 마시면서 걸어가기

import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    locations = []
    dist = [[False for _ in range(n + 2)] for _ in range(n + 2)]

    for i in range(n + 2):
        x, y = map(int, sys.stdin.readline().split())
        locations.append([x, y])

    for i in range(n + 2):
        for j in range(n + 2):
            diff = abs(locations[i][0] - locations[j][0]) + abs(locations[i][1] - locations[j][1])
            if diff <= 1000:
                dist[i][j] = True

    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                if dist[i][k] and dist[k][j]:
                    dist[i][j] = True

    if dist[0][-1]:
        print('happy')
    else:
        print('sad')
