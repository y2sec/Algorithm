# 11004 K번째 수

# n과 k를 입력받고 리스트 A를 입력받음
n, k = map(int, input().split())
A = list(map(int, input().split()))

# 정렬하여 k번째 수를 출력
A = sorted(A)

print(A[k-1])
