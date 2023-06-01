def solution(tickets):
    V = [0 for _ in range(len(tickets) + 1)]
    answer = []

    def dfs(depth, ticket, mid):
        if depth == len(tickets):
            answer.append(mid)
            return

        for i in range(len(tickets)):
            if ticket == tickets[i][0] and not V[i]:
                V[i] = 1
                dfs(depth + 1, tickets[i][1], mid + [tickets[i][1]])
                V[i] = 0

    dfs(0, "ICN", ["ICN"])

    answer.sort()
    return answer[0]


solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], ["IAD", "JIU"]])
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
