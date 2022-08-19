tc = int(input())

for t in range(1, tc+1):
    n = int(input())
    lst = [sorted(list(map(int, input().split()))) for _ in range(n)]
    ARR = [0 for _ in range(200)]

    for i in range(n):
        for j in range(2):
            if j == 0:
                if lst[i][j] % 2:
                    a = lst[i][j]//2
                else:
                    a = lst[i][j]//2 - 1
            else:
                if lst[i][j] % 2:
                    b = lst[i][j]//2
                else:
                    b = lst[i][j]//2 - 1

        for k in range(a, b+1):
            ARR[k] += 1

    print(f'#{t} {max(ARR)}')
