def charge(k, remain, cntChg):
    global minV

    if cntChg > minV:
        return

    # 도착지 도달
    if k == N:
        if cntChg < minV:
            minV = cntChg
        return

    if remain == 0:
        return

    charge(k+1, remain-1, cntChg)
    charge(k+1, lst[k+1], cntChg+1)


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split())) + [0]
    N = lst[0]
    result = [-1] * N
    minV = 100000
    charge(1, lst[1], 0)
    print(f'#{tc} {minV}')