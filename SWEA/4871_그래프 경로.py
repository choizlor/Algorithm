def dfs(start):
    for i in range(1, V + 1):
        if lst[start][i] == 1 and visited[i] == 0:
            lst[S][i] = 1
            visited[i] = 1
            dfs(i)

tc = int(input())

for t in range(1, tc+1):
    V, E = map(int, input().split())
    lst = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        lst[a][b] = 1

    S, G = map(int, input().split())

    visited = [0] * (V + 1)
    visited[S] = 1
    dfs(S)

    print(f'#{t} {lst[S][G]}')
