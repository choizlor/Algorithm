def dfs(x, y, depth, midLst):
    if depth == M:
        if sum(midLst) > C:
            maxV = 0
            for i in range(1 << len(midLst)):
                subset = []
                for j in range(len(midLst)):
                    if i & (1 << j):
                        subset.append(midLst[j])
                if sum(subset) <= C:
                    sumV1 = 0
                    for i in subset:
                        sumV1 += i ** 2
                    if maxV < sumV1:
                        maxV = sumV1
            lst.append(maxV)
        else:
            sumV = 0
            for i in midLst:
                sumV += i**2
            lst.append(sumV)
        return

    nx, ny = x, y + 1
    if 0<=ny<N and visited[nx][ny] == 0:
        dfs(nx, ny, depth+1, midLst+[honey[nx][ny]])


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    lst = []
    for i in range(N):
        for j in range(N):
            visited[i][j] = 1
            dfs(i, j, 1, [honey[i][j]])

    result = sorted(list(set(lst)), reverse=True)
    print(f'#{tc}', result[0]+result[1])