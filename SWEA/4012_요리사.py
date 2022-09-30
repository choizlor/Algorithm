def dfs(L, B):
    global minV

    if L == r:
        food1, food2 = 0, 0
        f1 = result[:]
        f2 = [i for i in num if i not in f1]
        for i in f1:
            for j in f1:
                if i != j and ing[i][j]:
                    food1 += ing[i][j]
        for i in f2:
            for j in f2:
                if i != j and ing[i][j]:
                    food2 += ing[i][j]

        if minV > abs(food1 - food2):
            minV = abs(food1 - food2)

    else:
        for i in range(B, len(num)):
            result[L] = num[i]
            dfs(L+1, i+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ing = [list(map(int, input().split())) for _ in range(N)]
    num = [i for i in range(N)]
    r = N // 2
    result = [False] * r
    minV = 1000000
    dfs(0, 0)
    print(f'#{tc} {minV}')
