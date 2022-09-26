def f(n, x, y):
    if n == 1:
        result[x][y] = '*'
        return

    l = 4*(n-1) + 1

    for i in range(x, x + l):
        result[x][i] = '*'
        result[x+l-1][i] = '*'

    for i in range(y+1, y + l):
        result[i][y] = '*'
        result[i][y+l-1] = '*'

    f(n - 1, x + 2, y + 2)


N = int(input())
result = [[' ' for _ in range((4*(N-1) + 1))] for _ in range(4*(N-1) + 1)]
f(N, 0, 0)
for r in result:
    print(''.join(r))