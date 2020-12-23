# 17269 이름궁합 테스트

# dict를 통해 미리 해당 값을 넣어줌
alpha = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3, 'I': 1,
         'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2,
         'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}

N, M = map(int, input().split())
A, B = input().split()
result = []

idx = 0
# 이름 궁합의 순서를 진행
while idx < N and idx < M:
    result.append(A[idx])
    result.append(B[idx])
    idx += 1
while idx < N:
    result.append(A[idx])
    idx += 1
while idx < M:
    result.append(B[idx])
    idx += 1

for idx in range(len(result)):
    result[idx] = alpha[result[idx]]

while len(result) != 2:
    for idx in range(len(result) - 1):
        result[idx] = (result[idx] + result[idx + 1]) % 10
    result.pop()

# 결과 출력
if result[0] == 0:
    print(str(result[1]) + '%')
else:
    print(str(result[0]) + str(result[1]) + '%')
