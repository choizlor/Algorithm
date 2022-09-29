from collections import deque

def bfs():
    q = deque()
    q.append([0,0])
    while q:
        x, y = q.popleft()
        for dx, dy in [[-1,0],[0,1],[1,0],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                tmp = max(arr[nx][ny] - arr[x][y], 0)
                if tmp + 1 + result[x][y] < result[nx][ny]:
                    result[nx][ny] = tmp + result[x][y] + 1
                    q.append([nx, ny])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [[10000 for _ in range(N)] for _ in range(N)]
    result[0][0] = 0
    bfs()
    print(f'#{tc} {result[N-1][N-1]}')
