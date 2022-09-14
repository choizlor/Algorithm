from collections import deque

def bfs(s):
    dq = deque()
    dq.append(s)
    while dq:
        sumV = 0
        m = dq.popleft()
        while 1 <= sumV <= F:
            sumV = m + U

# 최단거리처럼 풀면 될듯.
F, S, G, U, D = map(int, input().split())
bfs(S)