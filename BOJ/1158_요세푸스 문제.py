N, K = map(int, input().split())

lst = [i + 1 for i in range(N)]
res = []
idx = K - 1

while lst:
    if idx > len(lst)-1:
        idx -= len(lst)
    else:
        res.append(lst.pop(idx))
        idx += K - 1

print('<', end='')
for i in range(N-1):
    print(res[i], end=', ')
print(res[-1], end='')
print('>')