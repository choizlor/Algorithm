def DFS(L, BeginWith):
  # 종료조건 (depth, level 등)
    if L == M:
        lst = result[:]
        if lst not in res:
            res.append(lst)
    else:
        for i in range(BeginWith, len(p)):
            result[L] = p[i]
            DFS(L+1, i)


N, M = map(int, input().split())
p = list(map(int, input().split()))
result = [False] * M
res = []
DFS(0, 0)
print(res)