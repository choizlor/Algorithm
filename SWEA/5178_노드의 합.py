tc = int(input())
for t in range(1, tc+1):
    N, M, L = map(int, input().split())
    num = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        num[a] = b

    for i in range(N, 0, -1):
        if i // 2 > 0:
            num[i//2] += num[i]

    print(f'#{t} {num[L]}')