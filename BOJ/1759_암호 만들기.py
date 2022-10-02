def f(lst):
    num = [0, 0]
    for i in lst:
        if i in ['a', 'e', 'i', 'o', 'u']:
            num[0] += 1
        else:
            num[1] += 1
    return num

def DFS(L, BeginWith):
    if L == N:
        check = f(result)
        if check[0] >= 1 and check[1] >= 2:
            print(''.join(result))
    else:
        for i in range(BeginWith, M):
            result[L] = p[i]
            DFS(L + 1, i + 1)


N, M = map(int, input().split())
p = sorted(list(input().split()))
result = [False] * N
res = []
DFS(0, 0)
