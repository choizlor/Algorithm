def dfs(v):
    result = []
    visited = [0] * (1000 + 1)
    q = []
    q.append(v)
    visited[v] = 1
    result.append(v)
    while q:
        v = q.pop()
        if visited[v] == 0:
            result.append(v)
            visited[v] = 1
        adjList[v].sort(reverse=True)
        for w in adjList[v]:
            if visited[w] == 0:
                q.append(w)
    return result

def bfs(v):
    result = []
    visited = [0] * (1000 + 1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        visited[v] = 1
        result.append(v)
        for w in adjList[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1
    return result


N, M, V = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

adjList = [[] for _ in range(1001)]

for i in range(M):
    a, b = arr[i][0], arr[i][1]
    adjList[a].append(b)
    adjList[b].append(a)

print(*dfs(V))
for i in adjList:
    i.sort()
print(*bfs(V))