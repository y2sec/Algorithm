# 14888 연산자 끼워넣기
# +, -, *, /

def calculator(exp, idx):
    exp.append(A[idx])
    if idx == N-1:
        res = ''
        for x in range(len(exp)):
            res += exp[x]
            if x % 2 == 0:
                res = str(int(eval(res)))
        ans.append(int(res))
        exp.pop()
        return
    for i in range(4):
        if operN[i] > 0:
            operN[i] -= 1
            exp.append(oper[i])
            calculator(exp, idx+1)
            exp.pop()
            operN[i] += 1
    exp.pop()


N = int(input())
A = list(input().split())
operN = list(map(int, input().split()))
oper = ['+', '-', '*', '/']
ans = []
calculator([], 0)
print(max(ans))
print(min(ans))
