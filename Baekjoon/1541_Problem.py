# 1541 잃어버린 괄호

data = input()
exp = []
start = 0
end = 0
for s in data:
    if s == '+' or s == '-':
        exp.append(data[start:end])
        exp.append(s)
        end += 1
        start = end
    else:
        end += 1
exp.append(data[start:end])

i = 0
while i < len(exp):
    if exp[i] == '+':
        y = int(exp.pop(i+1))
        oper = exp.pop(i)
        x = int(exp.pop(i-1))
        exp.insert(i-1, str(x+y))
    else:
        i += 1

ans = int(exp[0])
for i in range(1, len(exp)):
    if exp[i] != '-':
        ans -= int(exp[i])

print(ans)
