T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    time = sorted(arr, key=lambda x:x[1])
    result = [time[0]]

    for i in range(1, N):
        if result[-1][1] <= time[i][0]:
            result.append(time[i])

    print(f'#{tc} {len(result)}')