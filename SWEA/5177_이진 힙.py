def enq(n):
    global last
    last += 1
    heap[last] = n

    c = last
    p = c//2

    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2


tc = int(input())

for t in range(1, tc+1):
    N = int(input())
    heap = [0] * (N+1)
    last = 0
    lst = list(map(int, input().split()))
    result = 0

    for i in lst:
        enq(i)

    while N > 0:
        N = N//2
        result += heap[N]

    print(f'#{t} {result}')
