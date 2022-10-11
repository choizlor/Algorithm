def comb(L, B):
    if L == 6:
        print(*result)
    else:
        for i in range(B, len(lst)):
            result[L] = lst[i]
            comb(L + 1, i + 1)


while True:
    num = list(map(int, input().split()))
    if num == [0]:
        break
    else:
        lst = num[1:]
        result = [False] * 6
        comb(0, 0)
        print()