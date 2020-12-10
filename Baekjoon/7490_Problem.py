# 7490 0 만들기

# 입력받은 수까지 만들 수 있는 모든 수식을 만듦
def make_zero(n, s):
    if n > N:
        exp_list.append(s)
        return
    if n == 1:
        make_zero(n+1, str(n))
        return
    make_zero(n+1, s+" "+str(n))
    make_zero(n+1, s+"+"+str(n))
    make_zero(n+1, s+"-"+str(n))


test_case = int(input())

for _ in range(test_case):
    result = list()
    N = int(input())
    exp_list = list()
    make_zero(1, "")
    # 생성된 수식을 계산하여 0이 되는 수식을 result에 삽입
    for exp in exp_list:
        if eval(exp.replace(" ", "")) == 0:
            result.append(exp)

    for r in result:
        print(r)
    print()
