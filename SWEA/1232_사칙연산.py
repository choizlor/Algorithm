def math_f(n):
    global s
    if tree[n]:
        math_f(c1[n])
        math_f(c2[n])
        if type(tree[n]) == int:
            s.append(tree[n])
        else:
            a = s.pop()
            b = s.pop()
            if tree[n] == '+':
                s.append(b + a)
            elif tree[n] == '-':
                s.append(b - a)
            elif tree[n] == '*':
                s.append(b * a)
            else:
                s.append(b / a)


for t in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    c1 = [0] * (N+1)
    c2 = [0] * (N+1)

    for _ in range(N):
        a = input().split()

        if len(a) == 4:
            tree[int(a[0])] = a[1]
            c1[int(a[0])] = int(a[2])
            c2[int(a[0])] = int(a[3])

        else:
            tree[int(a[0])] = int(a[1])

    s = []
    math_f(1)
    print(f'#{t} {int(s[0])}')
