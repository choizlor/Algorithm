from collections import deque

def bfs(x, y):
    global maxV
    visited = [[-1]*W for _ in range(L)]
    dq = deque()
    dq.append((x,y))
    visited[x][y] = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0<=nx<L and 0<=ny<W and bomul[nx][ny] == 'L' and visited[nx][ny] == -1:
                dq.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                if visited[nx][ny] > maxV:
                    maxV = visited[nx][ny]


L, W = map(int, input().split())
bomul = [list(input()) for _ in range(L)]
maxV = 0
for x in range(L):
    for y in range(W):
        if bomul[x][y] == 'L':
            bfs(x,y)
print(maxV)