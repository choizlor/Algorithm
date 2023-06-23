def solution(n):
    board = [[0] * (i + 1) for i in range(n)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            board[x][y] = num
            num += 1

    return sum(board, [])


solution(1000)
