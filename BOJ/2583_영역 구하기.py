def bfs(x, y):
    s = 1
    q = []
    q.append((x, y))
    arr[x][y] = 0
    while q:
        x, y = q.pop(0)
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 1:
                s += 1
                q.append((nx, ny))
                arr[nx][ny] = 0
    result.append(s)

M, N, K = map(int, input().split())
arr = [[1]*N for _ in range(M)]
result = []
cnt = 0

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[y][x] = 0

for x in range(M):
    for y in range(N):
        if arr[x][y] == 1:
            bfs(x, y)
            cnt += 1

result = sorted(result)

print(cnt)
print(*result)
