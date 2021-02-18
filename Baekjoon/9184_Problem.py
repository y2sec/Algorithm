# 9184 신나는 함수 실행

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c] != float('inf'):
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[a][b][c]


A, B, C = map(int, input().split())
dp = [[[float('inf') for _ in range(21)] for _ in range(21)] for _ in range(21)]
while A != -1 or B != -1 or C != -1:
    print('w(' + str(A) + ', ' + str(B) + ', ' + str(C) + ') = ', end='')
    print(w(A, B, C))

    A, B, C = map(int, input().split())
