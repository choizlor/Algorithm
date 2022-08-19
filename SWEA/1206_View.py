def minF(k, m):
    if k > m:
        k = m
    return k

for t in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    sumV = 0
    for i in range(2, len(lst) - 1):
        if lst[i] == 0:
            continue
        else:
            minV = lst[i] - lst[i - 2]
            if lst[i] > lst[i - 1] and lst[i] > lst[i - 2] and lst[i] > lst[i + 1] and lst[i] > lst[i + 2]:
                minV = minF(minV, lst[i] - lst[i - 1])
                minV = minF(minV, lst[i] - lst[i + 1])
                minV = minF(minV, lst[i] - lst[i + 2])
                sumV += minV

    print(f'#{t} {sumV}')