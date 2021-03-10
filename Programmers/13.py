# 가장 큰 정사각형 찾기

def solution(board):
    answer = 0

    row = len(board)
    col = len(board[0])

    dp = [[0] * (col + 1) for _ in range(row + 1)]

    for i in range(row):
        for j in range(col):
            if board[i][j]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    answer = max([max(lst) for lst in dp])

    return answer * answer
