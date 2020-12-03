# 1966 프린터 큐

# 테스트 케이스와 결과를 저장할 리스트
case = int(input())
result = list()

# 테스트 케이스만큼 실행
for i in range(case):
    # 문서 수 n과 위치 m 입력
    n, m = map(int, input().split(' '))
    queue = list(map(int, input().split(' ')))
    out = 0
    # 중요도가 가장 높은 문서가 맨 앞에 있을 경우에만 pop 시켜줌
    while queue:
        if max(queue) == queue[0]:
            queue.pop(0)
            out += 1
            if m == 0:
                break
            m -= 1
        else:
            queue.append(queue.pop(0))
            if m == 0:
                m = len(queue) - 1
            else:
                m -= 1
    # 결과를 result에 넣어줌
    result.append(out)

for i in result:
    print(i)
