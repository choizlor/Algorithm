import heapq


def solution(n, k, enemy):
    heap = []
    total = 0
    answer = 0

    for e in enemy:
        heapq.heappush(heap, -e)
        total += e
        if total > n:
            if k == 0: break
            total += heapq.heappop(heap)
            k -= 1
        answer += 1

    return answer

# 최소힙으로는 못 푸는 걸까?
# def solution(n, k, enemy):
#     heap = []
#     total = 0
#     answer = 0
#
#     for e in enemy:
#         if len(heap) == k:
#             total += heapq.heappop(heap)
#             heapq.heappush(heap, e)
#             if total > n:
#                 break
#         else:
#             heapq.heappush(heap, e)
#
#         answer += 1
#
#     return answer


solution(7, 3, [4, 2, 4, 5, 3, 3, 1])