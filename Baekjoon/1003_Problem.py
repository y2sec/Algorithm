# 1003 피보나치 함수

T = int(input())

fibo = [[0, 0] for _ in range(40)]
fibo[0][0] = 1
fibo[1][1] = 1

for i in range(2, 40):
    fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
    fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]

for _ in range(T):
    N = int(input())
    print(fibo[N][0], fibo[N][1])
