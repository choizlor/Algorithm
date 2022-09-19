from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in [[-1,0],[0,-1],[1,0],[0,1]]:
            nx = x + dx
            ny = y + dy


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            x, y = i, j
            break
bfs(x, y)