def par(k, curSum):
    global minV
    if curSum - B >= minV:
        return

    if k == N:
        if curSum >= B:
            if curSum - B < minV:
                minV = curSum - B
    else:
        result[k] = 0
        par(k+1, curSum)

        result[k] = 1
        par(k+1, curSum+key[k])


tc = int(input())

for t in range(1, tc+1):
    N, B = map(int, input().split())
    key = list(map(int, input().split()))
    minV = 10000000
    result = [-1] * N
    par(0, 0)
    print(f'#{t} {minV}')