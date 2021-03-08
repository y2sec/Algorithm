# 문자열 압축

def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        start = 0
        cnt = 1
        change = ''
        while start < len(s):
            if s[start:start + i] == s[start + i:start + i + i]:
                cnt += 1
            elif cnt >= 2:
                change += str(cnt) + s[start:start + i]
                cnt = 1
            else:
                change += s[start:start + i]
            start += i

        answer = min(answer, len(change))

    return answer


print(solution('a'))
