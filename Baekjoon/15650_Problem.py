# 15650 N과 M (2)

def sequence(num, cnt):
    lst.append(num)
    if cnt == M:
        for i in lst:
            print(i, end=' ')
        print()
        lst.pop()
        return

    for i in range(num+1, N+1):
        if i not in lst:
            sequence(i, cnt+1)
    lst.pop()


N, M = map(int, input().split())
lst = []

for n in range(1, N+1):
    sequence(n, 1)
