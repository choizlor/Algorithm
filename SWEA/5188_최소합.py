def dfs(x, y, d):
    global minV
    if d > minV:
        return

    if x == N-1 and y == N-1:
        if minV > d:
            minV = d
        return

    else:
        visited[x][y] = 1
        for dx, dy in [[1,0],[0,1]]:
            nx, ny = x + dx, y + dy
            if nx < N and ny < N and visited[nx][ny] == 0:
                dfs(nx, ny, d + arr[nx][ny])
        visited[x][y] = 0
        return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    minV = 100000
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {minV}')

'''
def solve(r, c):
    if r==goalR and c==goalC:
        # path에 있는 합을 구한다.
        return
    
    if midSum > currentMin:
        return
    
    if r+1이 영역 안 일때:
        solve(k+1, r+1, c, midSum+ARR[r+1][c])
    
    if c+1이 영역 안 일때:
        solve(k+1, r, c+1, midSum+ARR[r][c+1])

path = [0] * (N*N)
'''
