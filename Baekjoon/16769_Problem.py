# 16769 Mixing Milk

milks = list()

# 입력받은 우유를 리스트로 삽입
for _ in range(3):
    milks.append(list(map(int, input().split())))

# 100번을 반복
for i in range(100):
    # 현재 위치는 cur 다음 위치는 nxt
    cur = i % 3
    nxt = (i + 1) % 3
    # 우유를 섞어줌
    milks[nxt][1] += milks[cur][1]
    milks[cur][1] = 0
    # 넘치는 우유 양을 되돌림
    if milks[nxt][0] < milks[nxt][1]:
        diff = milks[nxt][1] - milks[nxt][0]
        milks[cur][1] += diff
        milks[nxt][1] -= diff

for milk in milks:
    print(milk[1])
