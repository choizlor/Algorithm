def pre(root):
    if root:
        pre(c1[root])
        result.append(ch[root])
        pre(c2[root])
 
 
for t in range(1, 11):
    N = int(input())
    ch = [''] * (N+1)
    c1 = [0] * (N+1)
    c2 = [0] * (N+1)
    result = []
 
    for _ in range(N):
        a = list(input().split())
        ch[int(a[0])] = a[1]
 
        if len(a) > 2:
            for i in range(2, len(a)):
                if i == 2:
                    c1[int(a[0])] = int(a[i])
                else:
                    c2[int(a[0])] = int(a[i])
     
    pre(1)
    a = ''.join(result)
    print(f'#{t} {a}')