from collections import deque

def bfs():
    dq = deque()
    dq.append(N)
    visited[N] = 1
    while dq:
        a = dq.popleft()
        if a == M:
            return
        for i in [a+1, a-1, a*2, a-10]:
            if 0 < i <= 1000000 and visited[i] == 0:
                dq.append(i)
                visited[i] = visited[a] + 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    bfs()
    print(f'#{tc} {visited[M]-1}')
