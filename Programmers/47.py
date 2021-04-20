# 프렌즈4블록

def solution(m, n, board):
    answer = 0

    blocks = [''.join([board[col][row] for col in range(m-1, -1, -1)]) for row in range(n)]
    while True:
        removeBlock = set()
        isRemove = False
        for row in range(m-1):
            for col in range(n-1):
                if blocks[col][row] == ' ':
                    continue
                fourBlock = set(list(blocks[col][row:row+2]) + list(blocks[col+1][row:row+2]))
                if len(fourBlock) != 1:
                    continue
                isRemove = True
                removeBlock.add((col, row))
                removeBlock.add((col+1, row))
                removeBlock.add((col, row+1))
                removeBlock.add((col+1, row+1))

        for x, y in removeBlock:
            blocks[x] = blocks[x][:y] + ' ' + blocks[x][y+1:]

        for col in range(n):
            cnt = blocks[col].count(' ')
            blocks[col] = blocks[col].replace(' ', '')
            blocks[col] += ' ' * cnt

        if not isRemove:
            break

    return sum([block.count(' ') for block in blocks])
