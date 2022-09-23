def solve(k, r, c, d):
    # 끝나는 조건
    if d == 3 and r == stR and c == stC:
        answer.append(k)
        return

    # r과 c가 범위를 벗어나거나, 같은 디저트면
    if 0 > r or N <= r or 0 > c or N <= c or (ARR[r][c] in result):
        return

    if len(answer) > 0:
        if d == 2 and k < max(answer) // 2:
            return

    result.append(ARR[r][c])
    newR, newC = r + dr[d], c + dc[d]
    solve(k + 1, newR, newC, d)
    d = (d + 1) % 4
    newR, newC = r + dr[d], c + dc[d]
    solve(k + 1, newR, newC, d)
    result.pop()


dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    answer = []

    for r in range(N):
        for c in range(N):
            stR, stC = r, c
            result = []
            solve(0, r, c, 0)

    if len(answer) == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max(answer)}')