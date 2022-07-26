T = int(input())
for num in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    a_price = p * w
    b_price = q
    if w > r:
        b_price += (w - r) * s
    if a_price < b_price:
        result = a_price
    else:
        result = b_price
    print(f'#{num} {result}')