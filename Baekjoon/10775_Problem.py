# 10775 공항

import sys

G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
gate = [0 for _ in range(G+1)]

airplane_num = 0
isDocking = True
for _ in range(P):
    if not isDocking:
        break

    airplane = int(sys.stdin.readline())

    while airplane > 0 and gate[airplane] > 0:
        t = gate[airplane]
        gate[airplane] += 1
        airplane -= t
    if airplane <= 0:
        isDocking = False
    else:
        gate[airplane] = 1
        airplane_num += 1


print(airplane_num)
