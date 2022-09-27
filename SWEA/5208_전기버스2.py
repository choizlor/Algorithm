def dfs(s, b, cnt):
    global minV

    if s + b >= N - 1:
        if minV > cnt:
            minV = cnt
        return

    else:
        if minV <= cnt:
            return
        for k in range(s+1, s+b+1):
            if k <= N-1:
                dfs(k, battery[k], cnt+1)


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    battery = lst[1:]
    minV = 10000000
    dfs(0, battery[0], 0)
    print(f'#{tc} {minV}')