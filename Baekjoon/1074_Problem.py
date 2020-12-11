# 1074 Z

def z(N, x, y):
    global result
    if N == 2:
        if (r, c) == (x, y):
            print(result)
            return
        result += 1
        if (r, c) == (x, y + 1):
            print(result)
            return
        result += 1
        if (r, c) == (x + 1, y):
            print(result)
            return
        result += 1
        if (r, c) == (x + 1, y + 1):
            print(result)
            return
        result += 1
        return
    z(N / 2, x, y)
    z(N / 2, x, y + N / 2)
    z(N / 2, x + N / 2, y)
    z(N / 2, x + N / 2, y + N / 2)


result = 0
N, r, c = map(int, input().split())
z(2 ** N, 0, 0)
