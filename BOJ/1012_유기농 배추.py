def bfs(x, y):
    q = []
    q.append((x, y))
    arr[x][y] = 0
    while q:
        (i, j) = q.pop(0)
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = i + dx
            ny = j + dy
            w = (nx, ny)
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 1:
                q.append(w)
                arr[nx][ny] = 0


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*N for _ in range(M)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1

    for x in range(M):
        for y in range(N):
            if arr[x][y] == 1:
                bfs(x, y)
                cnt += 1

    print(cnt)