# 여행경로
import collections


def solution(tickets):
    answer = ['ICN']

    airplain = collections.defaultdict(dict)
    for start, end in tickets:
        if end in airplain[start]:
            airplain[start][end] += 1
        else:
            airplain[start][end] = 1

    def dfs(curr, useTicket):
        if useTicket == len(tickets):
            return

        for nxt in sorted(airplain[curr].keys()):
            if airplain[curr][nxt] == 0:
                continue

            airplain[curr][nxt] -= 1
            answer.append(nxt)

            dfs(nxt, useTicket + 1)

            if len(answer) == len(tickets) + 1:
                return

            airplain[curr][nxt] += 1
            answer.pop()

    dfs('ICN', 0)

    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
