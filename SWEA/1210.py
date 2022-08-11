for _ in range(10):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    # 왼, 오, 위
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    curC = -1
    curR = 99
    for i in range(100):
        if board[-1][i] == 2:
            curC = i

    while curR >= 0:
        if curR == 0:
            break

        for d in range(3):
            newR = curR + dr[d]
            newC = curC + dc[d]

            if 100 > newR >= 0 and 100 > newC >= 0 and board[newR][newC] == 1:
                board[newR][newC] = -1
                curC = newC
                curR = newR
                break

    print(f'#{n} {curC}')