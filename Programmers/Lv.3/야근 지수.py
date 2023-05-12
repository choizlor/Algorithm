import heapq


def solution(n, works):
    if n >= sum(works):
        return 0

    works = [-w for w in works]
    heapq.heapify(works)

    for _ in range(n):
        a = heapq.heappop(works)
        a += 1
        heapq.heappush(works, a)

    return sum([w**2 for w in works])