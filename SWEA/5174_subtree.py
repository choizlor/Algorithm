def tree(n):
    global result
    if n == 0:
        return
    result += 1 
    tree(c1[n])
    tree(c2[n])

tc = int(input())
for t in range(1, tc+1):
    E, N = map(int, input().split())
    c1 = [0] * (E+2)
    c2 = [0] * (E+2)
    lst = list(map(int, input().split()))
    result = 0

    for i in range(0, E*2, 2):
        if c1[lst[i]]:
            c2[lst[i]] = lst[i+1]

        else:
            c1[lst[i]] = lst[i+1]
    
    tree(N)

    print(f'#{t} {result}')