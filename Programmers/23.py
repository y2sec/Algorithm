# 삼각 달팽이

def solution(n):
    answer = []

    pyramid = [[0] * x for x in range(1, n + 1)]

    cnt = sum([x for x in range(1, n + 1)])

    move = [[1, 0], [0, 1], [-1, -1]]
    m = 0

    x, y = 0, 0
    num = 1
    for i in range(n):
        for j in range(n - i):
            pyramid[x][y] = num
            num += 1

            if j == n-i-1:
                m = (m + 1) % 3
            x, y = x + move[m][0], y + move[m][1]

    for line in pyramid:
        for num in line:
            answer.append(num)

    return answer


solution(4)
