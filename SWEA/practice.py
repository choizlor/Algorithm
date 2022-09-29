def DFS(L, BeginWith):
    # 종료조건 (depth, level 등)
    if L == r:
        print(result)
    else:
        for i in range(BeginWith, len(n)):
            result[L] = n[i]
            DFS(L + 1, i + 1)


n = [1, 2, 3, 4, 5, 6]
r = 3

result = [False] * r

DFS(0, 0)