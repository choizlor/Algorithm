from collections import deque

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] + visited[x][y] < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    q.append((nx, ny))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[1000000] * N for _ in range(N)]
    bfs()
    print(f'#{tc} {visited[N-1][N-1]}')