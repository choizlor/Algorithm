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
                if val < 0:
                    dfs(-(-val // num[depth]), depth)
                else:
                    dfs(int(val // num[depth]), depth)
            mat[i] += 1


N = int(input())
num = list(map(int, input().split()))
mat = list(map(int, input().split()))

maxV = -1000000000
minV = 1000000000
dfs(num[0], 0)
print(maxV)
print(minV)
