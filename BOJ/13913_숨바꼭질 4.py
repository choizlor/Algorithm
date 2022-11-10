from collections import deque

def bfs():
    dq = deque()
    dq.append(N)
    while dq:
        num = dq.popleft()
        if num == K:
            return
        for numx in [num-1, num+1, num*2]:
            if 0<=numx<=100000 and visited[numx] == 0:
                dq.append(numx)
                visited[numx] = visited[num] + 1
                route[numx] = num


N, K = map(int, input().split())
visited = [0] * 100001
route = [0] * 100001
bfs()

result = []
tmp = K
for _ in range(visited[K]+1):
    result.append(tmp)
    tmp = route[tmp]

print(visited[K])
print(*result[::-1])
