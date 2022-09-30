def rec(k, midS):
    global minV
    if k > 12:
        return

    if k == 12:
        if midS < minV:
            minV = midS
        return

    rec(k+1, midS + min(fee[1], month[k] * fee[0]))
    rec(k+3, midS + fee[2])


T = int(input())
for tc in range(1, T+1):
    fee = list(map(int, input().split()))
    month = list(map(int, input().split()))
    minV = 100000
    rec(0, 0)
    print(f'#{tc} {min(minV, fee[3])}')
