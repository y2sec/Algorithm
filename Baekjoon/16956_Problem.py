# 16956 늑대와 양

R, C = map(int, input().split())

pasture = [[s for s in input()] for _ in range(R)]

# 전부 탐색해 주면서 늑대 주변 상하좌우에 양이 있는지 확인
chk = False
for x in range(R):
    for y in range(C):
        if pasture[x][y] == 'W':
            for nx, ny in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if x+nx < 0 or x+nx >= R or y+ny < 0 or y+ny >= C:
                    continue
                if pasture[x+nx][y+ny] == 'S':
                    chk = True
                    
# 주변에 양이 있다면 0을 아니면 1을 출력해주고 나머지를 모두 울타리로 채움
if chk:
    print(0)
else:
    print(1)
    for x in range(R):
        for y in range(C):
            if pasture[x][y] not in 'SW':
                pasture[x][y] = 'D'
    for line in pasture:
        print(''.join(line))
