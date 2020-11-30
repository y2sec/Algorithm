# 2920 음계

def scale():
    # 입력을 받아 list로 만들어준다.
    scale_list = list(map(int, input().split()))
    # 1부터 시작하는 경우
    if scale_list[0] == 1:
        # 순서대로 늘어난다면 ascending. 아니면 mixed를 리턴
        for i in range(2, 9):
            if scale_list[i - 1] != i:
                return "mixed"
        return "ascending"
    # 8부터 시작하는 경우
    elif scale_list[0] == 8:
        # 역순으로 줄어든다면 descending. 아니면 mixed를 리턴
        for i in range(7, 0, -1):
            if scale_list[8 - i] != i:
                return "mixed"
        return "descending"
    # 둘다 아닌 경우는 mixed를 리턴
    else:
        return "mixed"


print(scale())
