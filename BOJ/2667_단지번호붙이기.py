def bfs(x, y):
    s = 1
    q = []
    q.append((x, y))
    arr[x][y] = 0
    while q:
        x, y = q.pop(0)
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                s += 1
                q.append((nx, ny))
                arr[nx][ny] = 0
    result.append(s)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
result = []
cnt = 0

for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            bfs(x, y)
            cnt += 1

result.sort()

print(cnt)
for i in result:
    print(i)