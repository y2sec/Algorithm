# 10844 쉬운 계단 수

N = int(input())

stairsN = [[1 for _ in range(10)] for _ in range(N+1)]
stairsN[1][0] = 0

for i in range(2, N+1):
    stairsN[i][0] = stairsN[i-1][1]
    for j in range(1, 9):
        stairsN[i][j] = (stairsN[i-1][j-1] + stairsN[i-1][j+1]) % 1000000000
    stairsN[i][9] = stairsN[i-1][8] % 1000000000

print(sum(stairsN[N]) % 1000000000)
