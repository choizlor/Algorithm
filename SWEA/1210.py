board = [list(map(int, input().split())) for _ in range(10)]
for i in range(10):
    board[i].append(0)

dy = [0, 0, -1]
dx = [-1, 1, 0]

for j in range(10):
    if board[-1][j] == 2:
        nx = j

for ny in range(9, -1, -1):
    if board[ny][nx - 1] == 0 and board[ny][nx + 1] == 0:
        continue
    else:
        if board[ny][nx - 1] == 1:
            while board[ny][nx] > 0:
                nx -= 1
        elif board[ny][nx + 1] == 1:
            while board[ny][nx] > 0:
                nx += 1

print(nx)

# 1 0 0 0 1 0 1 0 0 1
# 1 0 0 0 1 0 1 1 1 1
# 1 0 0 0 1 0 1 0 0 1
# 1 0 0 0 1 1 1 0 0 1
# 1 0 0 0 1 0 1 0 0 1
# 1 1 1 1 1 0 1 1 1 1
# 1 0 0 0 1 0 1 0 0 1
# 1 1 1 1 1 0 1 0 0 1
# 1 0 0 0 1 1 1 0 0 1
# 1 0 0 0 1 0 1 0 0 2