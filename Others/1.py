# 왕실의 나이트

cols = ['1', '2', '3', '4', '5', '6', '7', '8']
rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

location = input()

col, row = 0, 0

for i in range(8):
    if cols[i] == location[1]:
        col = i
    if rows[i] == location[0]:
        row = i

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

cnt = 0
for i in range(8):
    nx = col + dx[i]
    ny = row + dy[i]

    if 0 <= nx < 8 and 0 <= ny < 8:
        cnt += 1

print(cnt)
