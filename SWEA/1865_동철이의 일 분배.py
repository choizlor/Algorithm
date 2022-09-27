def f(i, k, s):
    global maxV

    if maxV >= s:
        return

    if i == k:
        if maxV < s:
            maxV = s
        return

    else:
        for j in range(i, k):
            a[i], a[j] = a[j], a[i]
            f(i+1, k, (arr[i][a[i]]/100) * s)
            a[i], a[j] = a[j], a[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a = [i for i in range(N)]
    maxV = 0
    f(0, N, 1)
    print(f'#{tc} {maxV*100:.6f}')