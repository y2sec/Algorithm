# 1543 문서 검색

doc = input()
word = input()
result = 0

l = len(word)
idx = 0
while idx + l <= len(doc):
    # 한 칸씩 이동하면서 입력받은 문자열을 비교함
    if word == doc[idx:idx + l]:
        result += 1
        idx += l
    else:
        idx += 1

print(result)
