# 18406 럭키 스트레이트

N = input()

left = list(map(int, N[:len(N)//2]))
right = list(map(int, N[len(N)//2:]))

if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')
