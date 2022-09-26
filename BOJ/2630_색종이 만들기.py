def solve(x, y, n):
    global cnt_w, cnt_b

    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                solve(x, y, n//2)
                solve(x, y + n//2, n//2)
                solve(x + n//2, y, n//2)
                solve(x + n//2, y + n//2, n//2)
                return

    if color == 0:
        cnt_w += 1
    else:
        cnt_b += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt_w = cnt_b = 0
solve(0, 0, N)
print(cnt_w)
print(cnt_b)