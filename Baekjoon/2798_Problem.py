# 2798 블랙잭

N, M = map(int, input().split())
card = list(map(int, input().split()))

m = 0
# 완전 탐색을 통해 카드의 값을 비교한다
for i in range(len(card) - 2):
    for j in range(i + 1, len(card) - 1):
        if card[i] + card[j] > M:
            continue

        for k in range(j + 1, len(card)):
            if card[i] + card[j] + card[k] > M:
                continue

            if m < card[i] + card[j] + card[k]:
                m = card[i] + card[j] + card[k]
# M을 넘지 않으면서 M에 최대한 가까운 m 출력
print(m)
