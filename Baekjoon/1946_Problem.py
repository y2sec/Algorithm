# 1946 신입 사원

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    scores = [list(map(int, sys.stdin.readline().split())) + [i] for i in range(N)]
    rank = [sorted(scores, key=lambda x: x[0]), sorted(scores, key=lambda x: x[1])]
    res = set()
    for i in range(2):
        p = (i + 1) % 2
        min_rank = rank[i][0][p]
        res.add(rank[i][0][2])
        for j in range(1, N):
            if min_rank > rank[i][j][p]:
                res.add(rank[i][j][2])
                min_rank = rank[i][j][p]

    print(len(res))
