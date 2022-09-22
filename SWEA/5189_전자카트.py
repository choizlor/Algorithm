def perm(k, midSum, s):
    global minV
    if minV < midSum:
        return

    if k == N:
        midSum += arr[s][0]
        minV = min(minV, midSum)
        return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        perm(k+1, midSum + arr[s][i], i)
        visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    minV = 100000000

    visited[0] = True
    perm(1, 0, 0)
    print(f'#{tc} {minV}')