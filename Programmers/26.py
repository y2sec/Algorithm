# 폰켓몬

def solution(nums):
    return min(len(nums) // 2, len(set(nums)))


print(solution([3, 1, 2, 3]))
