# 2609 최대공약수와 최소공배수

def gcd(a, b):
    n = a % b
    if n == 0:
        return b
    return gcd(b, n)


a, b = map(int, input().split())
print(gcd(a, b))
print(a * b // gcd(a, b))
