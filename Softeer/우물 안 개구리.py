import sys

input = sys.stdin.readline

N, M = map(int, input().split())
W = list(map(int, input().split()))
win = [True] * N
answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    if W[a - 1] > W[b - 1]:
        win[b - 1] = False
    elif W[a - 1] < W[b - 1]:
        win[a - 1] = False
    else:
        win[a - 1] = False
        win[b - 1] = False

for w in win:
    if w:
        answer += 1

print(answer)
