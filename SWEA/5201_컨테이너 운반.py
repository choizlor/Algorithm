T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort(reverse=True)
    t.sort(reverse=True)
    sumV = 0
    j = 0

    for i in w:
        if t:
            if i <= t[0]:
                sumV += i
                t.pop(0)

    print(f'#{tc} {sumV}')
