def bfs():



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    node = [[] for _ in range(N+1)]
    lst = list(map(int, input().split()))
    for i in range(M):
        n1 = lst[i*2]
        n2 = lst[i*2+1]
        node[n1].append(n2)


