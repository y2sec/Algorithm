# 상호 평가

def solution(scores):
    answer = ''

    grades = {'A': 90, 'B': 80, 'C': 70, 'D': 50}

    studentN = len(scores)
    scores = [[scores[j][i] for j in range(studentN)] for i in range(studentN)]

    for i in range(studentN):
        score = scores[i][i]

        total = sum(scores[i])
        average = 0
        if scores[i].count(score) == 1 \
                and (score == max(scores[i]) or score == min(scores[i])):
            average = (total - score) / (studentN - 1)
        else:
            average = total / studentN

        answer += grade(average, grades)

    return answer


def grade(score, grades):
    for key in grades.keys():
        if score < grades[key]:
            continue
        return key
    return 'F'


print(solution(
    [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
print(solution([[50, 90], [50, 87]]))
print(solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]))
