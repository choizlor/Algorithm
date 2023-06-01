W, N = map(int, input().split())
price = []
answer = 0

for i in range(N):
    M, P = map(int, input().split())
    price.append([P, M])

price = sorted(price, key=lambda x: -x[0])

for p in price:
    if W - p[1] >= 0:
        answer += p[0] * p[1]
        W -= p[1]
    else:
        answer += W * p[0]
        break

print(answer)
