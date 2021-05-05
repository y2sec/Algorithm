# 호텔 방 배정

import sys
sys.setrecursionlimit(10 ** 7)


def solution(k, room_number):
    answer = []

    room = dict()

    def find(number):
        if number not in room:
            room[number] = number + 1
            return room[number]

        room[number] = find(room[number])
        return room[number]

    for number in room_number:
        answer.append(find(number) - 1)

    return answer
