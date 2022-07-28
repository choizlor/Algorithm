import math

T = int(input())
for t in range(1, T + 1):
    lst = []
    for i in range(9):
        lst.append(list(map(int, input().split())))

    for i in range(9):
        mul = 1
        for j in range(9):
            mul *= lst[i][j]
            mul *= lst[j][i]
            mul *= lst[i//3 * 3 + j % 3][i//3 * 3 + j // 3]
        if mul == math.factorial(9) * math.factorial(9) * math.factorial(9):
            result = 1
        else:
            result = 0
            break

    print(f'#{t} {result}')