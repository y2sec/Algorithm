# N개의 최소공배수

def solution(arr):
    def gcd(n1, n2):
        return n2 if n1 % n2 == 0 else gcd(n2, n1 % n2)

    for idx in range(1, len(arr)):
        arr[idx] = arr[idx - 1] * arr[idx] // gcd(arr[idx - 1], arr[idx])

    return arr[-1]
