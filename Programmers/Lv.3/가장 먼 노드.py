from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [-1] * (n+1)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue = deque([1])
    distance[1] = 0

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[now] + 1

    for d in distance:
        if d == max(distance):
            answer += 1

    return answer


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])