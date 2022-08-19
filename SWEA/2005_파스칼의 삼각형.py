# 파스칼의 삼각형
def pascal(n):
    a = [[1] * i for i in range(1, n+1)]
    for i in range(2, n):
        for j in range(1, i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    return a

tc = int(input())
for t in range(1, tc+1):
    n = int(input())

    print(f'#{t}')

    for i in pascal(n):
        print(*i)
