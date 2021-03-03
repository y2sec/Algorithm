# 1339 단어 수학

N = int(input())
datas = [input() for _ in range(N)]
alphabet_cnt = [dict() for _ in range(9)]
alphabet_score = dict()
for data in datas:
    for i in range(1, len(data)+1):
        if data[-i] not in alphabet_score:
            alphabet_score[data[-i]] = 0
        if data[-i] in alphabet_cnt[i]:
            alphabet_cnt[i][data[-i]] += 1
        else:
            alphabet_cnt[i][data[-i]] = 1

for i in range(1, 9):
    score = 10**i
    for alphabet, cnt in alphabet_cnt[i].items():
        alphabet_score[alphabet] += (score * cnt)

scores = sorted(alphabet_score.items(), key=lambda x: x[1], reverse=True)

alphabet_num = dict()
num = 9
while scores:
    alphabet, score = scores.pop(0)
    alphabet_num[alphabet] = num
    num -= 1

res = 0
for data in datas:
    str_num = ''
    for s in data:
        str_num += str(alphabet_num[s])
    res += int(str_num)

print(res)
