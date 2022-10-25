def f(i, k):
    if i == k:
        lst = p[:]
        if lst not in result:
            check = 0
            for j in range(k//2):
                if p[j] == p[k-1-j]:
                    check += 1
            if check == k//2:
                result.append(lst)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]


p = sorted(list(input()))
result = []
f(0, len(p))
if result:
    print(''.join(result[0]))
else:
    print("I'm Sorry Hansoo")