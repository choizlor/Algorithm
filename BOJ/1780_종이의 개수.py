def count(n):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == n:

N = int(input())
arr = [list(map(int, input().split()) for _ in range(N)]
