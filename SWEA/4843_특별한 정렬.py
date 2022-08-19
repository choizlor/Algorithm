def selectSort(lst, N):
    for i in range(N-1):
        maxIdx = i
        minIdx = i
        if i % 2 == 0:
            for j in range(i+1, N):
                if lst[maxIdx] < lst[j]:
                    maxIdx = j
            lst[i], lst[maxIdx] = lst[maxIdx], lst[i]
        else:
            for j in range(i+1, N):
                if lst[minIdx] > lst[j]:
                    minIdx = j
            lst[i], lst[minIdx] = lst[minIdx], lst[i]
    return lst


T = int(input())

for t in range(1, T+1):

    n = int(input())
    lst = list(map(int, input().split()))

    result = ' '.join(map(str, selectSort(lst, n)[:10]))

    print(f'#{t} {result}')