from collections import deque

def bfs(r,c,d):
    dq = deque()
    dq.append((r,c,d))
    while dq:
        check = 1
        r, c, d = dq.popleft()
        visited[r][c] = 1

        for _ in range(4):
            d = (d+3) % 4
            dr, dc = dir[d]
            nr, nc = r + dr, c + dc
            if arr[nr][nc] == 0 and visited[nr][nc] == 0:
                dq.append((nr,c,d))
                check = 0
                break

        if check == 1:
            dr, dc = h[d]
            nr, nc = r + dr, c + dc
            if arr[nr][nc] == 0:
                dq.append((nr,nc,d))
            else:
                break


N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dir = [[-1,0],[0,1],[1,0],[0,-1]]
h = [[1,0],[0,-1],[-1,0],[0,1]]

bfs(r,c,d)

cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            cnt += 1
print(cnt)