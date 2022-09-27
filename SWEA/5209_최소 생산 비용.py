def f(i, k, s):
    global minV

    if minV < s:
        return

    if i == k:
        if minV > s:
            minV = s
        return
    else:
        for j in range(i, k):
            a[i], a[j] = a[j], a[i]
            f(i+1, k, arr[i][a[i]] + s)
            a[i], a[j] = a[j], a[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a = [i for i in range(N)]
    minV = 10000000
    f(0, N, 0)

    print(f'#{tc} {minV}')


