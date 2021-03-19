# 2847 게임을 만든 동준이

N = int(input())
stage = [int(input()) for _ in range(N)]
down = 0
for level in range(N-2, -1, -1):
    if stage[level] >= stage[level+1]:
        level_down = stage[level] - stage[level+1] + 1
        stage[level] -= level_down
        down += level_down

print(down)
