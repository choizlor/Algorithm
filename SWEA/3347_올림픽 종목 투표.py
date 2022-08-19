tc = int(input())

for t in range(1, tc+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    test_dict = {}
    maxV = 0

    for i in range(1, N+1):
        test_dict[i] = 0

    for j in B:
        for i in range(N):
            if j >= A[i]:
                test_dict[i+1] += 1
                break

    for i in range(1, N+1):
        if maxV < test_dict[i]:
            maxV = test_dict[i]
            result = i

    print(f'#{t} {result}')