from collections import deque
import copy

def bfs():
    global maxV
    dq = deque()
    dq += lst
    check = copy.deepcopy(virus)

    while dq:
        i, j = dq.popleft()
        for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and not check[ni][nj]:
                check[ni][nj] = 2
                dq.append((ni,nj))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not check[i][j]:
                cnt += 1
    maxV = max(maxV, cnt)


def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if virus[i][j] == 0:
                virus[i][j] = 1
                wall(cnt+1)
                virus[i][j] = 0


N, M = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]
lst = deque()
for i in range(N):
    for j in range(M):
        if virus[i][j] == 2:
            lst.append((i, j))

maxV = 0
wall(0)
print(maxV)