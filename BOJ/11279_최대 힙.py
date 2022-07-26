import sys
import heapq

N = int(input())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, -num)