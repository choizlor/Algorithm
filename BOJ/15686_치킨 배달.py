def comb(L, BeginWith):
    # 종료조건 (depth, level 등)
    if L == M:
        xy = result[:]
        chickenC.append(xy)
    else:
        for i in range(BeginWith, len(chicken)):
            result[L] = chicken[i]
            comb(L + 1, i + 1)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            home.append([x,y])
        elif arr[x][y] == 2:
            chicken.append([x,y])

result = [False] * M
chickenC = []
comb(0,0)

answer = 1000000
for c in chickenC:
    sumV = 0
    for h in home:
        minV = 1000000
        for i in range(M):
            dist = abs(h[0] - c[i][0]) + abs(h[1] - c[i][1])
            if minV > dist:
                minV = dist
        sumV += minV
    if answer > sumV:
        answer = sumV

print(answer)