# 17298 오큰수

N = int(input())
lst = list(map(int, input().split()))

stack = []
NGE = [-1 for _ in range(N)]

for i in range(len(lst)):
    while stack and stack[-1][1] < lst[i]:
        idx, value = stack.pop()
        NGE[idx] = lst[i]

    stack.append((i, lst[i]))

for value in NGE:
    print(value, end=' ')
