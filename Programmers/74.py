# 가장 긴 팰린드롬
import sys
sys.setrecursionlimit(300000)


def solution(s):
    answer = 1

    for size in range(len(s), 1, -1):
        for start in range(len(s) - size + 1):
            if not isPalindrome(s[start:start+size]):
                continue

            return size

    return answer


def isPalindrome(s):
    return s[::-1] == s


print(solution('abcdcba'))
print(solution('abacde'))
