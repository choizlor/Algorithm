def solve(x, y, n):
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                result.append('(')
                solve(x, y, n//2)
                solve(x, y + n//2, n//2)
                solve(x + n//2, y, n//2)
                solve(x + n//2, y + n//2, n//2)
                result.append(')')
                return

    if color == '0':
        result.append('0')
    else:
        result.append('1')


N = int(input())
arr = [list(input()) for _ in range(N)]
result = []
solve(0, 0, N)
print(''.join(result))