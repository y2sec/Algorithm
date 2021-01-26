# 1181 단어 정렬

N = int(input())
lst = [input() for _ in range(N)]
lst = list(set(lst))
lst.sort(key=lambda x: (len(x), x))
for s in lst:
    print(s)
