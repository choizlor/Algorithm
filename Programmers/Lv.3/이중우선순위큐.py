import heapq


def solution(operations):
    heap = []
    for o in operations:
        check, num = o.split(" ")
        if check == 'D' and heap == []:
            continue

        if check == "D" and num == "1":
            heap.pop()
        elif check == "D" and num == "-1":
            heapq.heappop(heap)
        elif check == "I":
            heapq.heappush(heap, int(num))

    heap.sort()

    if heap:
        return [heap[-1], heap[0]]
    else:
        return [0, 0]


solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
