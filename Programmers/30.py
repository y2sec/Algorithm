# 방문 길이

def solution(dirs):
    move_road = []
    move = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}
    x, y = 0, 0
    for s in dirs:
        dx, dy = move[s]
        nx, ny = x + dx, y + dy
        if nx > 5 or ny > 5 or nx < -5 or ny < -5:
            continue
        move_road.append([(x, y), (nx, ny)])
        x, y = nx, ny

    for i in range(len(move_road)):
        move_road[i].sort()

    move_road.sort()
    answer = len(move_road)
    for i in range(len(move_road) - 1):
        if move_road[i] == move_road[i + 1]:
            answer -= 1

    print(move_road)

    return answer