# import sys
# input = sys.stdin.readline

from collections import deque

def bfs(s):
    dq = deque()
    dq.append(s)
    visited[s] = 1
    while dq:
        m = dq.popleft()
        for dm in [U, -D]:
            nm = m + dm
            if 1 <= nm <= F and visited[nm] == 0:
                visited[nm] = 1
                count[nm] = count[m] + 1
                if nm == G:
                    return
                dq.append(nm)


F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)
count = [0] * (F+1)

if S == G:
    print(0)
else:
    bfs(S)
    if count[G]:
        print(count[G])
    else:
        print('use the stairs')
