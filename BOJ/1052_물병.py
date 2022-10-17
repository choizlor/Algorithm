def solve(num):
    cnt = 0
    while True:
        a = num // 2
        b = num % 2
        cnt += b
        num = a
        if num == 0:
            break
    return cnt


N, K = map(int, input().split())

if K >= N:
    print(0)
else:
    num = N
    while True:
        if solve(num) <= K:
            print(num - N)
            break
        else:
            num += 1