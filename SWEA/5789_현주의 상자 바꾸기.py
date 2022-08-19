tc = int(input())

for t in range(1, tc+ 1):
    N, Q = map(int, input().split())
    lst = [0 for _ in range(N)]
    check = [list(map(int, input().split())) for _ in range(Q)]

    for i in range(Q):
        for j in range(check[i][0]-1, check[i][1]):
            lst[j] = i + 1

    print(f'#{t}', *lst)
