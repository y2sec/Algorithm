# 1934 최소공배수

def gcd(a, b):
    n = a % b
    if n == 0:
        return b
    return gcd(b, n)


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))
