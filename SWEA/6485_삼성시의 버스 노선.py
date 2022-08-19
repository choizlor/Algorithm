tc = int(input())

for t in range(1, tc+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C_lst = [int(input()) for _ in range(P)]

    test_lst = [0] * 5001
    result = []

    for i in range(N):
        for j in range(lst[i][0], lst[i][1] + 1):
            test_lst[j] += 1

    for i in C_lst:
        result.append(test_lst[i])

    print(f'#{t}', end=' ')
    print(*result)
