def dfs():

N, M = map(int, input().split())
G = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N-1):
    u, v, w = map(int, input().split())
    G[u][v] = w
    G[v][u] = w

print(G)