def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    parent = [i for i in range(N+1)]

    for i in range(M):
        n1, n2 = lst[i*2], lst[i*2+1]
        union(n1, n2)

    res = 0
    for i in range(1, N+1):
        if parent[i] == i:
            res += 1

    print(f'#{tc} {res}')