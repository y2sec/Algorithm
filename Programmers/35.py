# 피보나치 수

def solution(n):
    fibonacci = [0 for _ in range(100001)]
    fibonacci[1] = 1

    for i in range(2, n + 1):
        fibonacci[i] = (fibonacci[i - 1] + fibonacci[i - 2]) % 1234567

    return fibonacci[n]
