def f(n, x, y):
    w = 4 * n - 3
    h = w + 2

    for i in range(y, x-1, -1):
        result[x][i] = '*'
        result[x+h-1][i] = '*'

    for i in range(x, x + h):
        result[i][x] = '*'

    for i in range(x+2, x + h):
        result[i][y] = '*'
    result[x+2][y-1] = '*'

    if n == 2:
        result[x+2][x+2] = '*'
        result[x+3][x+2] = '*'
        result[x+4][x+2] = '*'
        return

    f(n-1, x+2, y-2)


N = int(input())
if N == 1:
    print('*')
else:
    r = 4 * N - 3
    c = r + 2
    result = [[' ' for _ in range(r)] for _ in range(c)]
    f(N, 0, r-1)
    for r in range(c):
        if r == 1:
            print('*')
        else:
            print(''.join(result[r]))
