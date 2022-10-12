from collections import deque

def bfs():
    cnt = 0
    dq = deque()
    dq.append((0, 0))
    visited[0][0] = 1
    while dq:
        c, r = dq.popleft()
        for dc, dr in [[1,0],[-1,0],[0,1],[0,-1]]:
            nc, nr = c + dc, r + dr
            if 0<=nc<col and 0<=nr<row and visited[nc][nr] == 0:
                if cheeze[nc][nr] == 0:
                    visited[nc][nr] = 1
                    dq.append((nc, nr))

                elif cheeze[nc][nr] == 1:
                    cheeze[nc][nr] = 0
                    visited[nc][nr] = 1
                    cnt += 1

    return cnt


col, row = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(col)]
time = 0
result = []

while True:
    visited = [[0] * row for _ in range(col)]
    cnt = bfs()
    if cnt != 0:
        result.append(cnt)
        time += 1
    else:
        break

print(time)
print(result[-1])
