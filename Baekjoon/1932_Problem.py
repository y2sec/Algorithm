# 1932 정수 삼각형

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(tri[i])):
        # 첫 번째 위치에 있을 때 
        if j == 0:
            tri[i][j] += tri[i-1][j]
        # 마지막 위치에 있을 때
        elif j == len(tri[i])-1:
            tri[i][j] += tri[i-1][j-1]
        # 그 이외의 경우는  두 수중 더 큰 수를 더해줌
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[n-1]))
