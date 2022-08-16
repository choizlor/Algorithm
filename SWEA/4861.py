# 회문

tc = int(input())
for t in range(1, tc + 1):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]
    test = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            test[i] += lst[j][i]
        test[i] = ''.join(test[i])

    result = ''

    for i in lst:
        for j in range(N-M+1):
            check = i[0+j:M+j]
            if check == check[::-1]:
                result = check

    for i in test:
        for j in range(N-M+1):
            check = i[0+j:M+j]
            if check == check[::-1]:
                result = check

    print(f'#{t} {result}')