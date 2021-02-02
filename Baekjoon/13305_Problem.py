# 13305 주유소

N = int(input())
length = list(map(int, input().split()))
oil = list(map(int, input().split()))

cur = 0
nxt = 0
ans = 0
while cur < N-1:
    for i in range(cur+1, N):
        if i == N-1:
            nxt = i
            break
        if oil[cur] >= oil[i]:
            nxt = i
            break
    ans += (sum(length[cur:nxt]) * oil[cur])
    cur = nxt

print(ans)
