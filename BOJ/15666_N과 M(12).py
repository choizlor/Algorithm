def DFS(L, BeginWith):
    if L == M:
        lst = result[:]
        if lst not in res:
            res.append(lst)
            print(*lst)
    else:
        for i in range(BeginWith, len(p)):
            result[L] = p[i]
            DFS(L+1, i)


N, M = map(int, input().split())
p = sorted(list(set(map(int, input().split()))))
result = [False] * M
res = []
DFS(0, 0)