def dfs(val, depth):
    global maxV, minV

    if not max(mat):
        if maxV < val:
            maxV = val
        if minV > val:
            minV = val
        return

    depth += 1
    for i in range(4):
        if mat[i]:
            mat[i] -= 1
            if i == 0:
                dfs(val + num[depth], depth)
            elif i == 1:
                dfs(val - num[depth], depth)
            elif i == 2:
                dfs(val * num[depth], depth)
            else:
                dfs(int(val / num[depth]), depth)
            mat[i] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = list(map(int, input().split()))
    num = list(map(int, input().split()))

    maxV = -100000
    minV = 1000000
    dfs(num[0], 0)
    print(f'#{tc} {maxV - minV}')
