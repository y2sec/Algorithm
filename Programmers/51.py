# 파일명 정렬

def solution(files):
    answer = []

    for file in files:
        file_info = []

        numStart = 0
        for idx in range(len(file)):
            if file[idx].isdigit():
                file_info.append(file[:idx])
                numStart = idx
                break

        numEnd = numStart
        for idx in range(numStart, len(file)):
            if not file[idx].isdigit():
                break
            numEnd = idx + 1

        file_info.append(file[numStart:numEnd])
        file_info.append(file[numEnd:])

        answer.append(file_info)

    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))

    for idx in range(len(answer)):
        answer[idx] = ''.join(answer[idx])

    return answer
