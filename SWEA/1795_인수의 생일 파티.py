def dijk(N, X, G, d):
    for i in range(N+1):
        d[i] = G[X][i]
    U = [X]
    for _ in range(N-1):
        w = 0
        for i in range(1, N+1):
            if (i not in U) and d[i] < d[w]:
                w = i
        U.append(w)
        for v in range(1, N+1):
            if 0 < G[w][v] < 100000:
                d[v] = min(d[v], d[w] + G[w][v])


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    Gout = [[100000] * (N+1) for _ in range(N+1)]
    Gin = [[100000] * (N+1) for _ in range(N+1)]

    for i in range(N+1):
        Gout[i][i] = 0

    for _ in range(M):
        x, y, c = map(int, input().split())
        Gout[x][y] = c
        Gin[y][x] = c

    dout = [0] * (N+1)
    dijk(N, X, Gout, dout)
    din = [0] * (N+1)
    dijk(N, X, Gin, din)

    maxV = 0
    for i in range(1, N+1):
        maxV = max(maxV, dout[i]+din[i])
    print(f'#{tc} {maxV}')
