def bfs(x, y):
    q = []
    q.append((x, y))
    visited[x][y] = 1
    while q:
        (x, y) = q.pop(0)
        if chess_board[x][y] == 1000:
            return
        for dx, dy in [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < chess_len and 0 <= ny < chess_len and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


tc = int(input())
for _ in range(tc):
    chess_len = int(input())
    chess_board = [[0] * chess_len for _ in range(chess_len)]
    visited = [[0] * chess_len for _ in range(chess_len)]

    x, y = map(int, input().split())
    x1, y1 = map(int, input().split())
    chess_board[x][y] = 1
    chess_board[x1][y1] = 1000

    bfs(x, y)

    print(visited[x1][y1]-1)
