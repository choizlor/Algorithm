def dfs(x, y, d, sumV):
    global maxV

    if maxV > sumV + (4-d) * check:
        return

    if d == 4:
        if maxV < sumV:
            maxV = sumV
        return

    for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx, ny = x + dx, y + dy
        if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            if d + 1 == 3:
                dfs(x, y, d+1, sumV+num[nx][ny])
            dfs(nx, ny, d+1, sumV+num[nx][ny])
            visited[nx][ny] = 0


N, M = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(N)]
check = 0

for lst in num:
    check = max(max(lst), check)

visited = [[0] * M for _ in range(N)]
maxV = 0

for x in range(N):
    for y in range(M):
        visited[x][y] = 1
        dfs(x, y, 1, num[x][y])
        visited[x][y] = 0
print(maxV)