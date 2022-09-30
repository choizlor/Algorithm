def prim():
    U = []
    D = [10000] * (N+1)
    P = [10000] * (N+1)
    D[0] = 0
    while len(U) < (N+1):
        # curV = D중 가장 작은 값을 가진 정점을 선택
        minV = 10000
        for i in range(N+1):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)
        # curV하과 연결된 정점들의 D값을 최선으로 바꿔준다.
        for i in range(N+1):
            if i in U: continue
            if G[curV][i] and D[i] > G[curV][i]:
                D[i] = G[curV][i]
                P[i] = curV

    print(U, D, P)


N, E = map(int, input().split())
G = [[0]*(N+1) for _ in range(N+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u][v] = w
    G[v][u] = w

prim()