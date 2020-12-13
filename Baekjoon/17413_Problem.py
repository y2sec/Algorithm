# 17413 단어 뒤집기2

# 문자열을 뒤집어서 list에 넣어주는 메소드
def reverse():
    for j in range(end-1, start-1, -1):
        result.append(S[j])


S = input()
result = list()
start, end = 0, 0
tag = False

# 문자의 위치를 기억해서 뒤집어줌
for i in range(len(S)):
    if tag and S[i] != '>':
        result.append(S[i])
        start, end = start+1, end+1
        continue
    # '<'가 들어오면 reverse 시켜주고 그 이후 문자를 뒤집지 않기 위해 tag로 저장해줌
    if S[i] == '<':
        reverse()
        result.append(S[i])
        start, end = end+1, end+1
        tag = True
    # '>'가 들어오면 태그가 끝났다는 뜻이기에 tag에 저장해줌
    elif S[i] == '>':
        result.append(S[i])
        start, end = start+1, end+1
        tag = False
    # 공백이 들어오면 tag가 아닐때 reverse해서 출력해줌
    elif S[i] == ' ':
        reverse()
        result.append(S[i])
        end, start = end+1, end+1
    else:
        end += 1
reverse()

print(''.join(result))
