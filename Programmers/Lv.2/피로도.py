answer = 0
V = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not V[i]:
            V[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons)
            V[i] = 0


def solution(k, dungeons):
    global V
    V = [0 for _ in range(len(dungeons))]
    dfs(k, 0, dungeons)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
