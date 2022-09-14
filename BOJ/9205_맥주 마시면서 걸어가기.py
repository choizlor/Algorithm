t = int(input())

for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n+2)]
    # beer = 20
    result = 'happy'

    for i in range(n+1):
        if (abs(arr[i+1][0] - arr[i][0]) + abs(arr[i+1][1] - arr[i][1])) / 50 > 20:
            result = 'sad'
            break

    print(result)