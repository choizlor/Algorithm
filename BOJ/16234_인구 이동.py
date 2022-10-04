def bfs(r, c):
    q = []
    q.append((r,c))
    visited[r][c] = 1

    while q:
        r, c = q.pop(0)
        for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
            nr = r + dr
            nc = c + dc
            if 0<=nr<N and 0<=nc<N and L <= abs(A[r][c] - A[nr][nc]) <= R and not visited[nr][nc]:
                visited[nr][nc] = 1
                value.append(A[nr][nc])
                rc.append([nr,nc])
                q.append((nr,nc))

    return value


N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
result = 0

while True:
    visited = [[0] * N for _ in range(N)]   # 방문한 곳 체크
    check = 0

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                value = [A[r][c]]
                rc = [[r, c]]
                g = bfs(r, c)
                aver = sum(g)//len(g)

                if len(rc) > 1:    # 초기값이 아니면
                    check = 1   # while문 루프 조건
                    for i in rc:
                        x, y = i[0], i[1]
                        A[x][y] = aver

    if check == 0:
        break
    else:
        result += 1

print(result)