# 1236 성 지키기

n, m = map(int, input().split())

castle = list()
height_result = 0
width_result = 0

# 입력값을 리스트화 해주고 castle에 넣어줌
for _ in range(n):
    castle.append(list(input()))
# 한 행에 한명의 경비원이 존재해야하므로 층에 경비원이 없으면 +1 해줌
for height in range(n):
    if 'X' not in castle[height]:
        height_result += 1

# 한 열에 한명의 경비원이 존재해야하므로 층에 경비원이 없으면 +1 해줌
for width in range(m):
    have = False
    for height in range(n):
        if castle[height][width] == 'X':
            have = True
            break
    if not have:
        width_result += 1

# 비어있는 행과 열 중 더 큰 값을 출력
print(max(height_result, width_result))
