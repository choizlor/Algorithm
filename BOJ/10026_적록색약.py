def bfs(x,y,z):
    q = []
    q.append((x,y))
    visited[x][y] = 1
    while q:
        (x, y) = q.pop(0)
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx = x + dx
            ny = y + dy
            w = (nx, ny)
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] == z:
                q.append(w)
                visited[nx][ny] = 1
def bfs_rg(x,y,z):
    q = []
    q.append((x,y))
    visited[x][y] = 1
    while q:
        (x, y) = q.pop(0)
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx = x + dx
            ny = y + dy
            w = (nx, ny)
            if z == 'RG':
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and (arr[nx][ny] == 'R' or arr[nx][ny] == 'G'):
                    q.append(w)
                    visited[nx][ny] = 1
            else:
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] == 'B':
                    q.append(w)
                    visited[nx][ny] = 1


N = int(input())
arr = [input() for _ in range(N)]
cnt1, cnt2 = 0, 0

visited = [[0]*N for _ in range(N)]

for x in range(N):
    for y in range(N):
        if arr[x][y] == 'R' and visited[x][y] == 0:
            bfs(x,y,'R')
            cnt1 += 1
        elif arr[x][y] == 'G' and visited[x][y] == 0:
            bfs(x,y,'G')
            cnt1 += 1
        elif arr[x][y] == 'B' and visited[x][y] == 0:
            bfs(x,y,'B')
            cnt1 += 1

visited = [[0]*N for _ in range(N)]

for x in range(N):
    for y in range(N):
        if (arr[x][y] == 'R' or arr[x][y] == 'G') and visited[x][y] == 0:
            bfs_rg(x,y,'RG')
            cnt2 += 1
        elif arr[x][y] == 'B' and visited[x][y] == 0:
            bfs_rg(x,y,'B')
            cnt2 += 1

print(cnt1, cnt2)