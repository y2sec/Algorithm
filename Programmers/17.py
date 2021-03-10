# 순위 검색

def solution(info, query):
    answer = []

    table = dict()
    for i in info:
        i = i.split()
        people = i[0] + i[1] + i[2] + i[3]
        for j in range(16):
            s = ''
            if j >= 8:
                j -= 8
                s = '-' + s
            else:
                s = i[3] + s

            if j >= 4:
                j -= 4
                s = '-' + s
            else:
                s = i[2] + s

            if j >= 2:
                j -= 2
                s = '-' + s
            else:
                s = i[1] + s

            if j >= 1:
                j -= 1
                s = '-' + s
            else:
                s = i[0] + s

            if s in table:
                table[s].append(int(i[4]))
            else:
                table[s] = [int(i[4])]

    for key in table.keys():
        table[key].sort(reverse=True)

    for q in query:
        q = q.split()
        key = q[0] + q[2] + q[4] + q[6]
        score = int(q[7])

        if key not in table:
            answer.append(0)
            continue

        min_res = 0
        max_res = len(table[key])
        mid_res = (min_res + max_res) // 2

        res = 0
        while min_res <= max_res:
            if len(table[key]) <= mid_res:
                break

            if table[key][mid_res] >= score:
                res = max(res, mid_res + 1)
                min_res = mid_res + 1
            else:
                max_res = mid_res - 1
            mid_res = (min_res + max_res) // 2

        answer.append(res)

    return answer
