import copy

def bfs(x, y):
    q = []
    q.append((x, y))
    testA[x][y] = 0
    while q:
        x, y = q.pop(0)
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and testA[nx][ny]:
                q.append((nx, ny))
                testA[nx][ny] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

maxlst = []
for i in range(N):
    maxlst.append(max(arr[i]))
maxV = max(maxlst)

result = []

for num in range(0, maxV):
    cnt = 0
    testA = copy.deepcopy(arr)

    for i in range(N):
        for j in range(N):
            if testA[i][j] <= num:
                testA[i][j] = 0

    for x in range(N):
        for y in range(N):
            if testA[x][y]:
                bfs(x, y)
                cnt += 1
    
    result.append(cnt)

print(max(result))