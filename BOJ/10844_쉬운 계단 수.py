# 백준 10844

n = int(input())
lst = []
for i in range(n):
    lst.append([])

for i in range(1, 10):
    lst[0].append(i)

for i in range(n - 1):
    for j in range(len(lst[i])):
        if lst[i][j] % 10 > 0:
            lst[i + 1].append(lst[i][j] * 10 + (lst[i][j] % 10) - 1)
        if lst[i][j] % 10 < 9:
            lst[i + 1].append(lst[i][j] * 10 + (lst[i][j] % 10) + 1)

print(len(lst[n - 1]) % 1000000000)