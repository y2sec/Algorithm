# 5397 키로거

test_case = int(input())
result = list()

# 테스트 케이스만큼 실행
for i in range(test_case):
    # 리스트 두 개를 구현하여 command가 들어올 때마다 이동
    left = list()
    right = list()
    for command in input():
        # '<'가 들어오면 right 리스트에 left 리스트를 pop해서 넣어줌
        if command == '<':
            if left:
                right.append(left.pop())
        # '>'가 들어오면 left 리스트에 right 리스트를 pop해서 넣어줌
        elif command == '>':
            if right:
                left.append(right.pop())
        # '-'가 들어오면 left 리스트를 pop 해줌
        elif command == '-':
            if left:
                left.pop()
        # 그 이외의 문자가 들어오면 left 리스트에 넣어줌
        else:
            left.append(command)
    # left와 right를 합쳐줌        
    left.extend(reversed(right))
    print(''.join(left))
