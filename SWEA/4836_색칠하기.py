T = int(input())
for t in range(1, T + 1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    area = [[0] * 10 for _ in range(10)]
    cnt = 0

    for i in range(n):
        num1, num2, num3, num4 = lst[i][0], lst[i][1], lst[i][2], lst[i][3]
        for j in range(num1, num3 + 1):
            for k in range(num2, num4 + 1):
                if area[j][k] != 0:
                    cnt += 1
                area[j][k] = lst[i][-1]
    print(f'#{t} {cnt}')