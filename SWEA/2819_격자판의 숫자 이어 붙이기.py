def dfs(x, y, d, s):
    if d == 7:
        result.append(s)
        return

    else:
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(nx, ny, d+1, s+arr[nx][ny])
        return


T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    result = []
    cnt = 0
    for x in range(4):
        for y in range(4):
            dfs(x, y, 1, arr[x][y])

    print(f'#{tc} {len(set(result))}')
