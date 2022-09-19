from collections import deque


def bfs():
    dq = deque()
    dq.append((home[0], home[1]))
    while dq:
        x, y = dq.popleft()
        if abs(x - fes[0]) + abs(y - fes[1]) <= 1000:
            return 'happy'
        for i in range(n):
            if not visited[i]:
                nx, ny = p[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    dq.append((nx, ny))
                    visited[i] = 1
    return 'sad'


t = int(input())

for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    p = []
    for _ in range(n):
        x, y = map(int, input().split())
        p.append((x, y))
    fes = list(map(int, input().split()))
    visited = [0 for _ in range(n)]
    print(bfs())