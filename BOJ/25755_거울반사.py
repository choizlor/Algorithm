W, N = input().split()
N = int(N)
board = []
answer = [['?'] * N for _ in range(N)]

for _ in range(N):
    board.append(list(map(int, input().split())))

if W == 'L' or W == 'R':
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                answer[i][N - 1 - j] = 1
            elif board[i][j] == 8:
                answer[i][N - 1 - j] = 8
            elif board[i][j] == 2:
                answer[i][N - 1 - j] = 5
            elif board[i][j] == 5:
                answer[i][N - 1 - j] = 2
else:
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                answer[N - 1 - i][j] = 1
            elif board[i][j] == 8:
                answer[N - 1 - i][j] = 8
            elif board[i][j] == 2:
                answer[N - 1 - i][j] = 5
            elif board[i][j] == 5:
                answer[N - 1 - i][j] = 2

for i in range(N):
    print(*answer[i])