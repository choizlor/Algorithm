def binarySearch(l, N, key):
    start = 0
    end = N - 1
    cnt = 0
    while start <= end:
        middle = (start + end) // 2
        if l[middle] == key:
            return cnt
        elif l[middle] > key:
            end = middle
        else:
            start = middle
        cnt += 1


T = int(input())
for t in range(1, T+1):

    p, a, b = map(int, input().split())
    lst = [_ for _ in range(1, p + 1)]

    if binarySearch(lst, p, a) < binarySearch(lst, p, b):
        res = 'A'
    elif binarySearch(lst, p, a) == binarySearch(lst, p, b):
        res = '0'
    else:
        res = 'B'

    print(f'#{t} {res}')