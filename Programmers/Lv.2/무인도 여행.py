def solution(maps):
    answer = []
    m = len(maps[0])
    visited = [[0] * m for _ in range(len(maps))]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(len(maps)):
        for j in range(m):
            if maps[i][j] != "X" and visited[i][j] == 0:
                period = 0
                q = [(i, j)]

                while q:
                    x, y = q.pop()
                    if visited[x][y]:
                        continue
                    visited[x][y] = 1
                    period += int(maps[x][y])

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if -1 < nx < len(maps) and -1 < ny < m and maps[nx][ny] != 'X' and not visited[nx][ny]:
                            q.append((nx, ny))

                answer.append(period)

    return sorted(answer) if answer else [-1]


solution(["X591X", "X1X5X", "X231X", "1XXX1"])
