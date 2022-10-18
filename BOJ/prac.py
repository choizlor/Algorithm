d = 1
for dr, dc in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
    d = (d+3) % 4
    print(d)