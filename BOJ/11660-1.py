N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     for j in range(1, N):
#         if i > 0 and j == 1:
#             lst[i][j-1] = lst[i-1][-1] + lst[i][j-1]
#         lst[i][j] = lst[i][j-1] + lst[i][j]
#     if i > 0:
#         lst[i][0] = lst[i-1][N-1]

for i in range(N):
    for j in range(1, N):
        if i > 0 and j == 1:
            lst[i][j-1] = lst[i-1][-1] + lst[i][j-1]
        lst[i][j] = lst[i][j-1] + lst[i][j]
    if i > 0:
        lst[i].insert(0, lst[i-1][-1])
    else:
        lst[i].insert(0, 0)

for _ in range(M):
    a, b, c, d = map(int, input().split())

    if (a == c and b == d) or b == 1:
        print(lst[c-1][d]-lst[a-1][b-1])
    else:
        print(lst[c-1][d] - lst[a-1][b])

# for _ in range(M):
#     sumV = 0
#     a, b, c, d = map(int, input().split())
#     for i in range(a-1, c):
#         for j in range(b-1, d):
#             sumV += lst[i][j]
#     print(sumV)