# def bfs(pipe):
#     global cnt
#     while len(pipe) >= 2:
#         if pipe[-1] == [N-1, N-1]:
#             cnt += 1
#             pipe.pop()
#
#         a = abs(pipe[0][0] - pipe[1][0])
#         b = abs(pipe[0][1] - pipe[1][1])
#
#         if a == 0 and b == 1:   # 가로
#             x, y = pipe.pop(0)
#             dia = 0
#
#             for dx, dy in [[0, 2], [1, 1], [1, 2]]:
#                 nx = x + dx
#                 ny = y + dy
#                 if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
#                     dia += 1
#             if dia == 3:
#                 pipe.append([x + 1, y + 2])
#
#             if 0 <= x < N and 0 <= y + 2 < N and arr[x][y+2] == 0:
#                 arr[x][y+2] = 1
#                 pipe.append([x,y+2])
#
#         elif a == 1 and b == 0: # 세로
#             x, y = pipe.pop(0)
#             dia = 0
#             for dx, dy in [[2, 0], [1, 1], [2, 1]]:
#                 nx = x + dx
#                 ny = y + dy
#                 if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
#                     dia += 1
#             if dia == 3:
#                 pipe.append([x + 2, y + 1])
#
#             if 0 <= x + 2 < N and 0 <= y < N and arr[x + 2][y] == 0:
#                 arr[x + 2][y] = 1
#                 pipe.append([x + 2, y])
#
#         elif a == 1 and b == 1: # 대각선
#             x, y = pipe.pop(0)
#             dia = 0
#             for dx, dy in [[1, 2], [2, 2], [2, 1]]:
#                 nx = x + dx
#                 ny = y + dy
#                 if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
#                     dia += 1
#             if dia == 3:
#                 pipe.append([x + 2, y + 1])
#
#             if 0 <= x + 1 < N and 0 <= y + 2 < N and arr[x + 1][y + 2] == 0:
#                 arr[x + 1][y + 2] = 1
#                 pipe.append([x + 1, y + 2])
#
#             if 0 <= x + 2 < N and 0 <= y + 1 < N and arr[x + 2][y + 1] == 0:
#                 arr[x + 2][y + 1] = 1
#                 pipe.append([x + 2, y + 1])
#
def dfs(x, y, direction):
    global cnt
    if x == N - 1 and y == N - 1:
        cnt += 1

    if direction == 0:
        if y + 1 < N and s[x][y+1] == 0:
            dfs(x, y+1, 0)
        if x + 1 < N and y + 1 < N:
            if s[x][y+1] == 0 and s[x+1][y+1] == 0 and s[x+1][y] == 0:
                dfs(x+1, y+1, 2)

    elif direction == 1:
        if x + 1 < N and s[x + 1][y] == 0:
            dfs(x + 1, y, 1)
        if x + 1 < N and y + 1 < N:
            if s[x][y+1] == 0 and s[x+1][y+1] == 0 and s[x+1][y] == 0:
                dfs(x+1, y+1, 2)

    elif direction == 2:
        if y + 1 < N and s[x][y+1] == 0:
            dfs(x, y+1, 0)
        if x + 1 < N and s[x + 1][y] == 0:
            dfs(x + 1, y, 1)
        if x + 1 < N and y + 1 < N:
            if s[x][y+1] == 0 and s[x+1][y+1] == 0 and s[x+1][y] == 0:
                dfs(x+1, y+1, 2)



N = int(input())
s = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs(0, 1, 0)
print(cnt)