def solve(x, y, N):
    global cnt1, cnt2, cnt3

    num = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if num != arr[i][j]:
                n = N//3

                solve(x, y, n)
                solve(x, y+n, n)
                solve(x, y+2*n, n)

                solve(x+n, y, n)
                solve(x+n, y+n, n)
                solve(x+n, y+2*n, n)

                solve(x+2*n, y, n)
                solve(x+2*n, y+n, n)
                solve(x+2*n, y+2*n, n)
                return

    if num == -1:
        cnt1 += 1
    elif num == 0:
        cnt2 += 1
    else:
        cnt3 += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt1 = cnt2 = cnt3 = 0
solve(0, 0, N)
print(cnt1)
print(cnt2)
print(cnt3)