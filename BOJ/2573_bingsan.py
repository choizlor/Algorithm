from collections import deque

def bfs(x,y):
    dq = deque()
    dq.append((x,y))
    visited[x][y] = 1
    while dq:
        x, y = dq.popleft()
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx, ny = x + dx, y + dy
            if 0<=nx<N and 0<=ny<M and ice[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                dq.append((nx,ny))


def melt_f():
    melt = [[0] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if ice[x][y] == 0:
                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if ice[nx][ny]:
                            melt[nx][ny] += 1

    for x in range(N):
        for y in range(M):
            ice[x][y] -= melt[x][y]
            if ice[x][y] < 0:
                ice[x][y] = 0


N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
time = 0

while True:
    melt_f()

    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if ice[x][y] and visited[x][y] == 0:
                bfs(x, y)
                cnt += 1

    if cnt >= 2:
        time += 1
        print(time)
        break
    elif cnt == 1:
        time += 1
    else:
        print(0)
        break
