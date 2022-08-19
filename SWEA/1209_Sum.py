def myMax(maxV, num):
    if maxV < num:
        maxV = num
    return maxV

for _ in range(10):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    maxV = 0
    dia1_S = 0
    dia2_S = 0

    for i in range(100):
        col_S = 0
        row_S = 0
        dia1_S += lst[i][i]
        dia2_S += lst[i][99-i]
        for j in range(100):
            col_S += lst[i][j]
            row_S += lst[j][i]
        maxV = myMax(maxV, col_S)
        maxV = myMax(maxV, row_S)

    maxV = myMax(maxV, dia1_S)
    maxV = myMax(maxV, dia2_S)

    print(f'#{n} {maxV}')