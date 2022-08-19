T = int(input())
for t in range(1, T + 1):
    case = int(input())
    n = case - 1 # 인덱스 맞춰주기 위해서
    num = 1
    lst = [[0] * case for _ in range(case)]

    for i in range(case//2):

        for j in range(i, n-i): # 상
            lst[i][j] = num
            num += 1

        for j in range(i, n-i): # 우
            lst[j][n-i] = num
            num += 1

        for j in range(n-i, i, -1): # 하
            lst[n-i][j] = num
            num += 1

        for j in range(n-i, i, -1): # 좌
            lst[j][i] = num
            num += 1

    if case % 2 != 0: # 홀수일 때 마지막으로 들어갈 값 따로 넣어주기
        lst[n//2][n//2] = num

    print(f'#{t}')

    for k in lst:
        print(' '.join(map(str, k)))