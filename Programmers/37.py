# 단속카메라

# 가장 먼저 빠져나가는 차의 끝부분에 카메라를 설치하지 않으면 절대로 그 차를 찍을 수 없음
# 그 다음 설치할 부분은 카메라에 찍히지 않은 차들 중 가장 먼저 빠져나가는 차의 끝부분임
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])

    prev_location = -30001

    for route in routes:
        if prev_location >= route[0]:
            continue
        else:
            answer += 1
            prev_location = route[1]

    return answer


solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]])
