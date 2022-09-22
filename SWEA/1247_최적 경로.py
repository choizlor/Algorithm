def dfs(idx, lastx, lasty, d):
    global minV
    if minV < d:
        return
    if idx == n:
        d += abs(lastx - home[0]) + abs(lasty - home[1])
        minV = min(d, minV)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            temp = d + abs(lastx - client[i][0]) + abs(lasty - client[i][1])
            dfs(idx+1, client[i][0], client[i][1], temp)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    company = [arr[0], arr[1]]
    home = [arr[2], arr[3]]
    client = []
    for i in range(4, len(arr), 2):
        client.append([arr[i], arr[i+1]])
    visited = [0 for _ in range(n)]
    minV = 100000
    dfs(0, company[0], company[1], 0)
    print(f'#{tc} {minV}')