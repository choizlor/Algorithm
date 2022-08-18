from collections import deque

n = int(input())
card = [i for i in range(1, n+1)]
q = deque(card)

while len(q) > 1:
    q.popleft()
    up = q.popleft()
    q.append(up)

print(*q)