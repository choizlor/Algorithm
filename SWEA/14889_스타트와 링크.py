def DFS(L, BeginWith):
    global minV, cnt
    # 종료조건 (depth, level 등)
    if L == r:
        team1, team2 = 0, 0
        t1 = result[:]
        t2 = [i for i in lst if i not in t1]
        for i in t1:
            for j in t1:
                if i != j and arr[i][j]:
                   team1 += arr[i][j]
        for i in t2:
            for j in t2:
                if i != j and arr[i][j]:
                    team2 += arr[i][j]
        if minV > abs(team1 - team2):
            minV = abs(team1 - team2)

    else:
        for i in range(BeginWith, len(lst)):
            result[L] = lst[i]
            DFS(L + 1, i + 1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = [i for i in range(N)]
r = N//2
result = [False] * r
minV = 100000
DFS(0, 0)
print(minV)
