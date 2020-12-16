# 14620 꽃길

# 현재 위치의 대여료
def searchValue(x, y):
    value = 0
    for nx, ny in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
        value += G[x + nx][y + ny]
    return value


# 세 개의 위치에 꽃을 심을수 있는지 체크
def chk(a, b, c):
    g = set()
    n = N - 2
    xa, xb, xc = a // n, b // n, c // n
    ya, yb, yc = a % n, b % n, c % n
    for nx, ny in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
        g.add((xa+nx, ya+ny))
        g.add((xb+nx, yb+ny))
        g.add((xc+nx, yc+ny))

    if len(g) == 15:
        return True
    return False


N = int(input())
G = [[int(x) for x in input().split()] for _ in range(N)]
result = float('inf')

values = []

for cx in range(1, N - 1):
    for cy in range(1, N - 1):
        values.append(searchValue(cx, cy))

# 최소 값을 계속 갱신해줌
for i in range(len(values) - 2):
    for j in range(i + 1, len(values) - 1):
        for k in range(j + 1, len(values)):
            if chk(i, j, k):
                result = min(result, values[i] + values[j] + values[k])
print(result)
