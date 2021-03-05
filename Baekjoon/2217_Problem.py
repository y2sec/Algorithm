# 2217 로프

import sys

N = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline()) for _ in range(N)]

ropes.sort()

ans = 0
for i in range(N):
    ans = max(ans, ropes[i] * (N - i))

print(ans)
