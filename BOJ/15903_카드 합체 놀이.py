n, m = map(int, input().split())
card = sorted(list(map(int, input().split())))

for _ in range(m):
    sumV = card[0] + card[1]
    card[0] = sumV
    card[1] = sumV
    card.sort()

print(sum(card))