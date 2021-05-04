# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    stack = []

    def crain(location):
        for depth in range(len(board)):
            if board[depth][location]:
                doll = board[depth][location]
                board[depth][location] = 0
                return doll
        return 0

    for move in moves:
        doll = crain(move - 1)
        if doll == 0:
            continue

        if stack and stack[-1] == doll:
            stack.pop()
            answer += 2
        else:
            stack.append(doll)

    return answer