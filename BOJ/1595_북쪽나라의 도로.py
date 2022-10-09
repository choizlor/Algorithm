def dfs(a, s):
    global maxV

    if maxV < s:
        maxV = s

    for n, d in G[a]:
        if not visited[n]:
            visited[n] = 1
            dfs(n, s + d)
            visited[n] = 0


check = []
N = 1
while True:
    try:
        s, e, w = map(int, input().split())
        check.append([s,e,w])
        N += 1
    except:
        break

G = [[] for _ in range(10001)]
for c in check:
    G[c[0]].append([c[1],c[2]])
    G[c[1]].append([c[0],c[2]])

maxV = 0
for i in range(1, N+1):
    visited = [0] * (N+1)
    visited[i] = 1
    dfs(i, 0)

print(maxV)