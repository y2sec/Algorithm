# 1874 스택 수열

# 입력하는 수 개수와 스택, 결과를 저장할 리스트와 입력 값을 저장할 리스트 생성
n = int(input())
stack = list()
output = list()
data = list()

# 수열을 만들수 있는지 체크
sequence = True

for i in range(n):
    data.append(int(input()))

idx = 0
for i in range(1, n+1):
    # 스택은 LIFO이기 때문에 리스트 마지막에 저장된 값을 확인하면서 결과를 저장
    for j in range(len(stack)):
        if stack[-1] == data[idx]:
            idx += 1
            stack.pop()
            output.append('-')
        else:
            break
    stack.append(i)
    output.append('+')

# 남아있는 데이터들을 pop하면서 입력한 수열과 맞는지 확인
for i in range(len(stack)):
    if stack[-1] == data[idx]:
        idx += 1
        stack.pop()
        output.append('-')
    else:
        sequence = False

# 출력
if sequence:
    for s in output:
        print(s)
else:
    print("NO")
