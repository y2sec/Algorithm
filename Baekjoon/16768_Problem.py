# 16768 Mooyo Mooyo

# 위에 있는 블록들을 아래로 내리기 위한 메소드
def sort():
    swap = False
    for y in range(M):
        for x in range(N-1, -1, -1):
            if mymy[x][y] == '0':
                for nx in range(x, -1, -1):
                    if mymy[nx][y] != '0':
                        swap = True
                        mymy[x][y], mymy[nx][y] = mymy[nx][y], mymy[x][y]
                        break
    return swap


# 동일한 블록이 K개 이상이면 '0'으로 변환해주는 메소드
def crash(n):
    visited = [[0 for _ in range(M)] for __ in range(N)]
    need_visit = [(i, j)]
    count = 0
    # BFS를 이용해서 탐색
    while need_visit:
        x, y = need_visit.pop(0)
        if mymy[x][y] != n:
            continue

        if visited[x][y] == 0:
            visited[x][y] = 1
            count += 1
            for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if N > x + nx >= 0 and M > y + ny >= 0:
                    need_visit.append((x + nx, y + ny))
    # K개 이상이면 '0'으로 만들어줌
    if count >= K:
        for x in range(N):
            for y in range(M):
                if visited[x][y] == 1:
                    mymy[x][y] = '0'


N, K = map(int, input().split())
mymy = [list(input()) for _ in range(N)]
M = len(mymy[0])

# 아래부터 탐색하면서 지워줌
while True:
    for i in range(N-1, -1, -1):
        for j in range(len(mymy[i])):
            if mymy[i][j] != '0':
                crash(mymy[i][j])
    if not sort():
        break

for i in range(N):
    print(''.join(mymy[i]))
