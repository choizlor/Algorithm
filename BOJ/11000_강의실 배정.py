import heapq

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
heap = []

arr.sort(key=lambda x:x[0])
heapq.heappush(heap, arr[0][1])

for i in range(1, N):
    if heap[0] > arr[i][0]:
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])

print(len(heap))