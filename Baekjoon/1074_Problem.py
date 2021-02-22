# 1074 Z

def z(n, x, y):
    global result

    if x > r or x + n < r:
        result += n ** 2
        return
    elif y > c or y + n < c:
        result += n ** 2
        return

    if n == 2:
        if (r, c) == (x, y):
            print(result)
            exit()
        result += 1
        if (r, c) == (x, y + 1):
            print(result)
            exit()
        result += 1
        if (r, c) == (x + 1, y):
            print(result)
            exit()
        result += 1
        if (r, c) == (x + 1, y + 1):
            print(result)
            exit()
        result += 1
        return
    z(n // 2, x, y)
    z(n // 2, x, y + n // 2)
    z(n // 2, x + n // 2, y)
    z(n // 2, x + n // 2, y + n // 2)


N, r, c = map(int, input().split())
result = 0
z(2**N, 0, 0)
