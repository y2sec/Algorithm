# SRM425D2 CrazyBot

def solution(x, y, cnt):
    global ans
    if cnt == n:
        return 1
    ans = 0
    for i in range(4):
        if m[x + move[i][0]][y + move[i][1]]:
            m[x + move[i][0]][y + move[i][1]] = False
            ans += solution(x + move[i][0], y + move[i][1], cnt + 1) * prob[i]
            m[x + move[i][0]][y + move[i][1]] = True
    return ans


n = int(input())
E, W, S, N = map(int, input().split())

prob = [E/100, W/100, S/100, N/100]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

m = [[True for _ in range(n * 2 + 1)] for __ in range(n * 2 + 1)]
m[n][n] = False

ans = 0

solution(n, n, 0)

print(ans)

