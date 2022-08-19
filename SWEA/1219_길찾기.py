def dfs(v):
    s = []
    s.append(v)
    visited[v] = 1
    result = 0

    while s:
        v = s.pop(-1)

        if visited[99] == 1:
            result = 1
            break

        for w in arr[v]:
            if not visited[w]:
                s.append(w)
                visited[w] = 1

    return result


for _ in range(1, 11):
    t, n = map(int, input().split())

    arr = [[] for _ in range(100)]
    lst = list(map(int, input().split()))

    for i in range(0, n * 2, 2):
        a, b = lst[i], lst[i+1]
        arr[a].append(b)

    visited = [0 for _ in range(100)]

    print(f'#{t} {dfs(0)}')
