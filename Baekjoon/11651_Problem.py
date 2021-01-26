# 11651 좌표 정렬하기 2

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x : (x[1], x[0]))

for x, y in lst:
    print(x, y)
