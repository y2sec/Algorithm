# 1495 기타리스트

N, S, M = map(int, input().split())
V = list(map(int, input().split()))
P = [S]
idx = 0
result = 0
able = True
for v in V:
    p_list = set()
    for p in P:
        if p + v <= M:
            p_list.add(p+v)
        if p - v >= 0:
            p_list.add(p-v)
    if not p_list:
        able = False
        break
    P = p_list
    idx += 1
if able:
    print(max(P))
else:
    print(-1)