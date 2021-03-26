# 2655 가장 높은 탑 쌓기

N = int(input())
bricks = list()
bricks.append((0, 0, 0, 0))
for _ in range(1, N + 1):
    a, h, w = map(int, input().split())
    bricks.append((_, a, h, w))
bricks = sorted(bricks, key=lambda x: x[3])
tower = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i):
        if bricks[i][1] > bricks[j][1]:
            tower[i] = max(bricks[i][2] + tower[j], tower[i])

max_tower = max(tower)
idx = N
result = []

while idx != 0:
    if max_tower == tower[idx]:
        max_tower -= bricks[idx][2]
        result.insert(0, bricks[idx][0])
    idx -= 1
print(len(result))
[print(x) for x in result]
