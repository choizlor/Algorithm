from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(start, end, maps):
    V = [[0] * len(maps[0]) for _ in range(len(maps))]
    n = len(maps)
    m = len(maps[0])
    q = deque()
    check = False

    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                q.append((i, j))
                V[i][j] = 1
                check = True
                break
        if check: break

    while q:
        x, y = q.popleft()

        if maps[x][y] == end:
            return V[x][y] - 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not V[nx][ny] and maps[nx][ny] != 'X':
                V[nx][ny] = V[x][y] + 1
                q.append((nx, ny))

    return -1


def solution(maps):
    a = bfs('S', 'L', maps)
    b = bfs('L', 'E', maps)

    if a != -1 and b != -1:
        return a + b
    else:
        return -1


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"])
