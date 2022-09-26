def f(n, x, y):
    w = 4 * n - 3
    h = w + 2

    for i in range(y, w):
        result[x][i] = '*'
        result[h-1][i] = '*'
    for i in range(x, h):
        result[i][y] = '*'
    for i in range(h-w, h-1):
        result[i][w-1] = '*'
    result[h-w][w-2] = '*'

    if n == 2:
        result[x+2][x+2] = '*'
        result[x+2][x+3] = '*'
        result[x+2][x+4] = '*'
        return

    f(n-1, x+2, y+2)


N = int(input())
if N == 1:
    print('*')
else:
    r = 4 * N - 3
    c = r + 2
    result = [[' ' for _ in range(r)] for _ in range(c)]
    f(N, 0, 0)
    for r in result:
        print(''.join(r))
