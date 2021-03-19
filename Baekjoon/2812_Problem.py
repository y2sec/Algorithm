# 2812 크게 만들기

N, K = map(int, input().split())
num = input()
stack = [num[0]]

for idx in range(1, N):
    while len(stack) > 0 and stack[-1] < num[idx] and K > 0:
        K -= 1
        stack.pop()
    stack.append(num[idx])

if K != 0:
    stack = stack[:-K]

print(''.join(stack))
