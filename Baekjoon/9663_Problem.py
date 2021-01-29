# 9663 N-Queen

def isAvailable(line):
    for i in range(line):
        if board[i] == board[line]:
            return False
        if abs(line - i) == abs(board[line]-board[i]):
            return False
    return True


def NQueue(line):
    global ans
    if line == N:
        ans += 1
        return

    for i in range(N):
        board[line] = i
        if isAvailable(line):
            NQueue(line+1)


N = int(input())
board = [0 for _ in range(N)]
ans = 0
NQueue(0)
print(ans)
