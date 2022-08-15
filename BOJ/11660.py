N, M = map(int, input().split())
test = [[0] * (N+1) for _ in range(N+1)]
lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        test[i + 1][j + 1] = (test[i][j + 1] + test[i + 1][j] - test[i][j]) + lst[i][j]

# for i in range(N):
#     for j in range(1, N):
#         lst[i][j] = lst[i][j-1] + lst[i][j]
#
# for i in range(N):
#     for j in range(1, N):
#         lst[j][i] = lst[j-1][i] + lst[j][i]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(test[x2][y2] - test[x1-1][y2] - (test[x2][y1-1] - test[x1-1][y1-1]))

