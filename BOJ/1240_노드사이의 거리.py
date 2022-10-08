from collections import deque

def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a] = 0
    while q:
        a, b = q.popleft()
        if a == b:
            print(visited[b])
            return
        for i in range(1, N+1):
            if G[a][i] and visited[i] == -1:
                q.append((i, b))
                visited[i] = visited[a] + G[a][i]


N, M = map(int, input().split())
G = [[0] * (N+1) for _ in range(N+1)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    G[u][v] = w
    G[v][u] = w

for _ in range(M):
    a, b = map(int, input().split())
    if G[a][b] == 0:
        visited = [-1] * (N+1)
        bfs(a, b)
    else:
        print(G[a][b])
