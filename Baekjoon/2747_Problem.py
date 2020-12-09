# 2747 피보나치 수

def fibonacci(n):
    global result
    if n < 2:
        return n
    elif result[n] is not None:
        return result[n]
    else:
        result[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return result[n]


N = int(input())

result = [None for _ in range(46)]
print(fibonacci(N))
