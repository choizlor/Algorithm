def par(k, midSum):
    global maxV

    if k > N:
        return

    if k == N:
        if maxV < midSum:
            maxV = midSum
        return

    par(k + T[k], midSum + P[k])
    par(k + 1, midSum)


N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

maxV = 0
par(0, 0)
print(maxV)