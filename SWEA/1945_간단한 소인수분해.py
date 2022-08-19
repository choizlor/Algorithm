tc = int(input())

for t in range(1, tc+1):
    num = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0

    while num > 1:
        if num % 11 == 0:
            e += 1
            num //= 11
        elif num % 7 == 0:
            d += 1
            num //= 7
        elif num % 5 == 0:
            c += 1
            num //= 5
        elif num % 3 == 0:
            b += 1
            num //= 3
        elif num % 2 == 0:
            a += 1
            num //= 2

    print(f'#{t} {a} {b} {c} {d} {e}')