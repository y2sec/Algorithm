# 20949 효정과 새 모니터

import sys
import math

N = int(sys.stdin.readline())
monitor = []

for i in range(1, N+1):
    W, H = map(int, sys.stdin.readline().split())
    ppi = math.sqrt(W**2 + H**2) / 77
    monitor.append([ppi, i])

monitor.sort(key=lambda x : (-x[0], x[1]))

for m in monitor:
    print(m[1])
