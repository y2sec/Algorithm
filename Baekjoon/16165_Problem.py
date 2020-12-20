# 16165 걸그룹 마스터 준석이


N, M = map(int, input().split())
# 입력받은 걸그룹을 dict에 저장
girlgroups = dict()
for _ in range(N):
    groupname = input()
    girlgroups[groupname] = list()
    for __ in range(int(input())):
        girlgroups[groupname].append(input())
# 그 후 입력 받는 옵션에 따라 다른 출력을 보여줌
for _ in range(M):
    name = input()
    num = int(input())
    if num == 1:
        for key, values in girlgroups.items():
            if name in values:
                print(key)
                break
    else:
        for value in sorted(girlgroups[name]):
            print(value)
